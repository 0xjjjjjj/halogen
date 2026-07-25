TOOLCHAIN := /tmp/llvm-mingw-toolchain.cmake
BUILD_DIR := build-mingw
SDL2_DIR  := /tmp/SDL2-2.32.10/x86_64-w64-mingw32
DEPLOY_TO ?= /mnt/c/halogen-run
LLVM_MINGW := /tmp/llvm-mingw-20250910-ucrt-ubuntu-22.04-x86_64

.PHONY: win-configure win-build win-package win-deploy win-run win-all clean-win

win-configure:
	cmake -B $(BUILD_DIR) -G Ninja \
		-DCMAKE_TOOLCHAIN_FILE=$(TOOLCHAIN) \
		-DCMAKE_BUILD_TYPE=Release \
		-DSDL2_DIR=$(SDL2_DIR)/lib/cmake/SDL2 \
		-DCMAKE_PREFIX_PATH=$(SDL2_DIR) \
		-DSDL2_NO_MWINDOWS=1

win-build:
	cmake --build $(BUILD_DIR) -j$$(nproc) --target halogen-gui

win-package:
	@mkdir -p $(BUILD_DIR)/dist
	cp $(BUILD_DIR)/halogen-gui.exe $(BUILD_DIR)/dist/
	cp $(LLVM_MINGW)/x86_64-w64-mingw32/bin/libc++.dll $(BUILD_DIR)/dist/
	cp $(LLVM_MINGW)/x86_64-w64-mingw32/bin/libunwind.dll $(BUILD_DIR)/dist/
	cp $(SDL2_DIR)/bin/SDL2.dll $(BUILD_DIR)/dist/
	cp $(BUILD_DIR)/ThirdParty/ffmpeg-prefix/src/ffmpeg_external/bin/*.dll $(BUILD_DIR)/dist/
	@echo "packaged: $$(ls $(BUILD_DIR)/dist/ | wc -l) files, $$(du -sh $(BUILD_DIR)/dist/ | cut -f1)"

win-deploy: win-package
	@mkdir -p $(DEPLOY_TO)
	rsync -a --delete $(BUILD_DIR)/dist/ $(DEPLOY_TO)/
	@[ -f bin/SLUS_205.65 ] && rsync -a bin/SLUS_205.65 $(DEPLOY_TO)/bin/ && mkdir -p $(DEPLOY_TO)/bin || true
	@echo "deployed to $(DEPLOY_TO) — run: $(DEPLOY_TO)\\halogen-gui.exe"

CD_ROOT ?= \\\\wsl.localhost\\Ubuntu\\home\\j\\git\\halogen\\bin\\disc
ELF     ?= \\\\wsl.localhost\\Ubuntu\\home\\j\\git\\halogen\\bin\\SLUS_205.65
TIMEOUT ?= 30

win-run:
	/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe -Command '$$exe="C:\halogen-run\halogen-gui.exe"; $$p=Start-Process $$exe -ArgumentList @("--cd-root","$(CD_ROOT)","$(ELF)") -WorkingDirectory (Split-Path $$exe) -RedirectStandardOutput C:\halogen-run\stdout.log -RedirectStandardError C:\halogen-run\stderr.log -PassThru; Start-Sleep -Seconds $(TIMEOUT); if(!$$p.HasExited){Stop-Process -Id $$p.Id -Force}; Write-Host "---stderr---"; Get-Content C:\halogen-run\stderr.log | Select-Object -Last 30'

win-all: win-configure win-build win-deploy

clean-win:
	rm -rf $(BUILD_DIR)
