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

### Installation

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

### First Time Setup

1. Click the ⚙️ settings icon
2. Choose your preferred theme
3. Select your timezone
4. Adjust opacity to your liking
5. Start studying!

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
- `Space` - Start/Pause timer
- `R` - Reset timer
- `Esc` - Show/Hide controls

### View Statistics
1. Click ⚙️ settings icon
2. Go to "Stats" tab
3. View today/week/month totals
4. Check your streak and level
5. Export data with "📊 Export CSV"

## 🎨 Themes

Choose from 6 professionally designed themes:
- **Dark** - Classic dark mode (default)
- **Light** - Clean light theme
- **Blue** - Ocean-inspired
- **Green** - Nature-focused
- **Purple** - Creative vibes
- **Nord** - Popular Nordic palette

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
