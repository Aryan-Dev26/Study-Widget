@echo off
echo Adding Study Timer Pro to Windows Startup...
echo.

REM Get the current directory
set "CURRENT_DIR=%~dp0"

REM Create icon if it doesn't exist
if not exist "%CURRENT_DIR%icon.ico" (
    echo Creating icon...
    python "%CURRENT_DIR%create_icon.py"
)

REM Create a shortcut in the Startup folder
set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
set "SHORTCUT=%STARTUP_FOLDER%\StudyTimerPro.lnk"

REM Check if executable exists
if exist "%CURRENT_DIR%dist\StudyTimerPro.exe" (
    set "TARGET=%CURRENT_DIR%dist\StudyTimerPro.exe"
    
    REM Create shortcut
    powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%SHORTCUT%'); $Shortcut.TargetPath = '%TARGET%'; $Shortcut.WorkingDirectory = '%CURRENT_DIR%'; $Shortcut.Save()"
    
) else if exist "%CURRENT_DIR%study_timer_pro.py" (
    REM Find Python executable
    where pythonw.exe >nul 2>&1
    if %errorlevel% equ 0 (
        set "PYTHON_EXE=pythonw.exe"
    ) else (
        where python.exe >nul 2>&1
        if %errorlevel% equ 0 (
            set "PYTHON_EXE=python.exe"
        ) else (
            echo Error: Python not found in PATH
            pause
            exit /b 1
        )
    )
    
    set "ARGS=%CURRENT_DIR%study_timer_pro.py"
    
    REM Create shortcut
    powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%SHORTCUT%'); $Shortcut.TargetPath = '%PYTHON_EXE%'; $Shortcut.Arguments = '%ARGS%'; $Shortcut.WorkingDirectory = '%CURRENT_DIR%'; $Shortcut.Save()"
) else (
    echo Error: Could not find StudyTimerPro.exe or study_timer_pro.py
    pause
    exit /b 1
)

if exist "%SHORTCUT%" (
    echo.
    echo ✅ Success! Study Timer Pro will now start automatically when Windows starts.
    echo.
    echo The app will start minimized in the system tray.
    echo.
    echo Shortcut created at: %SHORTCUT%
    echo.
    echo To remove from startup later, run: remove_from_startup.bat
) else (
    echo.
    echo ❌ Error: Failed to create startup shortcut.
    echo.
    echo Try running as Administrator.
)

echo.
pause
