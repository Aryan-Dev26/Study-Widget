@echo off
echo Building Study Timer Pro...
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create icon if it doesn't exist
if not exist icon.ico (
    echo Creating icon...
    python create_icon.py
)

REM Build executable
echo Building executable...
pyinstaller --onefile --windowed --icon=icon.ico --name="StudyTimerPro" study_timer_pro.py

echo.
echo Build complete! Executable is in the dist folder.
echo.
pause
