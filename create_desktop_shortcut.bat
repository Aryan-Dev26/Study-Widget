@echo off
echo Creating Desktop Shortcut for Study Timer Pro...
echo.

REM Get the current directory
set "CURRENT_DIR=%~dp0"

REM Desktop path
set "DESKTOP=%USERPROFILE%\Desktop"
set "SHORTCUT=%DESKTOP%\Study Timer Pro.lnk"

REM Check if executable exists
if exist "%CURRENT_DIR%dist\StudyTimerPro.exe" (
    set "TARGET=%CURRENT_DIR%dist\StudyTimerPro.exe"
    set "ICON=%CURRENT_DIR%icon.ico"
) else if exist "%CURRENT_DIR%study_timer_pro.py" (
    set "TARGET=pythonw.exe"
    set "ARGS=%CURRENT_DIR%study_timer_pro.py"
    set "ICON=%CURRENT_DIR%icon.ico"
) else (
    echo Error: Could not find StudyTimerPro.exe or study_timer_pro.py
    pause
    exit /b 1
)

REM Create shortcut using PowerShell
if defined ARGS (
    powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%SHORTCUT%'); $Shortcut.TargetPath = '%TARGET%'; $Shortcut.Arguments = '%ARGS%'; $Shortcut.WorkingDirectory = '%CURRENT_DIR%'; $Shortcut.IconLocation = '%ICON%'; $Shortcut.Save()"
) else (
    powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%SHORTCUT%'); $Shortcut.TargetPath = '%TARGET%'; $Shortcut.WorkingDirectory = '%CURRENT_DIR%'; $Shortcut.IconLocation = '%ICON%'; $Shortcut.Save()"
)

if exist "%SHORTCUT%" (
    echo.
    echo Success! Desktop shortcut created.
    echo.
    echo You can now:
    echo 1. Double-click the shortcut to launch
    echo 2. Right-click the shortcut and pin to taskbar
    echo 3. Right-click the shortcut, Properties, and set a keyboard shortcut
    echo.
    echo To set a keyboard shortcut:
    echo - Right-click the shortcut
    echo - Select Properties
    echo - Click in "Shortcut key" field
    echo - Press your desired key combo (e.g., Ctrl+Alt+S)
    echo - Click OK
) else (
    echo.
    echo Error: Failed to create desktop shortcut.
)

echo.
pause
