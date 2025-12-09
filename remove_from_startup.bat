@echo off
echo Removing Study Timer Pro from Windows Startup...
echo.

set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
set "SHORTCUT=%STARTUP_FOLDER%\StudyTimerPro.lnk"

if exist "%SHORTCUT%" (
    del "%SHORTCUT%"
    echo Success! Study Timer Pro removed from startup.
) else (
    echo Study Timer Pro is not in startup folder.
)

echo.
pause
