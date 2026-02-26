// Headless main for crash-driven development.
// Skips Raylib window creation -- runs dispatchLoop directly on the main thread.
// Usage: halogen-headless [--trace] [--max-calls N] <elf_file>

#include "ps2_runtime.h"
#include "ps2_syscalls.h"
#include "register_functions.h"
#include <iostream>
#include <iomanip>
#include <string>
#include <csignal>
#include <cstdlib>
#include <chrono>
#include <thread>
#include <unordered_map>

// ---------------------------------------------------------------------------
// Globals for signal handler access
// ---------------------------------------------------------------------------
static PS2Runtime* g_runtime = nullptr;
static uint64_t g_callCount = 0;
static uint64_t g_maxCalls = 0;         // 0 = unlimited
static bool g_traceEnabled = false;
static uint32_t g_lastPC = 0;
static uint32_t g_prevPC = 0;           // PC two calls ago, for crash context

// MIPS register names for readable dumps
static const char* const kRegNames[32] = {
    "zero", "at", "v0", "v1", "a0", "a1", "a2", "a3",
    "t0",   "t1", "t2", "t3", "t4", "t5", "t6", "t7",
    "s0",   "s1", "s2", "s3", "s4", "s5", "s6", "s7",
    "t8",   "t9", "k0", "k1", "gp", "sp", "fp", "ra"
};

// ---------------------------------------------------------------------------
// CPU state dump -- more useful than the built-in dump() for crash analysis
// ---------------------------------------------------------------------------
static void dumpCPUState(const R5900Context& ctx, const char* reason)
{
    std::cerr << "\n===== CPU STATE DUMP =====" << std::endl;
    std::cerr << "Reason: " << reason << std::endl;
    std::cerr << "PC:  0x" << std::hex << std::setfill('0') << std::setw(8) << ctx.pc << std::endl;
    std::cerr << "Calls executed: " << std::dec << g_callCount << std::endl;
    std::cerr << "Previous PC: 0x" << std::hex << std::setw(8) << g_prevPC << std::endl;
    std::cerr << std::endl;

    // GPRs -- show low 32 bits and full 128 bits for non-zero upper halves
    for (int i = 0; i < 32; ++i)
    {
        uint32_t lo = static_cast<uint32_t>(_mm_extract_epi32(ctx.r[i], 0));
        uint32_t w1 = static_cast<uint32_t>(_mm_extract_epi32(ctx.r[i], 1));
        uint32_t w2 = static_cast<uint32_t>(_mm_extract_epi32(ctx.r[i], 2));
        uint32_t w3 = static_cast<uint32_t>(_mm_extract_epi32(ctx.r[i], 3));

        std::cerr << "$" << std::left << std::setfill(' ') << std::setw(5) << kRegNames[i]
                  << std::right << std::setfill('0');

        if (w1 == 0 && w2 == 0 && w3 == 0)
        {
            std::cerr << " 0x" << std::hex << std::setw(8) << lo;
        }
        else
        {
            std::cerr << " 0x" << std::hex
                      << std::setw(8) << w3 << "_"
                      << std::setw(8) << w2 << "_"
                      << std::setw(8) << w1 << "_"
                      << std::setw(8) << lo;
        }

        // Annotate common registers
        if (i == 29)
            std::cerr << "  (SP)";
        else if (i == 31)
            std::cerr << "  (RA)";
        else if (i == 28)
            std::cerr << "  (GP)";
        else if (i == 30)
            std::cerr << "  (FP)";

        std::cerr << std::dec << std::endl;
    }

    std::cerr << std::hex << std::setfill('0');
    std::cerr << "\nHI:  0x" << std::setw(16) << ctx.hi
              << "  LO:  0x" << std::setw(16) << ctx.lo << std::endl;
    std::cerr << "HI1: 0x" << std::setw(16) << ctx.hi1
              << "  LO1: 0x" << std::setw(16) << ctx.lo1 << std::endl;
    std::cerr << "SA:  0x" << std::setw(8) << ctx.sa << std::endl;

    // COP0 status/cause/epc
    std::cerr << "\nCOP0 Status: 0x" << std::setw(8) << ctx.cop0_status
              << "  Cause: 0x" << std::setw(8) << ctx.cop0_cause
              << "  EPC: 0x" << std::setw(8) << ctx.cop0_epc << std::endl;

    std::cerr << "===== END CPU STATE =====" << std::dec << std::endl;
}

// ---------------------------------------------------------------------------
// Signal handler -- dump state on SIGSEGV, SIGABRT, SIGFPE, SIGBUS
// ---------------------------------------------------------------------------
static volatile sig_atomic_t g_signalReceived = 0;

static void signalHandler(int sig)
{
    // Prevent re-entry
    if (g_signalReceived)
        _exit(128 + sig);
    g_signalReceived = 1;

    const char* sigName = "UNKNOWN";
    switch (sig)
    {
    case SIGINT:  sigName = "SIGINT (interrupt)"; break;
    case SIGSEGV: sigName = "SIGSEGV (segfault)"; break;
    case SIGABRT: sigName = "SIGABRT (abort)"; break;
    case SIGFPE:  sigName = "SIGFPE (floating point)"; break;
#ifdef SIGBUS
    case SIGBUS:  sigName = "SIGBUS (bus error)"; break;
#endif
    }

    std::cerr << "\n[headless] FATAL: caught " << sigName << std::endl;

    if (g_runtime)
    {
        std::cerr << "[headless] Last dispatched PC: 0x" << std::hex << g_lastPC << std::dec << std::endl;
        dumpCPUState(g_runtime->cpu(), sigName);
        g_runtime->requestStop();
    }

    // Re-raise so the OS records the signal properly
    signal(sig, SIG_DFL);
    raise(sig);
}

// ---------------------------------------------------------------------------
// Usage
// ---------------------------------------------------------------------------
static void printUsage(const char* prog)
{
    std::cerr << "Usage: " << prog << " [options] <elf_file>\n"
              << "\nOptions:\n"
              << "  --trace          Print each function PC as it executes\n"
              << "  --max-calls N    Stop after N function dispatches\n"
              << "  --cd-root DIR    Set CD filesystem root directory\n"
              << "  --help           Show this message\n"
              << std::endl;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------
int main(int argc, char* argv[])
{
    // Parse arguments
    std::string elfPath;
    std::string cdRoot;
    for (int i = 1; i < argc; ++i)
    {
        std::string arg = argv[i];
        if (arg == "--trace")
        {
            g_traceEnabled = true;
        }
        else if (arg == "--max-calls" && i + 1 < argc)
        {
            g_maxCalls = std::strtoull(argv[++i], nullptr, 10);
        }
        else if (arg == "--cd-root" && i + 1 < argc)
        {
            cdRoot = argv[++i];
        }
        else if (arg == "--help" || arg == "-h")
        {
            printUsage(argv[0]);
            return 0;
        }
        else if (arg[0] == '-')
        {
            std::cerr << "Unknown option: " << arg << std::endl;
            printUsage(argv[0]);
            return 1;
        }
        else
        {
            elfPath = arg;
        }
    }

    if (elfPath.empty())
    {
        std::cerr << "Error: no ELF file specified" << std::endl;
        printUsage(argv[0]);
        return 1;
    }

    // Set up signal handlers
    signal(SIGINT, signalHandler);
    signal(SIGSEGV, signalHandler);
    signal(SIGABRT, signalHandler);
    signal(SIGFPE, signalHandler);
#ifdef SIGBUS
    signal(SIGBUS, signalHandler);
#endif

    // Create runtime (does NOT create a window)
    PS2Runtime runtime;
    g_runtime = &runtime;

    // Initialize memory only -- no Raylib, no window
    std::cout << "[headless] Initializing PS2 memory..." << std::endl;
    if (!runtime.memory().initialize())
    {
        std::cerr << "[headless] FATAL: failed to initialize PS2 memory" << std::endl;
        return 1;
    }

    // Register all recompiled functions
    std::cout << "[headless] Registering recompiled functions..." << std::endl;
    registerAllFunctions(runtime);

    // Load ELF into PS2 memory
    std::cout << "[headless] Loading ELF: " << elfPath << std::endl;
    if (!runtime.loadELF(elfPath))
    {
        std::cerr << "[headless] FATAL: failed to load ELF: " << elfPath << std::endl;
        return 1;
    }

    std::cout << "[headless] ELF loaded. Entry: 0x" << std::hex << runtime.cpu().pc << std::dec << std::endl;

    // Override CD root if specified
    if (!cdRoot.empty())
    {
        auto paths = PS2Runtime::getIoPaths();
        paths.cdRoot = cdRoot;
        PS2Runtime::setIoPaths(paths);
        std::cout << "[headless] CD root: " << cdRoot << std::endl;
    }

    // Set up initial CPU state (mirrors PS2Runtime::run())
    R5900Context& ctx = runtime.cpu();
    ctx.r[4] = _mm_setzero_si128();                                          // a0 = 0
    ctx.r[5] = _mm_setzero_si128();                                          // a1 = 0
    ctx.r[29] = _mm_set_epi64x(0, static_cast<int64_t>(PS2_RAM_SIZE - 0x10u)); // SP near top of RAM

    // Verify entry point has a registered function
    if (!runtime.hasFunction(ctx.pc))
    {
        std::cerr << "[headless] WARNING: no registered function at entry PC 0x"
                  << std::hex << ctx.pc << std::dec << std::endl;
        std::cerr << "[headless] The dispatch loop will hit the unregistered-function handler immediately." << std::endl;
    }

    std::cout << "[headless] Starting dispatch loop"
              << (g_traceEnabled ? " (trace ON)" : "")
              << (g_maxCalls > 0 ? " (max " + std::to_string(g_maxCalls) + " calls)" : "")
              << "..." << std::endl;

    auto startTime = std::chrono::steady_clock::now();

    // Register this as the main dispatch thread — only the main thread
    // polls VBlank in cooperative WaitSema (worker threads just yield).
    ps2_syscalls::setMainThread();

    // -----------------------------------------------------------------------
    // Manual dispatch loop (instead of runtime.dispatchLoop) for trace/limit
    // -----------------------------------------------------------------------
    uint8_t* rdram = runtime.memory().getRDRAM();
    int exitCode = 0;

    try
    {
        while (!runtime.isStopRequested())
        {
            uint32_t pc = ctx.pc;
            g_prevPC = g_lastPC;
            g_lastPC = pc;

            // Null PC = normal exit
            if (pc == 0u)
            {
                std::cout << "[headless] PC reached 0x00000000 -- clean exit" << std::endl;
                break;
            }

            // Call limit
            if (g_maxCalls > 0 && g_callCount >= g_maxCalls)
            {
                std::cout << "[headless] Reached --max-calls limit (" << g_maxCalls << ")" << std::endl;
                break;
            }

            // Look up the recompiled function
            auto fn = runtime.lookupFunction(pc);

            // Trace output
            if (g_traceEnabled)
            {
                uint32_t ra = static_cast<uint32_t>(_mm_extract_epi32(ctx.r[31], 0));
                uint32_t sp = static_cast<uint32_t>(_mm_extract_epi32(ctx.r[29], 0));
                std::cout << "[trace] #" << std::dec << g_callCount
                          << " pc=0x" << std::hex << std::setfill('0') << std::setw(8) << pc
                          << " ra=0x" << std::setw(8) << ra
                          << " sp=0x" << std::setw(8) << sp
                          << std::dec << std::endl;
            }
            else if (g_callCount > 0 && (g_callCount % 100000) == 0)
            {
                // Periodic heartbeat so we know it's alive
                auto now = std::chrono::steady_clock::now();
                auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(now - startTime).count();
                std::cout << "[headless] " << g_callCount << " calls, "
                          << elapsed << "ms, pc=0x" << std::hex << pc << std::dec << std::endl;
            }

            // Dispatch — hold guest exec mutex to serialize with worker threads
            ++g_callCount;
            ps2_syscalls::getGuestExecMutex().lock();
            fn(rdram, &ctx, &runtime);
            // Cooperative VBlank: drain pending ticks and dispatch INTC
            // handlers on the main thread while still holding the mutex,
            // matching real PS2 where interrupts fire on the same core.
            ps2_syscalls::pollVBlank(rdram, &runtime);
            ps2_syscalls::getGuestExecMutex().unlock();
        }
    }
    catch (const std::exception& e)
    {
        std::cerr << "\n[headless] EXCEPTION: " << e.what() << std::endl;
        dumpCPUState(ctx, e.what());
        exitCode = 1;
    }
    catch (...)
    {
        std::cerr << "\n[headless] UNKNOWN EXCEPTION" << std::endl;
        dumpCPUState(ctx, "unknown exception");
        exitCode = 1;
    }

    // -----------------------------------------------------------------------
    // Summary
    // -----------------------------------------------------------------------
    auto endTime = std::chrono::steady_clock::now();
    auto elapsedMs = std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime).count();

    std::cout << "\n[headless] === Summary ===" << std::endl;
    std::cout << "[headless] Total calls:  " << g_callCount << std::endl;
    std::cout << "[headless] Elapsed:      " << elapsedMs << " ms" << std::endl;
    if (elapsedMs > 0)
    {
        double callsPerSec = static_cast<double>(g_callCount) / (static_cast<double>(elapsedMs) / 1000.0);
        std::cout << "[headless] Throughput:   " << std::fixed << std::setprecision(0)
                  << callsPerSec << " calls/sec" << std::endl;
    }
    std::cout << "[headless] Final PC:     0x" << std::hex << std::setfill('0') << std::setw(8)
              << ctx.pc << std::dec << std::endl;
    std::cout << "[headless] Final SP:     0x" << std::hex << std::setfill('0') << std::setw(8)
              << static_cast<uint32_t>(_mm_extract_epi32(ctx.r[29], 0)) << std::dec << std::endl;
    std::cout << "[headless] Final RA:     0x" << std::hex << std::setfill('0') << std::setw(8)
              << static_cast<uint32_t>(_mm_extract_epi32(ctx.r[31], 0)) << std::dec << std::endl;

    if (exitCode != 0)
    {
        dumpCPUState(ctx, "exit with error");
    }

    g_runtime = nullptr;
    return exitCode;
}
