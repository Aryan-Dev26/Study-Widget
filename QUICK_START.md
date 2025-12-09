# Study Timer Pro - Quick Start Guide

## 🚀 Getting Started (Choose One Method)

### Method 1: Run Directly (Fastest)
```bash
pip install -r requirements.txt
python study_timer_pro.py
```

### Method 2: Create Desktop Shortcut
1. Double-click `create_desktop_shortcut.bat`
2. A shortcut will appear on your desktop
3. **Pin to Taskbar**: Right-click shortcut → Pin to taskbar
4. **Set Keyboard Shortcut**: 
   - Right-click shortcut → Properties
   - Click "Shortcut key" field
   - Press `Ctrl+Alt+S` (or your preferred combo)
   - Click OK
   - Now press `Ctrl+Alt+S` anywhere to launch!

### Method 3: Auto-Start with Windows
1. Double-click `add_to_startup.bat`
2. App will start automatically when Windows boots
3. Runs minimized in system tray

### Method 4: Build Standalone .exe
1. Double-click `build_exe.bat`
2. Wait for build to complete
3. Find `StudyTimerPro.exe` in `dist` folder
4. Copy it anywhere you want!

## 🎯 Using the App

### Basic Usage
1. **Start Timer**: Enter hours and click Start (or use presets)
2. **Minimize**: Click X to hide to system tray
3. **Show Again**: Double-click tray icon or use your keyboard shortcut

### System Tray
- **Right-click tray icon** for menu:
  - Show/Hide window
  - Start/Stop timer
  - Quit application

### Keyboard Shortcuts
- `Space` - Start/Pause timer
- `R` - Reset timer
- `Esc` - Show/Hide controls
- `Ctrl+Alt+S` - Launch app (if you set it up)

## 🎨 Customization

1. Click ⚙️ (settings icon)
2. Go to Settings tab
3. Choose:
   - **Theme**: 6 beautiful themes
   - **Timezone**: World clock
   - **Opacity**: Transparency level
   - **Sound**: Enable/disable alerts
   - **Notifications**: Windows toast notifications

## 📊 Features

### Presets Tab
- 🍅 Pomodoro (25 min)
- ☕ Short Break (5 min)
- 🌟 Long Break (15 min)
- 🎯 Deep Work (90 min)
- 📚 Quick Study (45 min)
- ⏰ Power Hour (60 min)
- 🚀 Sprint (30 min)

### Stats Tab
- Today's total study time
- Weekly total
- Monthly total
- Streak counter
- Level & XP
- Export to CSV

## 🔧 Troubleshooting

**App won't start?**
- Make sure Python is installed
- Run: `pip install -r requirements.txt`

**System tray not working?**
- Install: `pip install pystray pillow`

**Want to remove from startup?**
- Run: `remove_from_startup.bat`

**Can't see the widget?**
- It's small (200x70px) - check top-left of screen
- Click and drag to move it
- Adjust opacity in settings if too transparent

## 💡 Pro Tips

1. **Keep it visible**: Place in corner of screen for constant motivation
2. **Use presets**: Faster than typing hours each time
3. **Check stats**: Review your progress daily
4. **Set keyboard shortcut**: Summon instantly from anywhere
5. **Pin to taskbar**: One-click access
6. **Auto-start**: Never forget to track your study time

## 🎓 Study Techniques

### Pomodoro Technique
1. Study for 25 minutes
2. Take 5-minute break
3. Repeat 4 times
4. Take 15-minute long break

### Deep Work
- 90-minute focused sessions
- Best for complex tasks
- Take 20-minute breaks

### Time Blocking
- Set specific hours for studying
- Use timer to stay on track
- Review stats to improve

---

**Need help?** Open an issue on GitHub!
**Love it?** Star the repo! ⭐
