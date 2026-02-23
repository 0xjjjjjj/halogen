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

# --- Recompiled game code ---
# All 9,395 PS2Recomp-generated .cpp files
file(GLOB RECOMP_SOURCES CONFIGURE_DEPENDS
    "${CMAKE_SOURCE_DIR}/output/champions-of-norrath/*.cpp"
)

# Build as a static library (avoids re-linking 9K objects every time)
add_library(recompiled_game STATIC ${RECOMP_SOURCES})
target_include_directories(recompiled_game PRIVATE
    ${CMAKE_SOURCE_DIR}/vendor/PS2Recomp/ps2xRuntime/include
    ${CMAKE_SOURCE_DIR}/output/champions-of-norrath
)
# Suppress warnings in generated code
target_compile_options(recompiled_game PRIVATE -w)

# --- Halogen executable ---
add_executable(halogen
    vendor/PS2Recomp/ps2xRuntime/src/main.cpp
    src/register_functions_gen.cpp
    src/missing_stubs.cpp
    src/linker_stubs_gen.cpp
)
target_include_directories(halogen PRIVATE
    ${CMAKE_SOURCE_DIR}/vendor/PS2Recomp/ps2xRuntime/include
    ${CMAKE_SOURCE_DIR}/output/champions-of-norrath
)
target_link_libraries(halogen PRIVATE
    recompiled_game
    ps2_runtime
    raylib
)
