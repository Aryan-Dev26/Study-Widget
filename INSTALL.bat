@echo off
color 0A
title Study Timer Pro - Easy Installer

echo.
echo ╔══════════════════════════════════════════════════════════════════╗
echo ║                                                                  ║
echo ║              📚 STUDY TIMER PRO - EASY INSTALLER 📚              ║
echo ║                                                                  ║
echo ╚══════════════════════════════════════════════════════════════════╝
echo.
echo This will set up everything for you automatically!
echo.
pause

echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo 📦 STEP 1/5: Installing Python packages...
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo ❌ Error installing packages. Please check if Python is installed.
    pause
    exit /b 1
)
echo.
echo ✅ Packages installed successfully!
timeout /t 2 >nul

echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo 🎨 STEP 2/5: Creating app icon...
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
python create_icon.py
echo.
echo ✅ Icon created!
timeout /t 2 >nul

echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo 🖱️ STEP 3/5: Creating desktop shortcut...
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
call create_desktop_shortcut.bat
timeout /t 2 >nul

echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo 🧪 STEP 4/5: Testing the app...
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
echo The app will open for 5 seconds to test...
echo.
start /B pythonw study_timer_pro.py
timeout /t 5 >nul
taskkill /F /IM pythonw.exe >nul 2>&1
echo.
echo ✅ Test complete!
timeout /t 2 >nul

echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo 🎉 STEP 5/5: Installation Complete!
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
echo ✅ Python packages installed
echo ✅ App icon created
echo ✅ Desktop shortcut created
echo ✅ App tested successfully
echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo 📋 NEXT STEPS:
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
echo 1. Find "Study Timer Pro" shortcut on your desktop
echo 2. Right-click it and select "Pin to taskbar"
echo 3. (Optional) Set keyboard shortcut:
echo    - Right-click shortcut ^> Properties
echo    - Click "Shortcut key" field
echo    - Press Ctrl+Alt+S
echo    - Click OK
echo.
echo 4. (Optional) Add to Windows startup:
echo    - Run: add_to_startup.bat
echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo 🚀 READY TO USE!
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
echo Double-click the desktop shortcut to start!
echo.
pause
