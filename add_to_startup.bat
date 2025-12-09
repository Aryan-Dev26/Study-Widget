@echo off
echo Adding Study Timer Pro to Windows Startup...
echo.

REM Get the current directory
set "CURRENT_DIR=%~dp0"

REM Create a shortcut in the Startup folder
set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
set "SHORTCUT=%STARTUP_FOLDER%\StudyTimerPro.lnk"

REM Check if executable exists
if exist "%CURRENT_DIR%dist\StudyTimerPro.exe" (
    set "TARGET=%CURRENT_DIR%dist\StudyTimerPro.exe"
) else if exist "%CURRENT_DIR%study_timer_pro.py" (
    set "TARGET=%CURRENT_DIR%study_timer_pro.py"
) else (
    echo Error: Could not find StudyTimerPro.exe or study_timer_pro.py
    pause
    exit /b 1
)

REM Create shortcut using PowerShell
powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%SHORTCUT%'); $Shortcut.TargetPath = '%TARGET%'; $Shortcut.WorkingDirectory = '%CURRENT_DIR%'; $Shortcut.Save()"

if exist "%SHORTCUT%" (
    echo.
    echo Success! Study Timer Pro will now start automatically when Windows starts.
    echo.
    echo Shortcut created at: %SHORTCUT%
) else (
    echo.
    echo Error: Failed to create startup shortcut.
)

echo.
pause
