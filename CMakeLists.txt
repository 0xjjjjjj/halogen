cmake_minimum_required(VERSION 3.20)
project(halogen LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# SSE4.1 for ps2_runtime_macros.h (_mm_extract_epi32)
if(NOT MSVC AND NOT CMAKE_SYSTEM_PROCESSOR MATCHES "arm64|aarch64|ARM64")
    add_compile_options(-msse4.1)
endif()

# --- Vendor: ps2_runtime static library ---
# Build ps2xRuntime as a subdirectory (brings in raylib via FetchContent)
add_subdirectory(vendor/PS2Recomp/ps2xRuntime)

# --- Vendor: parallel-gs (Vulkan GS emulator, LGPL-3.0+) ---
# Consumed as a library via PARALLEL_GS_STANDALONE=ON. Provides targets:
#   parallel-gs, granite-vulkan, granite-util, granite-application-global,
#   granite-application-global-init, granite-volk.
# Optional: skip if vendor tree isn't checked out (headless build still works).
if(EXISTS "${CMAKE_SOURCE_DIR}/vendor/parallel-gs/CMakeLists.txt")
    set(PARALLEL_GS_STANDALONE ON CACHE BOOL "" FORCE)
    add_subdirectory(vendor/parallel-gs EXCLUDE_FROM_ALL)
    set(HALOGEN_HAVE_PARALLEL_GS TRUE)
    find_package(SDL2 REQUIRED)
endif()

# --- Recompiled game code ---
# All 9,395 PS2Recomp-generated .cpp files
# RECOMP_DIR: override for short paths on Windows (e.g. -DRECOMP_DIR=C:/CoN)
if(NOT RECOMP_DIR)
    set(RECOMP_DIR "${CMAKE_SOURCE_DIR}/output/champions-of-norrath")
endif()
file(GLOB RECOMP_SOURCES CONFIGURE_DEPENDS "${RECOMP_DIR}/*.cpp")

# Build as a static library (avoids re-linking 9K objects every time)
add_library(recompiled_game STATIC ${RECOMP_SOURCES})
target_include_directories(recompiled_game PRIVATE
    ${CMAKE_SOURCE_DIR}/vendor/PS2Recomp/ps2xRuntime/include
    ${RECOMP_DIR}
)

# Unity build: batch files per TU to reduce compiler invocations
# PS2Recomp output is ideal for unity: no static vars, no anonymous namespaces
# GCC handles 50/batch fine; MSVC needs smaller batches (memory pressure)
if(MSVC)
    set(UNITY_BATCH 10)  # 9,395 -> 940 TUs (MSVC memory-hungry with generated code)
else()
    set(UNITY_BATCH 50)  # 9,395 -> 188 TUs
endif()
set_target_properties(recompiled_game PROPERTIES
    UNITY_BUILD ON
    UNITY_BUILD_BATCH_SIZE ${UNITY_BATCH}
)

# Suppress warnings in generated code
if(MSVC)
    target_compile_options(recompiled_game PRIVATE /W0 /Z7 /Od /bigobj)
else()
    target_compile_options(recompiled_game PRIVATE -w -O0)
endif()

# --- Halogen executable ---
add_executable(halogen
    vendor/PS2Recomp/ps2xRuntime/src/main.cpp
    src/register_functions_gen.cpp
    src/missing_stubs.cpp
    src/linker_stubs_gen.cpp
)
target_include_directories(halogen PRIVATE
    ${CMAKE_SOURCE_DIR}/vendor/PS2Recomp/ps2xRuntime/include
    ${RECOMP_DIR}
)
target_link_libraries(halogen PRIVATE
    recompiled_game
    ps2_runtime
    raylib
)

if(MSVC)
    target_compile_options(halogen PRIVATE /Z7)
endif()

# --- Halogen headless executable (no Raylib / no window) ---
# For crash-driven development: runs the dispatch loop on the main thread
# with function tracing, crash dumps, and call limits.
add_executable(halogen-headless
    src/main_headless.cpp
    src/raylib_stubs_headless.cpp
    src/register_functions_gen.cpp
    src/missing_stubs.cpp
    src/linker_stubs_gen.cpp
)
target_include_directories(halogen-headless PRIVATE
    ${CMAKE_SOURCE_DIR}/vendor/PS2Recomp/ps2xRuntime/include
    ${RECOMP_DIR}
)
# Link ps2_runtime (for dispatchLoop, loadELF, memory, etc.) and
# recompiled_game, but NOT raylib -- raylib_stubs_headless.cpp provides
# no-op stubs for the raylib symbols that ps2_runtime.a references.
target_link_libraries(halogen-headless PRIVATE
    recompiled_game
    ps2_runtime
)
if(MSVC)
    target_compile_options(halogen-headless PRIVATE /Z7)
endif()

# --- Halogen GUI executable (Vulkan window via SDL2 + parallel-gs) ---
# Task #3320: live paraLLEl-GS integration. Renders real GIF DMA to a Vulkan
# window instead of dumping to .gs files. M1: identical to headless (proves
# CMake wiring). M2+: swap main_headless.cpp for main_gui.cpp with SDL2 window
# + Vulkan swapchain + GSInterface init.
if(HALOGEN_HAVE_PARALLEL_GS)
    add_executable(halogen-gui
        src/main_gui.cpp
        src/raylib_stubs_headless.cpp
        src/register_functions_gen.cpp
        src/missing_stubs.cpp
        src/linker_stubs_gen.cpp
    )
    target_include_directories(halogen-gui PRIVATE
        ${CMAKE_SOURCE_DIR}/vendor/PS2Recomp/ps2xRuntime/include
        ${RECOMP_DIR}
        ${CMAKE_SOURCE_DIR}/vendor/parallel-gs/gs
        ${CMAKE_SOURCE_DIR}/vendor/parallel-gs/dump
        ${CMAKE_SOURCE_DIR}/vendor/parallel-gs/Granite/vulkan
        ${CMAKE_SOURCE_DIR}/vendor/parallel-gs/Granite/util
        ${CMAKE_SOURCE_DIR}/vendor/parallel-gs/Granite/math
        ${CMAKE_SOURCE_DIR}/vendor/parallel-gs/Granite/third_party/volk
        ${CMAKE_SOURCE_DIR}/vendor/parallel-gs/Granite/third_party/khronos/vulkan-headers/include
    )
    target_link_libraries(halogen-gui PRIVATE
        recompiled_game
        ps2_runtime
        parallel-gs
        parallel-gs-dump
        granite-vulkan
        granite-util
        granite-volk
        SDL2::SDL2
    )
    if(MSVC)
        target_compile_options(halogen-gui PRIVATE /Z7)
    endif()
endif()
