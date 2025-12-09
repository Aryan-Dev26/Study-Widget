# Study Timer Pro 🎯

A professional study timer widget for Windows with advanced features for focused learning and productivity tracking.

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.7+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## ✨ Features

### Core Timer Features
- ⏱️ **Countdown Timer** - Set custom study durations
- 🕐 **Live World Clock** - View time in different timezones
- 🍅 **Pomodoro Technique** - Built-in 25/5/15 minute intervals
- ⚡ **Quick Presets** - 15min, 25min, 30min, 1h, 2h, 5h buttons
- ⏸️ **Pause/Resume** - Full control over your sessions

### Statistics & Tracking
- 📊 **Session History** - Track all your study sessions
- 📈 **Daily/Weekly/Monthly Stats** - See your progress over time
- 🔥 **Streak Counter** - Maintain your study streak
- ⭐ **Gamification** - Level up and earn XP for studying
- 📁 **Export to CSV** - Download your study data

### Customization
- 🎨 **6 Beautiful Themes** - Dark, Light, Blue, Green, Purple, Nord
- 🌍 **30+ Timezones** - Study with friends worldwide
- 🔊 **Sound Alerts** - Customizable alarm sounds
- 🔔 **Desktop Notifications** - Windows toast notifications
- 👁️ **Opacity Control** - Adjust transparency (50-100%)
- ⌨️ **Keyboard Shortcuts** - Space (start/pause), R (reset), Esc (hide)

### Professional Features
- 📝 **Task Tracking** - Label what you're studying
- 🎯 **Daily Goals** - Set and track study goals
- 💾 **Auto-Save** - All settings and stats saved automatically
- 🖱️ **Draggable Widget** - Position anywhere on screen
- 📌 **Always On Top** - Stays visible while you work
- 🎭 **Minimal UI** - Clean, distraction-free design

## 🚀 Quick Start

### Option 1: Run from Source

1. **Clone the repository:**
```bash
git clone https://github.com/Aryan-Dev26/Study-Widget.git
cd Study-Widget
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python study_timer_pro.py
```

### Option 2: Build Executable

1. **Build the .exe file:**
```bash
build_exe.bat
```

2. **The executable will be in the `dist` folder**

### Option 3: Quick Setup Scripts

**Create Desktop Shortcut:**
```bash
create_desktop_shortcut.bat
```
- Creates a shortcut on your desktop
- Pin to taskbar for quick access
- Set custom keyboard shortcut (e.g., Ctrl+Alt+S)

**Add to Windows Startup:**
```bash
add_to_startup.bat
```
- Automatically starts with Windows
- Runs minimized in system tray

**Remove from Startup:**
```bash
remove_from_startup.bat
```

### First Time Setup

1. Click the ⚙️ settings icon
2. Choose your preferred theme
3. Select your timezone
4. Adjust opacity to your liking
5. Start studying!

## 🎯 System Tray Features

- **Minimize to Tray** - Click X to hide to system tray
- **Right-click Tray Icon** for quick actions:
  - Show/Hide window
  - Start/Stop timer
  - Quit application
- **Double-click Tray Icon** to show window

## 📖 How to Use

### Basic Timer
1. Enter study duration in hours (e.g., 2.5 for 2.5 hours)
2. Optionally add a task name
3. Click "▶ Start"
4. Timer auto-minimizes to stay out of your way
5. Click ⚙️ to access controls anytime

### Pomodoro Mode
1. Go to "Presets" tab
2. Click "🍅 Start Pomodoro"
3. Work for 25 minutes
4. Take 5-minute breaks
5. Every 4th break is 15 minutes

### Keyboard Shortcuts

**Built-in Shortcuts:**
- `Space` - Start/Pause timer
- `R` - Reset timer
- `Esc` - Show/Hide controls

**Custom Global Shortcut (Windows):**
1. Create desktop shortcut using `create_desktop_shortcut.bat`
2. Right-click the shortcut → Properties
3. Click in "Shortcut key" field
4. Press your desired combo (e.g., `Ctrl+Alt+S`)
5. Click OK
6. Now press your combo anywhere to launch the app!

### View Statistics
1. Click ⚙️ settings icon
2. Go to "Stats" tab
3. View today/week/month totals
4. Check your streak and level
5. Export data with "📊 Export CSV"

## 🎨 Beautiful Themes

Choose from 6 stunning themes with instant switching (no restart needed):

- **🌙 Midnight Focus** - Deep purple-blue gradient for late-night study sessions (default)
- **🌅 Sunrise Energy** - Warm orange and cream tones for morning motivation
- **🌲 Forest Calm** - Soothing green shades for peaceful concentration
- **☕ Coffee Break** - Cozy amber and cream for comfortable studying
- **🌊 Ocean Depth** - Cool cyan and blue for deep focus
- **⚫ Minimal Dark** - Clean grayscale for distraction-free work

All themes feature:
- Glowing borders that pulse when timer is active
- Smooth color transitions
- Hover effects on preset buttons
- Instant theme switching without restart
- Optimized color contrast for readability
- Time breakdown display (hours, minutes, seconds)

## 🌍 Supported Timezones

View time in 30+ countries including:
- USA (EST, CST, MST, PST)
- Europe (London, Paris, Berlin, Moscow)
- Asia (India, China, Japan, Singapore)
- Australia, Brazil, Canada, and more!

## 🏆 Gamification System

- Earn **1 XP per minute** of study time
- Level up every **100 XP × current level**
- Maintain daily streaks for motivation
- Track your progress over time

## 📦 Building Executable

Create a standalone .exe file:

```bash
pyinstaller --onefile --windowed --icon=icon.ico study_timer_pro.py
```

The executable will be in the `dist/` folder.

## 🛠️ Technical Details

- **Language:** Python 3.7+
- **GUI Framework:** Tkinter (built-in)
- **Notifications:** win10toast
- **Data Storage:** JSON files
- **Platform:** Windows 10/11

## 📁 Project Structure

```
Study-Widget/
├── study_timer_pro.py    # Main application
├── config.py             # Configuration management
├── statistics.py         # Stats tracking
├── themes.py            # Theme definitions
├── timezones.py         # Timezone data
├── requirements.txt     # Dependencies
├── README.md           # Documentation
└── .gitignore         # Git ignore rules
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Inspired by the Pomodoro Technique
- Built for students and professionals worldwide
- Community feedback and suggestions

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Made with ❤️ for focused learners everywhere**
