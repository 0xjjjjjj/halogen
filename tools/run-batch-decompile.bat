@echo off
REM Batch decompile all Champions of Norrath functions via Ghidra headless mode.
REM
REM BEFORE RUNNING:
REM   1. Close Ghidra GUI (project lock conflict)
REM   2. Edit paths below to match your system
REM   3. Ensure engine-map.json path in ghidra-batch-decompile.py is correct

REM ==== EDIT THESE ====
set GHIDRA_DIR=C:\ghidra\ghidra_11.4.2_PUBLIC
set PROJ_DIR=C:\Users\j\Documents\ghidra_projects
set PROJ_NAME=ChampionsOfNorrath
set SCRIPT_DIR=%~dp0
set LOG_FILE=%~dp0decompile.log
REM ====================

echo.
echo === Ghidra Batch Decompilation ===
echo Ghidra:    %GHIDRA_DIR%
echo Project:   %PROJ_DIR%\%PROJ_NAME%
echo Script:    %SCRIPT_DIR%ghidra-batch-decompile.py
echo Log:       %LOG_FILE%
echo.
echo Close Ghidra GUI before continuing!
echo.
pause

"%GHIDRA_DIR%\support\analyzeHeadless.bat" ^
  "%PROJ_DIR%" %PROJ_NAME% ^
  -process "*" ^
  -noanalysis ^
  -postScript ghidra-batch-decompile.py ^
  -scriptPath "%SCRIPT_DIR%" ^
  -scriptlog "%LOG_FILE%"

echo.
echo === Done! Check %LOG_FILE% for results ===
pause
