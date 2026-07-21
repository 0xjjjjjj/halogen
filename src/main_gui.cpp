#include <SDL.h>
#include <SDL_vulkan.h>

#include "context.hpp"
#include "device.hpp"
#include "wsi.hpp"
#include "command_buffer.hpp"
#include "image.hpp"

#include "gs_interface.hpp"
#include "gs_dump_parser.hpp"

#include "ps2_runtime.h"
#include "ps2_syscalls.h"
#include "ps2_stubs.h"
#include "register_functions.h"

#include <atomic>
#include <chrono>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <mutex>
#include <string>
#include <thread>
#include <vector>

using namespace Vulkan;
using namespace ParallelGS;

namespace {

class HalogenPlatform : public WSIPlatform
{
public:
    explicit HalogenPlatform(SDL_Window *win) : window(win)
    {
        int w = 0, h = 0;
        SDL_Vulkan_GetDrawableSize(window, &w, &h);
        width = uint32_t(w);
        height = uint32_t(h);
    }

    VkSurfaceKHR create_surface(VkInstance instance, VkPhysicalDevice) override
    {
        VkSurfaceKHR surface = VK_NULL_HANDLE;
        if (!SDL_Vulkan_CreateSurface(window, instance, &surface))
        {
            fprintf(stderr, "[halogen-gui] SDL_Vulkan_CreateSurface: %s\n", SDL_GetError());
            return VK_NULL_HANDLE;
        }
        return surface;
    }

    std::vector<const char *> get_instance_extensions() override
    {
        unsigned count = 0;
        SDL_Vulkan_GetInstanceExtensions(window, &count, nullptr);
        std::vector<const char *> exts(count);
        SDL_Vulkan_GetInstanceExtensions(window, &count, exts.data());
        return exts;
    }

    uint32_t get_surface_width() override { return width; }
    uint32_t get_surface_height() override { return height; }

    bool alive(WSI &) override
    {
        SDL_Event ev;
        while (SDL_PollEvent(&ev))
        {
            switch (ev.type)
            {
            case SDL_QUIT:
                running = false;
                break;
            case SDL_WINDOWEVENT:
                if (ev.window.event == SDL_WINDOWEVENT_SIZE_CHANGED ||
                    ev.window.event == SDL_WINDOWEVENT_RESIZED)
                {
                    int w = 0, h = 0;
                    SDL_Vulkan_GetDrawableSize(window, &w, &h);
                    width = uint32_t(w);
                    height = uint32_t(h);
                    resize = true;
                }
                break;
            case SDL_KEYDOWN:
                if (ev.key.keysym.sym == SDLK_ESCAPE)
                    running = false;
                break;
            default:
                break;
            }
        }
        return running;
    }

    void poll_input() override {}
    void poll_input_async(Granite::InputTrackerHandler *) override {}

private:
    SDL_Window *window = nullptr;
    uint32_t width = 640;
    uint32_t height = 448;
    bool running = true;
};

struct GuestArgs
{
    std::string elfPath;
    std::string cdRoot;
};

static std::atomic<PS2Runtime *> g_runtime{nullptr};
static std::atomic<uint64_t> g_gifTransferCount{0};
static std::atomic<uint64_t> g_vsyncCount{0};

static GSInterface *g_ifacePtr = nullptr;
static std::mutex g_scanoutMutex;
static ScanoutResult g_latestScanout = {};
static bool g_haveNewScanout = false;

static void halogen_gs_transfer_cb(uint8_t path, const void *data, uint32_t size_bytes)
{
    if (!g_ifacePtr) return;
    g_ifacePtr->gif_transfer(path, data, size_bytes);
    g_gifTransferCount.fetch_add(1, std::memory_order_relaxed);
}

static void halogen_gs_vsync_cb(const uint8_t *priv_regs_8k)
{
    if (!g_ifacePtr) return;
    if (priv_regs_8k)
    {
        std::memcpy(&g_ifacePtr->get_priv_register_state(),
                    priv_regs_8k,
                    sizeof(PrivRegisterState));
    }
    g_ifacePtr->flush();

    VSyncInfo info = {};
    info.phase = 0;
    info.dst_layout = VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL;
    info.dst_stage = VK_PIPELINE_STAGE_TRANSFER_BIT;
    info.dst_access = VK_ACCESS_TRANSFER_READ_BIT;
    info.adapt_to_internal_horizontal_resolution = true;

    ScanoutResult sr = g_ifacePtr->vsync(info);
    g_vsyncCount.fetch_add(1, std::memory_order_relaxed);

    std::lock_guard<std::mutex> lk(g_scanoutMutex);
    g_latestScanout = sr;
    g_haveNewScanout = true;
}

static void blit_scanout_to_swapchain(CommandBuffer &cmd, const Image &dst, const Image &src)
{
    const auto &dc = dst.get_create_info();
    const auto &sc = src.get_create_info();

    cmd.full_barrier();

    cmd.image_barrier(dst,
                      VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL, VK_IMAGE_LAYOUT_TRANSFER_DST_OPTIMAL,
                      VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT,
                      VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT,
                      VK_PIPELINE_STAGE_TRANSFER_BIT, VK_ACCESS_TRANSFER_WRITE_BIT);

    VkImageBlit region = {};
    region.srcSubresource.aspectMask = VK_IMAGE_ASPECT_COLOR_BIT;
    region.srcSubresource.layerCount = 1;
    region.srcOffsets[1] = {int32_t(sc.width), int32_t(sc.height), 1};
    region.dstSubresource.aspectMask = VK_IMAGE_ASPECT_COLOR_BIT;
    region.dstSubresource.layerCount = 1;
    region.dstOffsets[1] = {int32_t(dc.width), int32_t(dc.height), 1};

    vkCmdBlitImage(cmd.get_command_buffer(),
                   src.get_image(), VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL,
                   dst.get_image(), VK_IMAGE_LAYOUT_TRANSFER_DST_OPTIMAL,
                   1, &region, VK_FILTER_LINEAR);

    cmd.image_barrier(dst,
                      VK_IMAGE_LAYOUT_TRANSFER_DST_OPTIMAL, VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL,
                      VK_PIPELINE_STAGE_TRANSFER_BIT, VK_ACCESS_TRANSFER_WRITE_BIT,
                      VK_PIPELINE_STAGE_ALL_COMMANDS_BIT,
                      VK_ACCESS_MEMORY_READ_BIT | VK_ACCESS_MEMORY_WRITE_BIT);
}

static int run_guest_dispatch(const GuestArgs &args)
{
    PS2Runtime runtime;
    g_runtime.store(&runtime, std::memory_order_release);

    if (!runtime.memory().initialize())
    {
        std::cerr << "[gui/guest] failed to initialize PS2 memory" << std::endl;
        g_runtime.store(nullptr);
        return 1;
    }

    registerAllFunctions(runtime);

    if (!runtime.loadELF(args.elfPath))
    {
        std::cerr << "[gui/guest] failed to load ELF: " << args.elfPath << std::endl;
        g_runtime.store(nullptr);
        return 1;
    }

    std::cerr << "[gui/guest] ELF loaded, entry=0x" << std::hex << runtime.cpu().pc
              << std::dec << std::endl;

    if (!args.cdRoot.empty())
    {
        auto paths = PS2Runtime::getIoPaths();
        paths.cdRoot = args.cdRoot;
        PS2Runtime::setIoPaths(paths);
        std::cerr << "[gui/guest] CD root: " << args.cdRoot << std::endl;
    }

    R5900Context &ctx = runtime.cpu();
    ctx.r[4] = _mm_setzero_si128();
    ctx.r[5] = _mm_setzero_si128();
    ctx.r[29] = _mm_set_epi64x(0, static_cast<int64_t>(PS2_RAM_SIZE - 0x10u));

    ps2_syscalls::setMainThread();

    uint8_t *rdram = runtime.memory().getRDRAM();
    int exitCode = 0;

    try
    {
        while (!runtime.isStopRequested())
        {
            uint32_t pc = ctx.pc;
            if (pc == 0u)
            {
                std::cerr << "[gui/guest] PC=0, clean exit" << std::endl;
                break;
            }
            auto fn = runtime.lookupFunction(pc);

            ps2_syscalls::getGuestExecMutex().lock();
            fn(rdram, &ctx, &runtime);
            ps2_syscalls::pollVBlank(rdram, &runtime);
            ps2_syscalls::getGuestExecMutex().unlock();
        }
    }
    catch (const std::exception &e)
    {
        std::cerr << "[gui/guest] EXCEPTION: " << e.what() << std::endl;
        exitCode = 1;
    }

    std::cerr << "[gui/guest] exit, final_pc=0x" << std::hex << ctx.pc << std::dec
              << " transfers=" << g_gifTransferCount.load()
              << " vsyncs=" << g_vsyncCount.load() << std::endl;
    g_runtime.store(nullptr);
    return exitCode;
}

static void printUsage(const char *prog)
{
    std::cerr << "Usage: " << prog << " [--cd-root DIR] <elf_file>\n";
}

}

int main(int argc, char **argv)
{
    GuestArgs gargs;
    for (int i = 1; i < argc; ++i)
    {
        std::string a = argv[i];
        if (a == "--cd-root" && i + 1 < argc)
            gargs.cdRoot = argv[++i];
        else if (a == "--help" || a == "-h")
        {
            printUsage(argv[0]);
            return 0;
        }
        else if (!a.empty() && a[0] == '-')
        {
            std::cerr << "Unknown option: " << a << std::endl;
            printUsage(argv[0]);
            return 1;
        }
        else
            gargs.elfPath = a;
    }

    if (gargs.elfPath.empty())
    {
        std::cerr << "Error: no ELF specified" << std::endl;
        printUsage(argv[0]);
        return 1;
    }

    if (SDL_Init(SDL_INIT_VIDEO) < 0)
    {
        fprintf(stderr, "[halogen-gui] SDL_Init failed: %s\n", SDL_GetError());
        return EXIT_FAILURE;
    }

    SDL_Window *window = SDL_CreateWindow(
        "halogen",
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        1280, 896,
        SDL_WINDOW_VULKAN | SDL_WINDOW_RESIZABLE | SDL_WINDOW_ALLOW_HIGHDPI);
    if (!window)
    {
        fprintf(stderr, "[halogen-gui] SDL_CreateWindow failed: %s\n", SDL_GetError());
        SDL_Quit();
        return EXIT_FAILURE;
    }

    if (!Context::init_loader(nullptr))
    {
        fprintf(stderr, "[halogen-gui] Vulkan loader init failed\n");
        SDL_DestroyWindow(window);
        SDL_Quit();
        return EXIT_FAILURE;
    }

    HalogenPlatform platform(window);
    WSI wsi;
    wsi.set_platform(&platform);
    wsi.set_backbuffer_format(BackbufferFormat::UNORM);
    wsi.set_present_mode(PresentMode::SyncToVBlank);

    if (!wsi.init_simple(1, {}))
    {
        fprintf(stderr, "[halogen-gui] WSI init failed\n");
        SDL_DestroyWindow(window);
        SDL_Quit();
        return EXIT_FAILURE;
    }

    Device &device = wsi.get_device();

    GSInterface iface;
    GSOptions gs_opts = {};
    if (!iface.init(&device, gs_opts))
    {
        fprintf(stderr, "[halogen-gui] GSInterface::init failed\n");
        return EXIT_FAILURE;
    }
    g_ifacePtr = &iface;

    const char *replayPath = std::getenv("HALOGEN_GS_REPLAY");
    GSDumpParser replayParser;
    bool replayMode = false;
    if (replayPath && replayPath[0])
    {
        if (!replayParser.open(replayPath, 4 * 1024 * 1024, &iface))
        {
            fprintf(stderr, "[halogen-gui] GSDumpParser::open failed for %s\n", replayPath);
            return EXIT_FAILURE;
        }
        replayMode = true;
        fprintf(stderr, "[halogen-gui] REPLAY MODE: %s (guest skipped)\n", replayPath);
    }
    else
    {
        ps2_stubs::g_halogenGsTransfer = &halogen_gs_transfer_cb;
        ps2_stubs::g_halogenGsVSync = &halogen_gs_vsync_cb;
    }

    std::atomic<int> guestExit{0};
    std::thread guestThread;
    if (!replayMode)
    {
        guestThread = std::thread([&]()
        {
            guestExit.store(run_guest_dispatch(gargs), std::memory_order_release);
        });
        fprintf(stderr, "[halogen-gui] guest launched, entering render loop\n");
    }
    else
    {
        fprintf(stderr, "[halogen-gui] entering replay render loop\n");
    }

    uint64_t frame = 0;
    uint64_t presentedScanouts = 0;
    auto startTime = std::chrono::steady_clock::now();
    while (platform.alive(wsi))
    {
        if (!replayMode)
        {
            if (auto *rt = g_runtime.load(std::memory_order_acquire); rt == nullptr && frame > 0)
            {
                std::cerr << "[halogen-gui] guest exited, closing window" << std::endl;
                break;
            }
        }

        if (!wsi.begin_frame())
            continue;

        if (replayMode)
        {
            bool more = replayParser.iterate_until_vsync(false);
            ScanoutResult sr = replayParser.consume_vsync_result();
            g_vsyncCount.fetch_add(1, std::memory_order_relaxed);
            std::lock_guard<std::mutex> lk(g_scanoutMutex);
            g_latestScanout = sr;
            g_haveNewScanout = true;
            if (!more)
                replayParser.restart();
        }

        ScanoutResult local = {};
        bool hasNew = false;
        {
            std::lock_guard<std::mutex> lk(g_scanoutMutex);
            if (g_haveNewScanout)
            {
                local = g_latestScanout;
                g_haveNewScanout = false;
                hasNew = true;
            }
        }

        auto cmd = device.request_command_buffer();
        if (hasNew && local.image)
        {
            auto rp = device.get_swapchain_render_pass(SwapchainRenderPass::ColorOnly);
            rp.clear_color[0].float32[0] = 0.0f;
            rp.clear_color[0].float32[1] = 0.0f;
            rp.clear_color[0].float32[2] = 0.0f;
            rp.clear_color[0].float32[3] = 1.0f;
            cmd->begin_render_pass(rp);
            cmd->end_render_pass();
            blit_scanout_to_swapchain(*cmd, device.get_swapchain_view().get_image(), *local.image);
            presentedScanouts++;
        }
        else
        {
            auto rp = device.get_swapchain_render_pass(SwapchainRenderPass::ColorOnly);
            rp.clear_color[0].float32[0] = 0.05f;
            rp.clear_color[0].float32[1] = 0.05f;
            rp.clear_color[0].float32[2] = 0.08f;
            rp.clear_color[0].float32[3] = 1.0f;
            cmd->begin_render_pass(rp);
            cmd->end_render_pass();
        }
        device.submit(cmd);
        wsi.end_frame();
        frame++;

        if ((frame % 60) == 0)
        {
            auto now = std::chrono::steady_clock::now();
            auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(now - startTime).count();
            fprintf(stderr, "[halogen-gui] frame=%llu presented=%llu transfers=%llu vsyncs=%llu %lldms\n",
                    (unsigned long long)frame,
                    (unsigned long long)presentedScanouts,
                    (unsigned long long)g_gifTransferCount.load(),
                    (unsigned long long)g_vsyncCount.load(),
                    (long long)ms);
        }
    }

    ps2_stubs::g_halogenGsTransfer = nullptr;
    ps2_stubs::g_halogenGsVSync = nullptr;

    if (auto *rt = g_runtime.load(std::memory_order_acquire); rt != nullptr)
    {
        fprintf(stderr, "[halogen-gui] requesting guest stop\n");
        rt->requestStop();
    }

    if (guestThread.joinable())
        guestThread.join();

    g_ifacePtr = nullptr;

    fprintf(stderr, "[halogen-gui] exit: frames=%llu presented=%llu guest_exit=%d\n",
            (unsigned long long)frame,
            (unsigned long long)presentedScanouts,
            guestExit.load());

    wsi.deinit_surface_and_swapchain();
    SDL_DestroyWindow(window);
    SDL_Quit();
    return guestExit.load();
}
