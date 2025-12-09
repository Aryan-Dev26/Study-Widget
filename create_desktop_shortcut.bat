@echo off
echo Creating Desktop Shortcut for Study Timer Pro...
echo.

REM Run PowerShell script
powershell -ExecutionPolicy Bypass -File "%~dp0create_desktop_shortcut.ps1"
exit /b

REM Get the current directory
set "CURRENT_DIR=%~dp0"

REM Create icon if it doesn't exist
if not exist "%CURRENT_DIR%icon.ico" (
    echo Creating icon...
    python "%CURRENT_DIR%create_icon.py"
    if not exist "%CURRENT_DIR%icon.ico" (
        echo Warning: Could not create icon, shortcut will use default icon
    )
)

REM Get Desktop path (handles OneDrive Desktop)
for /f "usebackq tokens=3*" %%A in (`reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" /v Desktop 2^>nul`) do set "DESKTOP=%%A %%B"
if "%DESKTOP%"=="" set "DESKTOP=%USERPROFILE%\Desktop"
REM Expand environment variables
call set "DESKTOP=%DESKTOP%"
set "SHORTCUT=%DESKTOP%\StudyTimerPro.lnk"

REM Check if executable exists
if exist "%CURRENT_DIR%dist\StudyTimerPro.exe" (
    set "TARGET=%CURRENT_DIR%dist\StudyTimerPro.exe"
    if exist "%CURRENT_DIR%icon.ico" (
        set "ICON=%CURRENT_DIR%icon.ico"
    ) else (
        set "ICON=%CURRENT_DIR%dist\StudyTimerPro.exe,0"
    )
    
    REM Create shortcut using VBScript
    cscript //nologo "%CURRENT_DIR%create_shortcut.vbs" "%SHORTCUT%" "%TARGET%" "%CURRENT_DIR%" "%ICON%"
    
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
    
    REM Create shortcut using VBScript
    if exist "%CURRENT_DIR%icon.ico" (
        cscript //nologo "%CURRENT_DIR%create_shortcut.vbs" "%SHORTCUT%" "%PYTHON_EXE%" "%CURRENT_DIR%" "%CURRENT_DIR%icon.ico" "%ARGS%"
    ) else (
        cscript //nologo "%CURRENT_DIR%create_shortcut.vbs" "%SHORTCUT%" "%PYTHON_EXE%" "%CURRENT_DIR%" "" "%ARGS%"
    )
) else (
    echo Error: Could not find StudyTimerPro.exe or study_timer_pro.py
    pause
    exit /b 1
)

if exist "%SHORTCUT%" (
    echo.
    echo ✅ Success! Desktop shortcut created.
    echo.
    echo 📋 Next Steps:
    echo.
    echo 1. 🖱️  Double-click the shortcut to launch
    echo 2. 📌 Right-click the shortcut and "Pin to taskbar"
    echo 3. ⌨️  Set a keyboard shortcut:
    echo    - Right-click the shortcut
    echo    - Select "Properties"
    echo    - Click in "Shortcut key" field
    echo    - Press Ctrl+Alt+S (or your preferred combo)
    echo    - Click OK
    echo.
    echo Now you can press Ctrl+Alt+S anywhere to open the app!
) else (
    echo.
    echo ❌ Error: Failed to create desktop shortcut.
    echo.
    echo Try running as Administrator or check if Desktop folder exists.
)

echo.
pause
