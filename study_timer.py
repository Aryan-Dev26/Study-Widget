import tkinter as tk
from datetime import datetime
import time

class StudyTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("")
        self.root.geometry("220x80")
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)  # Remove window borders
        self.root.attributes('-alpha', 0.9)  # Slight transparency
        
        # Dark theme colors
        self.bg_color = "#1e1e1e"
        self.fg_color = "#e0e0e0"
        self.accent_color = "#4a9eff"
        
        self.root.configure(bg=self.bg_color)
        
        self.study_seconds = 0
        self.running = False
        self.start_time = None
        self.minimized = False
        
        # Main container
        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(fill="both", expand=True)
        
        # Draggable title bar
        self.title_bar = tk.Frame(self.main_frame, bg=self.bg_color, cursor="fleur")
        self.title_bar.pack(fill="x")
        self.title_bar.bind("<Button-1>", self.start_drag)
        self.title_bar.bind("<B1-Motion>", self.on_drag)
        
        # Timer display (compact)
        self.timer_label = tk.Label(self.title_bar, text="00:00:00", 
                                    font=("Segoe UI", 24), 
                                    bg=self.bg_color, fg=self.fg_color)
        self.timer_label.pack(side="left", padx=10, pady=5)
        self.timer_label.bind("<Button-1>", self.start_drag)
        self.timer_label.bind("<B1-Motion>", self.on_drag)
        
        # Minimize button
        self.min_btn = tk.Label(self.title_bar, text="⚙", font=("Segoe UI", 12), 
                               bg=self.bg_color, fg=self.fg_color, cursor="hand2")
        self.min_btn.pack(side="right", padx=5)
        self.min_btn.bind("<Button-1>", self.toggle_controls)
        
        # Close button
        self.close_btn = tk.Label(self.title_bar, text="✕", font=("Segoe UI", 12), 
                                  bg=self.bg_color, fg=self.fg_color, cursor="hand2")
        self.close_btn.pack(side="right", padx=5)
        self.close_btn.bind("<Button-1>", lambda e: self.root.quit())
        
        # Controls frame (hidden by default)
        self.controls_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        
        # Input
        input_frame = tk.Frame(self.controls_frame, bg=self.bg_color)
        input_frame.pack(pady=5)
        
        tk.Label(input_frame, text="Hours:", bg=self.bg_color, fg=self.fg_color, 
                font=("Segoe UI", 9)).pack(side="left", padx=5)
        self.hours_entry = tk.Entry(input_frame, width=6, font=("Segoe UI", 9), 
                                    bg="#2d2d2d", fg=self.fg_color, 
                                    insertbackground=self.fg_color, relief="flat")
        self.hours_entry.pack(side="left")
        self.hours_entry.insert(0, "1")
        
        # Buttons (compact)
        button_frame = tk.Frame(self.controls_frame, bg=self.bg_color)
        button_frame.pack(pady=5)
        
        self.start_btn = tk.Button(button_frame, text="▶", command=self.start_timer, 
                                   bg=self.accent_color, fg="white", relief="flat",
                                   font=("Segoe UI", 10), cursor="hand2", width=3)
        self.start_btn.pack(side="left", padx=2)
        
        self.stop_btn = tk.Button(button_frame, text="⏸", command=self.stop_timer, 
                                  bg="#ff6b6b", fg="white", relief="flat",
                                  font=("Segoe UI", 10), cursor="hand2", width=3, state="disabled")
        self.stop_btn.pack(side="left", padx=2)
        
        self.reset_btn = tk.Button(button_frame, text="↻", command=self.reset_timer,
                                   bg="#2d2d2d", fg=self.fg_color, relief="flat",
                                   font=("Segoe UI", 10), cursor="hand2", width=3)
        self.reset_btn.pack(side="left", padx=2)
        
        self.update_timer_display()
    
    def start_drag(self, event):
        self.x = event.x
        self.y = event.y
    
    def on_drag(self, event):
        x = self.root.winfo_x() + event.x - self.x
        y = self.root.winfo_y() + event.y - self.y
        self.root.geometry(f"+{x}+{y}")
    
    def toggle_controls(self, event=None):
        if self.minimized:
            self.controls_frame.pack(fill="x")
            self.root.geometry("220x140")
            self.minimized = False
        else:
            self.controls_frame.pack_forget()
            self.root.geometry("220x80")
            self.minimized = True
    
    def start_timer(self):
        try:
            hours = float(self.hours_entry.get())
            self.study_seconds = int(hours * 3600)
            self.running = True
            self.start_time = time.time()
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            self.hours_entry.config(state="disabled")
            self.toggle_controls()  # Auto-minimize controls
        except ValueError:
            pass
    
    def stop_timer(self):
        self.running = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.hours_entry.config(state="normal")
    
    def reset_timer(self):
        self.running = False
        self.study_seconds = 0
        self.timer_label.config(fg=self.fg_color)
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.hours_entry.config(state="normal")
    
    def update_timer_display(self):
        if self.running:
            elapsed = int(time.time() - self.start_time)
            remaining = self.study_seconds - elapsed
            
            if remaining <= 0:
                self.running = False
                self.start_btn.config(state="normal")
                self.stop_btn.config(state="disabled")
                self.hours_entry.config(state="normal")
                self.timer_label.config(fg="#ff6b6b")
                self.root.bell()
                remaining = 0
            
            hours = remaining // 3600
            minutes = (remaining % 3600) // 60
            seconds = remaining % 60
            
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=time_str)
            
            # Subtle color change when low on time
            if remaining <= 300 and remaining > 0:
                self.timer_label.config(fg="#ffa500")
            elif remaining > 300:
                self.timer_label.config(fg=self.fg_color)
        else:
            if self.study_seconds == 0:
                self.timer_label.config(text="00:00:00")
        
        self.root.after(1000, self.update_timer_display)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTimer(root)
    root.mainloop()
