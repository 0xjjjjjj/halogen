#include <SDL.h>
#include <SDL_vulkan.h>

#include "context.hpp"
#include "device.hpp"
#include "wsi.hpp"
#include "command_buffer.hpp"
#include "image.hpp"
#include "thread_id.hpp"

#include "gs_interface.hpp"
#include "gs_dump_parser.hpp"

#include "ps2_runtime.h"
#include "ps2_syscalls.h"
#include "ps2_stubs.h"
#include "Stubs/Audio.h"
#include "Stubs/GS.h"
#include "Stubs/MPEG.h"
// #include "register_functions.h" // upstream: registration is now static array init

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

// Upstream GifArbiter emits (data,size); Snowblind routes GS via VU1 XGKICK (path=1).
static void halogen_gs_arbiter_adapter(const uint8_t *data, uint32_t size_bytes)
{
    halogen_gs_transfer_cb(1, data, size_bytes);
}

static void build_priv_regs_buffer(uint8_t *dst_8k, const GSRegisters &gs)
{
    std::memset(dst_8k, 0, 8192);
    auto put = [dst_8k](int idx, uint64_t val) {
        std::memcpy(dst_8k + idx * 16, &val, sizeof(val));
    };
    put(0,  gs.pmode);
    put(1,  gs.smode1);
    put(2,  gs.smode2);
    put(3,  gs.srfsh);
    put(4,  gs.synch1);
    put(5,  gs.synch2);
    put(6,  gs.syncv);
    put(7,  gs.dispfb1);
    put(8,  gs.display1);
    put(9,  gs.dispfb2);
    put(10, gs.display2);
    put(11, gs.extbuf);
    put(12, gs.extdata);
    put(13, gs.extwrite);
    put(14, gs.bgcolor);
    put(15, gs.csr.load(std::memory_order_relaxed));
    put(16, gs.imr);
    put(17, gs.busdir);
    put(18, gs.siglblid);
}

static void halogen_gs_vsync_cb(const uint8_t *priv_regs_8k)
{
    if (!g_ifacePtr) return;
    if (priv_regs_8k)
    {
        uint8_t fixed[8192];
        std::memcpy(fixed, priv_regs_8k, 8192);
        // Fill NTSC defaults for regs upstream GsSetCrt stub leaves zero.
        uint64_t smode1;
        std::memcpy(&smode1, fixed + 1 * 16, 8);
        if (smode1 == 0)
        {
            smode1 = (uint64_t(32) << 3) | (uint64_t(2) << 13);
            std::memcpy(fixed + 1 * 16, &smode1, 8);
        }
        uint64_t smode2;
        std::memcpy(&smode2, fixed + 2 * 16, 8);
        if (smode2 == 0)
        {
            smode2 = 0x3;
            std::memcpy(fixed + 2 * 16, &smode2, 8);
        }
        for (int idx : {8, 10})
        {
            uint64_t v;
            std::memcpy(&v, fixed + idx * 16, 8);
            uint32_t hi = uint32_t(v >> 32);
            if (hi == 0)
            {
                uint32_t magh = uint32_t((v >> 23) & 0xF);
                uint32_t dw_dots = 640u * (magh + 1u) - 1u;
                uint64_t dwdh_hi = (uint64_t(dw_dots) & 0xFFF) | (uint64_t(447) << 12);
                v = (v & 0xFFFFFFFFULL) | (dwdh_hi << 32);
                std::memcpy(fixed + idx * 16, &v, 8);
            }
        }
        std::memcpy(&g_ifacePtr->get_priv_register_state(),
                    fixed,
                    sizeof(PrivRegisterState));
        uint64_t n = g_vsyncCount.load(std::memory_order_relaxed);
        if (n < 240 || (n % 60) == 0)
        {
            uint64_t pmode, dispfb1, display1, dispfb2, display2, bgcolor;
            std::memcpy(&pmode, priv_regs_8k + 0, 8);
            std::memcpy(&dispfb1, priv_regs_8k + 7 * 16, 8);
            std::memcpy(&display1, priv_regs_8k + 8 * 16, 8);
            std::memcpy(&dispfb2, priv_regs_8k + 9 * 16, 8);
            std::memcpy(&display2, priv_regs_8k + 10 * 16, 8);
            std::memcpy(&bgcolor, priv_regs_8k + 14 * 16, 8);
            uint32_t d1_dx = uint32_t(display1) & 0xFFF;
            uint32_t d1_dy = uint32_t(display1 >> 12) & 0x7FF;
            uint32_t d1_magh = uint32_t(display1 >> 23) & 0xF;
            uint32_t d1_magv = uint32_t(display1 >> 27) & 0x3;
            uint32_t d1_dw = uint32_t(display1 >> 32) & 0xFFF;
            uint32_t d1_dh = uint32_t(display1 >> 44) & 0x7FF;
            uint32_t d2_dx = uint32_t(display2) & 0xFFF;
            uint32_t d2_dy = uint32_t(display2 >> 12) & 0x7FF;
            uint32_t d2_magh = uint32_t(display2 >> 23) & 0xF;
            uint32_t d2_magv = uint32_t(display2 >> 27) & 0x3;
            uint32_t d2_dw = uint32_t(display2 >> 32) & 0xFFF;
            uint32_t d2_dh = uint32_t(display2 >> 44) & 0x7FF;
            fprintf(stderr, "[vsync#%llu] pmode=0x%llx dispfb1=0x%llx dispfb2=0x%llx bgcolor=0x%llx\n"
                            "  display1 dx=%u dy=%u magh=%u magv=%u dw=%u dh=%u\n"
                            "  display2 dx=%u dy=%u magh=%u magv=%u dw=%u dh=%u\n",
                    (unsigned long long)n,
                    (unsigned long long)pmode,
                    (unsigned long long)dispfb1,
                    (unsigned long long)dispfb2,
                    (unsigned long long)bgcolor,
                    d1_dx, d1_dy, d1_magh, d1_magv, d1_dw, d1_dh,
                    d2_dx, d2_dy, d2_magh, d2_magv, d2_dw, d2_dh);
        }
    }
    g_ifacePtr->flush();

    VSyncInfo info = {};
    info.phase = 0;
    info.dst_layout = VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL;
    info.dst_stage = VK_PIPELINE_STAGE_TRANSFER_BIT;
    info.dst_access = VK_ACCESS_TRANSFER_READ_BIT;
    info.adapt_to_internal_horizontal_resolution = true;
    info.force_progressive = false;
    info.anti_blur = true;
    info.raw_circuit_scanout = false;

    ScanoutResult sr = g_ifacePtr->vsync(info);
    uint64_t vn = g_vsyncCount.fetch_add(1, std::memory_order_relaxed);
    if (vn < 240 || (vn % 60) == 0)
    {
        uint32_t iw = 0, ih = 0;
        if (sr.image)
        {
            const auto &ci = sr.image->get_create_info();
            iw = ci.width;
            ih = ci.height;
        }
        fprintf(stderr, "[vsync#%llu] sr.image=%p int=%ux%u img=%ux%u\n",
                (unsigned long long)vn, (void *)sr.image.get(),
                sr.internal_width, sr.internal_height, iw, ih);
    }

    std::lock_guard<std::mutex> lk(g_scanoutMutex);
    g_latestScanout = sr;
    g_haveNewScanout = true;
}

static void blit_scanout_to_swapchain(CommandBuffer &cmd, const Image &dst, const Image &src,
                                      uint32_t srcW, uint32_t srcH)
{
    const auto &dc = dst.get_create_info();
    const auto &sc = src.get_create_info();
    if (srcW == 0 || srcW > sc.width) srcW = sc.width;
    if (srcH == 0 || srcH > sc.height) srcH = sc.height;

    cmd.full_barrier();

    cmd.image_barrier(dst,
                      VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL, VK_IMAGE_LAYOUT_TRANSFER_DST_OPTIMAL,
                      VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT,
                      VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT,
                      VK_PIPELINE_STAGE_TRANSFER_BIT, VK_ACCESS_TRANSFER_WRITE_BIT);

    VkImageBlit region = {};
    region.srcSubresource.aspectMask = VK_IMAGE_ASPECT_COLOR_BIT;
    region.srcSubresource.layerCount = 1;
    region.srcOffsets[1] = {int32_t(srcW), int32_t(srcH), 1};
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

    if (!runtime.syncCoreSubsystems())
    {
        std::cerr << "[gui/guest] syncCoreSubsystems failed" << std::endl;
        g_runtime.store(nullptr);
        return 1;
    }

    runtime.setMissingFunctionPolicy(PS2Runtime::MissingFunctionPolicy::Stop);

    // Steal the arbiter route away from upstream's raylib rasterizer → parallel-gs.
    runtime.gifArbiter().setProcessPacketFn(&halogen_gs_arbiter_adapter);

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

    ps2_stubs::resetSifState();
    ps2_stubs::resetAudioStubState();
    ps2_stubs::resetGsSyncVCallbackState();
    ps2_stubs::resetMpegStubState();

    uint8_t *rdram = runtime.memory().getRDRAM();
    ps2_syscalls::initializeGuestKernelState(rdram);

    R5900Context &ctx = runtime.cpu();
    ctx.r[4] = _mm_setzero_si128();
    ctx.r[5] = _mm_setzero_si128();
    ctx.r[29] = _mm_set_epi64x(0, static_cast<int64_t>(PS2_RAM_SIZE - 0x10u));

    ps2_syscalls::EnsureVSyncWorkerRunning(rdram, &runtime);

    int exitCode = 0;
    try
    {
        runtime.dispatchLoop(rdram, &ctx);
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

    if (!wsi.init_simple(2, {}))
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
    std::atomic<int> guestExit{0};
    std::thread guestThread;
    if (!replayMode)
    {
        guestThread = std::thread([&]()
        {
            Util::register_thread_index(1);
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
    uint64_t lastVsyncTick = 0;
    bool guestEverSeen = false;
    auto startTime = std::chrono::steady_clock::now();
    while (platform.alive(wsi))
    {
        if (!replayMode)
        {
            auto *rt = g_runtime.load(std::memory_order_acquire);
            if (rt != nullptr) guestEverSeen = true;
            if (rt == nullptr && guestEverSeen)
            {
                std::cerr << "[halogen-gui] guest exited, closing window" << std::endl;
                break;
            }

            if (rt != nullptr)
            {
                uint64_t curTick = ps2_syscalls::GetCurrentVSyncTick();
                if (curTick != lastVsyncTick)
                {
                    lastVsyncTick = curTick;
                    uint8_t priv[8192];
                    build_priv_regs_buffer(priv, rt->memory().gs());
                    halogen_gs_vsync_cb(priv);
                }
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
            local = g_latestScanout;
            hasNew = g_haveNewScanout;
            g_haveNewScanout = false;
        }

        auto cmd = device.request_command_buffer();
        const auto &swapImg = device.get_swapchain_view().get_image().get_create_info();
        if (local.image)
        {
            auto rp = device.get_swapchain_render_pass(SwapchainRenderPass::ColorOnly);
            rp.clear_color[0].float32[0] = 0.0f;
            rp.clear_color[0].float32[1] = 0.0f;
            rp.clear_color[0].float32[2] = 0.0f;
            rp.clear_color[0].float32[3] = 1.0f;
            cmd->begin_render_pass(rp);
            cmd->end_render_pass();
            blit_scanout_to_swapchain(*cmd, device.get_swapchain_view().get_image(), *local.image,
                                      0, 0);
            if (hasNew) presentedScanouts++;
            if (frame < 240 || (frame % 60) == 0)
            {
                const auto &srcCi = local.image->get_create_info();
                fprintf(stderr, "[frame#%llu] %s swap=%ux%u img=%ux%u int=%ux%u mode=%ux%u\n",
                        (unsigned long long)frame, hasNew ? "BLIT" : "REBLIT",
                        swapImg.width, swapImg.height,
                        srcCi.width, srcCi.height,
                        local.internal_width, local.internal_height,
                        local.mode_width, local.mode_height);
            }
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
            if (frame < 240 || (frame % 60) == 0)
            {
                fprintf(stderr, "[frame#%llu] CLEAR swap=%ux%u (no scanout yet)\n",
                        (unsigned long long)frame, swapImg.width, swapImg.height);
            }
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
