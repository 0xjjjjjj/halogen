// Raylib function stubs for the headless build target.
//
// ps2_runtime.a has raylib calls compiled into ps2_runtime.cpp (InitWindow,
// CloseWindow, GenImageColor, etc.) in the initialize(), run(), and
// ~PS2Runtime() methods. The headless binary never calls those code paths,
// but the linker still needs the symbols resolved.
//
// These are no-op stubs. None of them are ever actually called at runtime
// in the headless configuration -- if one IS called, it means a code path
// that assumes a window is being taken, which is a bug.

#include <cstdio>
#include <cstdlib>

// Replicate the minimal raylib types the symbols reference.
// These must match raylib.h's layout exactly.
struct Color { unsigned char r, g, b, a; };
struct Image { void* data; int width; int height; int mipmaps; int format; };
struct Texture { unsigned int id; int width; int height; int mipmaps; int format; };
typedef Texture Texture2D;

// Trap: if any of these stubs are actually called, something is wrong.
static void headless_trap(const char* func)
{
    fprintf(stderr, "[headless] BUG: raylib stub '%s' was called -- "
                    "this code path should not be reached in headless mode\n", func);
}

extern "C" {

void InitWindow(int, int, const char*)          { headless_trap("InitWindow"); }
void CloseWindow(void)                          { /* called from ~PS2Runtime, harmless */ }
bool WindowShouldClose(void)                    { return true; }
bool IsWindowReady(void)                        { return false; }  // ~PS2Runtime checks this
void SetConfigFlags(unsigned int)               { headless_trap("SetConfigFlags"); }
void SetTargetFPS(int)                          { headless_trap("SetTargetFPS"); }

void BeginDrawing(void)                         { headless_trap("BeginDrawing"); }
void EndDrawing(void)                           { headless_trap("EndDrawing"); }
void ClearBackground(Color)                     { headless_trap("ClearBackground"); }

Image GenImageColor(int w, int h, Color)
{
    headless_trap("GenImageColor");
    return Image{nullptr, w, h, 1, 0};
}

Texture2D LoadTextureFromImage(Image)
{
    headless_trap("LoadTextureFromImage");
    return Texture2D{0, 0, 0, 1, 0};
}

void UnloadImage(Image)                         { headless_trap("UnloadImage"); }
void UnloadTexture(Texture2D)                   { headless_trap("UnloadTexture"); }
void UpdateTexture(Texture2D, const void*)      { headless_trap("UpdateTexture"); }
void DrawTexture(Texture2D, int, int, Color)    { headless_trap("DrawTexture"); }

} // extern "C"
