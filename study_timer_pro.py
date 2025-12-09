import tkinter as tk
from tkinter import ttk, messagebox
import time
from datetime import datetime, timedelta
import winsound
import threading
from config import Config
from statistics import Statistics
from themes import get_theme
from timezones import get_time_for_timezone, get_timezone_list

class StudyTimerPro:
    def __init__(self, root):
        self.root = root
        self.config = Config()
        self.stats = Statistics()
        
        # Load saved position
        pos = self.config.get("position")
        self.root.geometry(f"320x110+{pos['x']}+{pos['y']}")
        self.root.title("")
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)
        self.root.attributes('-alpha', self.config.get("opacity"))
        
        # Apply theme
        self.theme = get_theme(self.config.get("theme"))
        self.root.configure(bg=self.theme["bg"])
        
        # Timer state
        self.study_seconds = 0
        self.running = False
        self.start_time = None
        self.minimized = True
        self.pomodoro_mode = False
        self.is_break = False
        self.pomodoro_count = 0
        self.pulse_state = 0
        
        # Store all widgets for theme updates
        self.all_widgets = []
        
        # Gamification
        self.update_streak()
        
        self.setup_ui()
        self.setup_keyboard_shortcuts()
        self.update_display()
        self.pulse_animation()
        
    def setup_ui(self):
        # Main frame with border glow effect
        self.main_frame = tk.Frame(self.root, bg=self.theme["bg"], 
                                   highlightthickness=2, highlightbackground=self.theme["glow"])
        self.main_frame.pack(fill="both", expand=True, padx=2, pady=2)
        
        # Title bar
        self.title_bar = tk.Frame(self.main_frame, bg=self.theme["bg"], cursor="fleur")
        self.title_bar.pack(fill="x")
        self.title_bar.bind("<Button-1>", self.start_drag)
        self.title_bar.bind("<B1-Motion>", self.on_drag)
        
        # Top row: Clock and controls
        top_row = tk.Frame(self.title_bar, bg=self.theme["bg"])
        top_row.pack(fill="x", padx=10, pady=5)
        
        # Clock display with icon
        self.clock_label = tk.Label(top_row, text="", 
                                    font=("Consolas", 9),
                                    bg=self.theme["bg"], fg=self.theme["accent"])
        self.clock_label.pack(side="left")
        self.clock_label.bind("<Button-1>", self.start_drag)
        self.clock_label.bind("<B1-Motion>", self.on_drag)
        
        # Control buttons
        btn_frame = tk.Frame(top_row, bg=self.theme["bg"])
        btn_frame.pack(side="right")
        
        self.settings_btn = tk.Label(btn_frame, text="⚙", font=("Segoe UI", 11),
                                     bg=self.theme["bg"], fg=self.theme["glow"], cursor="hand2")
        self.settings_btn.pack(side="left", padx=4)
        self.settings_btn.bind("<Button-1>", self.toggle_controls)
        self.settings_btn.bind("<Enter>", lambda e: self.settings_btn.config(fg=self.theme["accent"]))
        self.settings_btn.bind("<Leave>", lambda e: self.settings_btn.config(fg=self.theme["glow"]))
        
        self.close_btn = tk.Label(btn_frame, text="✕", font=("Segoe UI", 11),
                                  bg=self.theme["bg"], fg=self.theme["glow"], cursor="hand2")
        self.close_btn.pack(side="left", padx=4)
        self.close_btn.bind("<Button-1>", self.on_close)
        self.close_btn.bind("<Enter>", lambda e: self.close_btn.config(fg=self.theme["danger"]))
        self.close_btn.bind("<Leave>", lambda e: self.close_btn.config(fg=self.theme["glow"]))
        
        # Timer display (large, centered)
        timer_container = tk.Frame(self.title_bar, bg=self.theme["bg"])
        timer_container.pack(fill="x", padx=10, pady=5)
        
        self.timer_label = tk.Label(timer_container, text="00:00:00",
                                    font=("Consolas", 32, "bold"),
                                    bg=self.theme["bg"], fg=self.theme["glow"])
        self.timer_label.pack()
        self.timer_label.bind("<Button-1>", self.start_drag)
        self.timer_label.bind("<B1-Motion>", self.on_drag)
        
        # Stats bar at bottom
        stats_bar = tk.Frame(self.title_bar, bg=self.theme["secondary"], height=2)
        stats_bar.pack(fill="x", padx=10, pady=2)
        
        self.stats_label = tk.Label(self.title_bar, text="",
                                    font=("Consolas", 8),
                                    bg=self.theme["bg"], fg=self.theme["accent"])
        self.stats_label.pack(pady=2)
        self.update_stats_display()
        
        # Controls frame
        self.controls_frame = tk.Frame(self.main_frame, bg=self.theme["bg"])
        self.setup_controls()
        
    def setup_controls(self):
        # Notebook for tabs
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.update_notebook_style()
        
        self.notebook = ttk.Notebook(self.controls_frame)
        self.notebook.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Timer Tab
        self.timer_tab = tk.Frame(self.notebook, bg=self.theme["bg"])
        self.notebook.add(self.timer_tab, text="⏱ Timer")
        self.setup_timer_tab()
        
        # Presets Tab
        self.presets_tab = tk.Frame(self.notebook, bg=self.theme["bg"])
        self.notebook.add(self.presets_tab, text="⚡ Presets")
        self.setup_presets_tab()
        
        # Stats Tab
        self.stats_tab = tk.Frame(self.notebook, bg=self.theme["bg"])
        self.notebook.add(self.stats_tab, text="📊 Stats")
        self.setup_stats_tab()
        
        # Settings Tab
        self.settings_tab = tk.Frame(self.notebook, bg=self.theme["bg"])
        self.notebook.add(self.settings_tab, text="⚙ Settings")
        self.setup_settings_tab()
    
    def update_notebook_style(self):
        self.style.configure('TNotebook', background=self.theme["bg"], borderwidth=0)
        self.style.configure('TNotebook.Tab', background=self.theme["secondary"],
                       foreground=self.theme["fg"], padding=[10, 5], borderwidth=0)
        self.style.map('TNotebook.Tab', 
                      background=[('selected', self.theme["accent"])],
                      foreground=[('selected', self.theme["bg"])])

    def setup_timer_tab(self):
        # Task entry
        tk.Label(self.timer_tab, text="Task:", bg=self.theme["bg"],
                fg=self.theme["fg"], font=("Segoe UI", 9)).pack(pady=5)
        self.task_entry = tk.Entry(self.timer_tab, bg=self.theme["secondary"],
                                   fg=self.theme["fg"], relief="flat", font=("Segoe UI", 9))
        self.task_entry.pack(fill="x", padx=10)
        self.task_entry.insert(0, self.config.get("last_task"))
        
        # Duration input
        duration_frame = tk.Frame(self.timer_tab, bg=self.theme["bg"])
        duration_frame.pack(pady=10)
        
        tk.Label(duration_frame, text="Hours:", bg=self.theme["bg"],
                fg=self.theme["fg"], font=("Segoe UI", 9)).pack(side="left", padx=5)
        self.hours_entry = tk.Entry(duration_frame, width=6, bg=self.theme["secondary"],
                                    fg=self.theme["fg"], relief="flat", font=("Segoe UI", 9))
        self.hours_entry.pack(side="left")
        self.hours_entry.insert(0, "1")
        
        # Control buttons
        btn_frame = tk.Frame(self.timer_tab, bg=self.theme["bg"])
        btn_frame.pack(pady=10)
        
        self.start_btn = tk.Button(btn_frame, text="▶ Start", command=self.start_timer,
                                   bg=self.theme["success"], fg="white", relief="flat",
                                   font=("Segoe UI", 10), cursor="hand2", width=8)
        self.start_btn.pack(side="left", padx=3)
        
        self.stop_btn = tk.Button(btn_frame, text="⏸ Pause", command=self.stop_timer,
                                  bg=self.theme["warning"], fg="white", relief="flat",
                                  font=("Segoe UI", 10), cursor="hand2", width=8, state="disabled")
        self.stop_btn.pack(side="left", padx=3)
        
        self.reset_btn = tk.Button(btn_frame, text="↻ Reset", command=self.reset_timer,
                                   bg=self.theme["secondary"], fg=self.theme["fg"], relief="flat",
                                   font=("Segoe UI", 10), cursor="hand2", width=8)
        self.reset_btn.pack(side="left", padx=3)
    
    def setup_presets_tab(self):
        tk.Label(self.presets_tab, text="Quick Start", bg=self.theme["bg"],
                fg=self.theme["fg"], font=("Segoe UI", 10, "bold")).pack(pady=10)
        
        presets = [
            ("15 min", 0.25),
            ("25 min (Pomodoro)", 25/60),
            ("30 min", 0.5),
            ("1 hour", 1),
            ("2 hours", 2),
            ("5 hours", 5)
        ]
        
        for text, hours in presets:
            btn = tk.Button(self.presets_tab, text=text,
                          command=lambda h=hours: self.quick_start(h),
                          bg=self.theme["accent"], fg="white", relief="flat",
                          font=("Segoe UI", 9), cursor="hand2", width=20)
            btn.pack(pady=3)
        
        # Pomodoro section
        tk.Label(self.presets_tab, text="Pomodoro Mode", bg=self.theme["bg"],
                fg=self.theme["fg"], font=("Segoe UI", 10, "bold")).pack(pady=10)
        
        pomo_btn = tk.Button(self.presets_tab, text="🍅 Start Pomodoro",
                            command=self.start_pomodoro,
                            bg=self.theme["danger"], fg="white", relief="flat",
                            font=("Segoe UI", 9), cursor="hand2", width=20)
        pomo_btn.pack(pady=5)
    
    def setup_stats_tab(self):
        stats_frame = tk.Frame(self.stats_tab, bg=self.theme["bg"])
        stats_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Today
        today_total = self.stats.get_today_total()
        tk.Label(stats_frame, text=f"Today: {self.format_time(today_total)}",
                bg=self.theme["bg"], fg=self.theme["fg"],
                font=("Segoe UI", 10)).pack(anchor="w", pady=3)
        
        # Week
        week_total = self.stats.get_week_total()
        tk.Label(stats_frame, text=f"This Week: {self.format_time(week_total)}",
                bg=self.theme["bg"], fg=self.theme["fg"],
                font=("Segoe UI", 10)).pack(anchor="w", pady=3)
        
        # Month
        month_total = self.stats.get_month_total()
        tk.Label(stats_frame, text=f"This Month: {self.format_time(month_total)}",
                bg=self.theme["bg"], fg=self.theme["fg"],
                font=("Segoe UI", 10)).pack(anchor="w", pady=3)
        
        # Streak
        streak = self.config.get("streak")
        tk.Label(stats_frame, text=f"🔥 Streak: {streak} days",
                bg=self.theme["bg"], fg=self.theme["accent"],
                font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=3)
        
        # Level
        level = self.config.get("level")
        xp = self.config.get("xp")
        tk.Label(stats_frame, text=f"⭐ Level {level} (XP: {xp})",
                bg=self.theme["bg"], fg=self.theme["accent"],
                font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=3)
        
        # Export button
        export_btn = tk.Button(stats_frame, text="📊 Export CSV",
                              command=self.export_stats,
                              bg=self.theme["accent"], fg="white", relief="flat",
                              font=("Segoe UI", 9), cursor="hand2")
        export_btn.pack(pady=10)
    
    def setup_settings_tab(self):
        settings_frame = tk.Frame(self.settings_tab, bg=self.theme["bg"])
        settings_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Theme selection
        tk.Label(settings_frame, text="Theme:", bg=self.theme["bg"],
                fg=self.theme["fg"], font=("Segoe UI", 9)).grid(row=0, column=0, sticky="w", pady=5)
        
        self.theme_var = tk.StringVar(value=self.config.get("theme"))
        theme_combo = ttk.Combobox(settings_frame, textvariable=self.theme_var,
                                   values=["cyberpunk", "neon", "matrix", "synthwave", "dark", "arctic"],
                                   state="readonly", width=15)
        theme_combo.grid(row=0, column=1, pady=5)
        theme_combo.bind("<<ComboboxSelected>>", self.change_theme)
        
        # Timezone selection
        tk.Label(settings_frame, text="Timezone:", bg=self.theme["bg"],
                fg=self.theme["fg"], font=("Segoe UI", 9)).grid(row=1, column=0, sticky="w", pady=5)
        
        self.tz_var = tk.StringVar(value=self.config.get("timezone"))
        tz_combo = ttk.Combobox(settings_frame, textvariable=self.tz_var,
                               values=get_timezone_list(), state="readonly", width=15)
        tz_combo.grid(row=1, column=1, pady=5)
        tz_combo.bind("<<ComboboxSelected>>", self.change_timezone)
        
        # Opacity slider
        tk.Label(settings_frame, text="Opacity:", bg=self.theme["bg"],
                fg=self.theme["fg"], font=("Segoe UI", 9)).grid(row=2, column=0, sticky="w", pady=5)
        
        opacity_slider = tk.Scale(settings_frame, from_=0.5, to=1.0, resolution=0.1,
                                 orient="horizontal", bg=self.theme["bg"],
                                 fg=self.theme["fg"], command=self.change_opacity)
        opacity_slider.set(self.config.get("opacity"))
        opacity_slider.grid(row=2, column=1, pady=5)
        
        # Sound toggle
        self.sound_var = tk.BooleanVar(value=self.config.get("sound_enabled"))
        sound_check = tk.Checkbutton(settings_frame, text="Enable Sound",
                                    variable=self.sound_var, bg=self.theme["bg"],
                                    fg=self.theme["fg"], selectcolor=self.theme["secondary"],
                                    command=self.toggle_sound)
        sound_check.grid(row=3, column=0, columnspan=2, sticky="w", pady=5)
        
        # Notifications toggle
        self.notif_var = tk.BooleanVar(value=self.config.get("show_notifications"))
        notif_check = tk.Checkbutton(settings_frame, text="Show Notifications",
                                     variable=self.notif_var, bg=self.theme["bg"],
                                     fg=self.theme["fg"], selectcolor=self.theme["secondary"],
                                     command=self.toggle_notifications)
        notif_check.grid(row=4, column=0, columnspan=2, sticky="w", pady=5)
        
        # About button
        about_btn = tk.Button(settings_frame, text="ℹ About",
                             command=self.show_about,
                             bg=self.theme["accent"], fg="white", relief="flat",
                             font=("Segoe UI", 9), cursor="hand2")
        about_btn.grid(row=5, column=0, columnspan=2, pady=10)

    def setup_keyboard_shortcuts(self):
        if self.config.get("keyboard_shortcuts"):
            self.root.bind("<space>", lambda e: self.toggle_timer())
            self.root.bind("<r>", lambda e: self.reset_timer())
            self.root.bind("<Escape>", lambda e: self.toggle_controls())
    
    def start_drag(self, event):
        self.x = event.x
        self.y = event.y
    
    def on_drag(self, event):
        x = self.root.winfo_x() + event.x - self.x
        y = self.root.winfo_y() + event.y - self.y
        self.root.geometry(f"+{x}+{y}")
        self.config.set("position", {"x": x, "y": y})
    
    def toggle_controls(self, event=None):
        if self.minimized:
            self.controls_frame.pack(fill="both", expand=True)
            self.root.geometry("320x420")
            self.minimized = False
        else:
            self.controls_frame.pack_forget()
            self.root.geometry("320x110")
            self.minimized = True
    
    def toggle_timer(self):
        if self.running:
            self.stop_timer()
        else:
            self.start_timer()
    
    def start_timer(self):
        try:
            hours = float(self.hours_entry.get())
            self.study_seconds = int(hours * 3600)
            self.running = True
            self.start_time = time.time()
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            self.hours_entry.config(state="disabled")
            
            task = self.task_entry.get()
            self.config.set("last_task", task)
            
            if self.minimized:
                pass
            else:
                self.toggle_controls()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    
    def stop_timer(self):
        if self.running:
            # Save session
            elapsed = int(time.time() - self.start_time)
            if elapsed > 60:  # Only save if more than 1 minute
                self.stats.add_session(elapsed, self.task_entry.get())
                self.add_xp(elapsed)
                self.update_stats_display()
        
        self.running = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.hours_entry.config(state="normal")
    
    def reset_timer(self):
        self.stop_timer()
        self.study_seconds = 0
        self.timer_label.config(fg=self.theme["fg"])
        self.pomodoro_mode = False
        self.is_break = False
    
    def quick_start(self, hours):
        self.hours_entry.delete(0, tk.END)
        self.hours_entry.insert(0, str(hours))
        self.start_timer()
    
    def start_pomodoro(self):
        self.pomodoro_mode = True
        self.pomodoro_count = 0
        self.is_break = False
        work_time = self.config.get("pomodoro_work") / 60
        self.quick_start(work_time)
    
    def next_pomodoro_phase(self):
        if not self.pomodoro_mode:
            return
        
        if self.is_break:
            # Start work session
            self.is_break = False
            work_time = self.config.get("pomodoro_work") / 60
            self.quick_start(work_time)
            self.show_notification("Work Time!", "Time to focus!")
        else:
            # Start break
            self.pomodoro_count += 1
            self.is_break = True
            
            if self.pomodoro_count % 4 == 0:
                break_time = self.config.get("pomodoro_long_break") / 60
                self.show_notification("Long Break!", "Take a longer break!")
            else:
                break_time = self.config.get("pomodoro_break") / 60
                self.show_notification("Break Time!", "Take a short break!")
            
            self.quick_start(break_time)
    
    def update_display(self):
        # Update clock
        tz = self.config.get("timezone")
        current_time = get_time_for_timezone(tz)
        time_str = current_time.strftime("%I:%M:%S %p")
        self.clock_label.config(text=f"🕐 {time_str}")
        
        # Update timer
        if self.running:
            elapsed = int(time.time() - self.start_time)
            remaining = self.study_seconds - elapsed
            
            if remaining <= 0:
                self.on_timer_complete()
                remaining = 0
            
            hours = remaining // 3600
            minutes = (remaining % 3600) // 60
            seconds = remaining % 60
            
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=time_str)
            
            # Color changes
            if remaining <= 60:
                self.timer_label.config(fg=self.theme["danger"])
            elif remaining <= 300:
                self.timer_label.config(fg=self.theme["warning"])
            else:
                self.timer_label.config(fg=self.theme["fg"])
        
        self.root.after(1000, self.update_display)
    
    def on_timer_complete(self):
        self.running = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.hours_entry.config(state="normal")
        
        # Save session
        self.stats.add_session(self.study_seconds, self.task_entry.get())
        self.add_xp(self.study_seconds)
        self.update_stats_display()
        
        # Play sound
        if self.config.get("sound_enabled"):
            threading.Thread(target=self.play_alarm, daemon=True).start()
        
        # Show notification
        self.show_notification("Timer Complete!", "Great job! Time's up!")
        
        # Pomodoro auto-continue
        if self.pomodoro_mode and self.config.get("auto_start_break"):
            self.root.after(2000, self.next_pomodoro_phase)
    
    def play_alarm(self):
        try:
            for _ in range(3):
                winsound.Beep(1000, 500)
                time.sleep(0.2)
        except:
            pass
    
    def show_notification(self, title, message):
        if self.config.get("show_notifications"):
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=5, threaded=True)
            except:
                messagebox.showinfo(title, message)
    
    def update_stats_display(self):
        today_total = self.stats.get_today_total()
        hours = today_total // 3600
        minutes = (today_total % 3600) // 60
        self.stats_label.config(text=f"📊 {hours}h {minutes}m")
    
    def format_time(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{hours}h {minutes}m"
    
    def add_xp(self, seconds):
        xp_gained = seconds // 60  # 1 XP per minute
        current_xp = self.config.get("xp")
        current_level = self.config.get("level")
        
        new_xp = current_xp + xp_gained
        xp_needed = current_level * 100
        
        if new_xp >= xp_needed:
            current_level += 1
            new_xp -= xp_needed
            self.show_notification("Level Up!", f"You reached Level {current_level}!")
        
        self.config.set("xp", new_xp)
        self.config.set("level", current_level)
    
    def update_streak(self):
        today = datetime.now().strftime("%Y-%m-%d")
        last_date = self.config.get("last_study_date")
        
        if last_date != today:
            yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
            if last_date == yesterday:
                streak = self.config.get("streak") + 1
            else:
                streak = 1 if self.stats.get_today_total() > 0 else 0
            
            self.config.set("streak", streak)
            self.config.set("last_study_date", today)
    
    def change_theme(self, event=None):
        theme_name = self.theme_var.get()
        self.config.set("theme", theme_name)
        self.theme = get_theme(theme_name)
        self.apply_theme_to_all_widgets()
    
    def change_timezone(self, event=None):
        tz = self.tz_var.get()
        self.config.set("timezone", tz)
    
    def change_opacity(self, value):
        self.root.attributes('-alpha', float(value))
        self.config.set("opacity", float(value))
    
    def toggle_sound(self):
        self.config.set("sound_enabled", self.sound_var.get())
    
    def toggle_notifications(self):
        self.config.set("show_notifications", self.notif_var.get())
    
    def export_stats(self):
        if self.stats.export_csv():
            messagebox.showinfo("Success", "Stats exported to study_export.csv")
        else:
            messagebox.showerror("Error", "Failed to export stats")
    
    def show_about(self):
        about_text = """Study Timer Pro v1.0
        
A professional study timer with:
• Pomodoro technique
• Statistics tracking
• Multiple themes
• World clock
• Gamification
• And much more!

Created for focused studying."""
        messagebox.showinfo("About", about_text)
    
    def apply_theme_to_all_widgets(self):
        """Apply theme to all widgets instantly without restart"""
        # Root and main frames
        self.root.configure(bg=self.theme["bg"])
        self.main_frame.configure(bg=self.theme["bg"], highlightbackground=self.theme["glow"])
        self.title_bar.configure(bg=self.theme["bg"])
        self.controls_frame.configure(bg=self.theme["bg"])
        
        # Labels
        self.clock_label.configure(bg=self.theme["bg"], fg=self.theme["accent"])
        self.timer_label.configure(bg=self.theme["bg"], fg=self.theme["glow"])
        self.stats_label.configure(bg=self.theme["bg"], fg=self.theme["accent"])
        self.settings_btn.configure(bg=self.theme["bg"], fg=self.theme["glow"])
        self.close_btn.configure(bg=self.theme["bg"], fg=self.theme["glow"])
        
        # Update notebook style
        self.update_notebook_style()
        
        # Timer tab
        self.timer_tab.configure(bg=self.theme["bg"])
        for widget in self.timer_tab.winfo_children():
            self.update_widget_theme(widget)
        
        # Presets tab
        self.presets_tab.configure(bg=self.theme["bg"])
        for widget in self.presets_tab.winfo_children():
            self.update_widget_theme(widget)
        
        # Stats tab
        self.stats_tab.configure(bg=self.theme["bg"])
        for widget in self.stats_tab.winfo_children():
            self.update_widget_theme(widget)
        
        # Settings tab
        self.settings_tab.configure(bg=self.theme["bg"])
        for widget in self.settings_tab.winfo_children():
            self.update_widget_theme(widget)
    
    def update_widget_theme(self, widget):
        """Recursively update widget colors"""
        try:
            widget_type = widget.winfo_class()
            
            if widget_type in ['Frame', 'Labelframe']:
                widget.configure(bg=self.theme["bg"])
            elif widget_type == 'Label':
                widget.configure(bg=self.theme["bg"], fg=self.theme["fg"])
            elif widget_type == 'Button':
                # Keep button-specific colors but update if needed
                current_bg = str(widget.cget('bg'))
                if 'green' in current_bg or '#4caf50' in current_bg:
                    widget.configure(bg=self.theme["success"])
                elif 'red' in current_bg or 'orange' in current_bg:
                    widget.configure(bg=self.theme["warning"])
                elif 'blue' in current_bg or '#4a9eff' in current_bg:
                    widget.configure(bg=self.theme["accent"])
                else:
                    widget.configure(bg=self.theme["secondary"], fg=self.theme["fg"])
            elif widget_type == 'Entry':
                widget.configure(bg=self.theme["secondary"], fg=self.theme["fg"], 
                               insertbackground=self.theme["fg"])
            elif widget_type == 'Checkbutton':
                widget.configure(bg=self.theme["bg"], fg=self.theme["fg"],
                               selectcolor=self.theme["secondary"])
            
            # Recursively update children
            for child in widget.winfo_children():
                self.update_widget_theme(child)
        except:
            pass
    
    def pulse_animation(self):
        """Subtle pulse animation for the timer border"""
        if self.running:
            # Pulse effect when timer is running
            colors = [self.theme["glow"], self.theme["accent"], self.theme["glow"]]
            color = colors[self.pulse_state % 3]
            self.main_frame.configure(highlightbackground=color)
            self.pulse_state += 1
            self.root.after(1000, self.pulse_animation)
        else:
            self.main_frame.configure(highlightbackground=self.theme["glow"])
            self.root.after(500, self.pulse_animation)
    
    def on_close(self, event=None):
        self.config.save_config()
        self.stats.save_stats()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTimerPro(root)
    root.mainloop()
