# 📝 Study Timer Pro - Complete Setup Instructions

## ✅ Prerequisites

Before starting, make sure you have:
- Windows 10 or 11
- Python 3.7 or higher installed ([Download Python](https://www.python.org/downloads/))
- Internet connection (for installing packages)

---

## 🚀 Step-by-Step Setup

### Step 1: Download the Project

**Option A: Using Git**
```bash
git clone https://github.com/Aryan-Dev26/Study-Widget.git
cd Study-Widget
```

**Option B: Download ZIP**
1. Go to https://github.com/Aryan-Dev26/Study-Widget
2. Click green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP file to a folder (e.g., `C:\StudyTimer`)
5. Open Command Prompt in that folder

---

### Step 2: Install Required Packages

Open Command Prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

**Wait for installation to complete.** You should see:
- ✅ win10toast installed
- ✅ pystray installed
- ✅ Pillow installed
- ✅ pyinstaller installed

**If you get an error:**
- Try: `python -m pip install -r requirements.txt`
- Or: `py -m pip install -r requirements.txt`

---

### Step 3: Test the App

Run the app to make sure it works:

```bash
python study_timer_pro.py
```

**You should see:**
- A small timer widget appear (200x70 pixels)
- It shows "00:00:00" 
- A clock in the top-left
- Gear icon and X button

**If it works, great! Press X to close it and continue.**

---

### Step 4: Create Desktop Shortcut (Recommended)

**Double-click this file:**
```
create_desktop_shortcut.bat
```

**What happens:**
- A shortcut appears on your desktop called "Study Timer Pro"
- You can now double-click it to launch the app

**Test it:**
- Double-click the desktop shortcut
- App should open

---

### Step 5: Pin to Taskbar (Recommended)

1. Find the "Study Timer Pro" shortcut on your desktop
2. **Right-click** the shortcut
3. Click **"Pin to taskbar"**
4. Now you have a taskbar icon for one-click access!

---

### Step 6: Set Keyboard Shortcut (Optional but Awesome!)

This lets you press **Ctrl+Alt+S** anywhere to open the app instantly.

1. **Right-click** the desktop shortcut
2. Click **"Properties"**
3. Click in the **"Shortcut key"** field
4. Press **Ctrl + Alt + S** (or any combo you want)
5. Click **"OK"**

**Test it:**
- Press **Ctrl+Alt+S** anywhere
- App should appear instantly!

---

### Step 7: Add to Windows Startup (Optional)

Make the app start automatically when Windows boots.

**Double-click this file:**
```
add_to_startup.bat
```

**What happens:**
- App will start automatically when you log into Windows
- It starts minimized in the system tray
- You won't see it until you click the tray icon or use your keyboard shortcut

**To remove from startup later:**
```
remove_from_startup.bat
```

---

## 🎯 How to Use the App

### Basic Usage

1. **Launch the app** (desktop shortcut, taskbar, or Ctrl+Alt+S)
2. **Set study time:**
   - Click ⚙️ (gear icon)
   - Go to "Timer" tab
   - Enter hours (e.g., 2 for 2 hours)
   - Click "▶ Start"

3. **Use presets** (faster):
   - Click ⚙️ (gear icon)
   - Go to "⚡ Presets" tab
   - Click any preset (e.g., "🍅 Pomodoro" for 25 min)

4. **Minimize to tray:**
   - Click **X** button
   - App hides to system tray (bottom-right of screen)
   - Look for the timer icon near the clock

5. **Show again:**
   - **Double-click** the tray icon
   - Or press your keyboard shortcut (Ctrl+Alt+S)
   - Or **right-click** tray icon → "Show/Hide"

### System Tray Menu

**Right-click the tray icon** to see:
- **Show/Hide** - Toggle window visibility
- **Start Timer** - Quick start
- **Stop Timer** - Quick stop
- **Quit** - Actually close the app

### Keyboard Shortcuts (when app is focused)

- **Space** - Start/Pause timer
- **R** - Reset timer
- **Esc** - Show/Hide controls

---

## 🎨 Customization

1. Click **⚙️** (gear icon)
2. Go to **"⚙ Settings"** tab
3. Customize:

**Theme:**
- 🌙 Midnight Focus (purple gradient)
- 🌅 Sunrise Energy (orange gradient)
- 🌲 Forest Calm (green gradient)
- ☕ Coffee Break (amber gradient)
- 🌊 Ocean Depth (blue gradient)
- ⚫ Minimal Dark (gray gradient)

**Timezone:**
- Select your country/timezone
- Clock shows time in that timezone

**Opacity:**
- Drag slider to adjust transparency
- 50% = very transparent
- 100% = fully opaque

**Sound & Notifications:**
- ✅ Enable Sound - Beep when timer ends
- ✅ Show Notifications - Windows toast notifications

---

## 📊 Tracking Your Progress

1. Click **⚙️** (gear icon)
2. Go to **"📊 Stats"** tab
3. See:
   - Today's total study time
   - This week's total
   - This month's total
   - 🔥 Streak (consecutive days)
   - ⭐ Level & XP (gamification)

4. Click **"📊 Export CSV"** to download your data

---

## 🔧 Troubleshooting

### Problem: "Python is not recognized"
**Solution:** 
- Install Python from https://python.org/downloads/
- During installation, check "Add Python to PATH"

### Problem: "pip is not recognized"
**Solution:**
```bash
python -m ensurepip --upgrade
```

### Problem: Can't install packages
**Solution:**
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Problem: App won't start
**Solution:**
1. Open Command Prompt in project folder
2. Run: `python study_timer_pro.py`
3. Look for error messages
4. Install missing packages: `pip install [package-name]`

### Problem: System tray icon not showing
**Solution:**
- Install: `pip install pystray pillow`
- Restart the app

### Problem: Can't see the widget
**Solution:**
- It's small (200x70px)
- Check top-left corner of screen
- Click and drag to move it
- Increase opacity in settings

### Problem: Keyboard shortcut not working
**Solution:**
- Make sure you set it on the desktop shortcut (not the .py file)
- Try a different combo (e.g., Ctrl+Shift+S)
- Restart Windows

---

## 🎓 Study Tips

### Pomodoro Technique
1. Click ⚙️ → Presets → 🍅 Pomodoro (25 min)
2. Study focused for 25 minutes
3. Take 5-minute break
4. Repeat 4 times
5. Take 15-minute long break

### Deep Work Sessions
1. Click ⚙️ → Presets → 🎯 Deep Work (90 min)
2. No distractions for 90 minutes
3. Take 20-minute break
4. Best for complex tasks

### Time Blocking
1. Set specific hours for studying
2. Use timer to stay on track
3. Review stats daily to improve

---

## 📦 Building Standalone Executable (Advanced)

Want to share with friends who don't have Python?

**Double-click:**
```
build_exe.bat
```

**Wait 2-3 minutes for build to complete.**

**Find the .exe file:**
```
dist\StudyTimerPro.exe
```

**You can now:**
- Copy this .exe anywhere
- Run it without Python
- Share it with friends
- Put it on a USB drive

---

## ✅ Quick Checklist

After setup, you should have:

- [ ] App runs when you type `python study_timer_pro.py`
- [ ] Desktop shortcut created
- [ ] Taskbar icon pinned
- [ ] Keyboard shortcut set (Ctrl+Alt+S)
- [ ] (Optional) Added to Windows startup
- [ ] Tested: Timer starts and counts down
- [ ] Tested: Minimize to tray works
- [ ] Tested: Keyboard shortcut summons app
- [ ] Customized theme and settings

---

## 🆘 Need More Help?

1. **Check QUICK_START.md** for quick reference
2. **Check README.md** for full documentation
3. **Open an issue** on GitHub
4. **Check error messages** when running from Command Prompt

---

## 🎉 You're All Set!

Your Study Timer Pro is now ready to help you stay focused and productive!

**Quick reminder:**
- Press **Ctrl+Alt+S** to summon the timer
- Click **X** to minimize to tray
- Right-click tray icon for quick actions
- Check stats daily to track progress

**Happy studying! 📚✨**
