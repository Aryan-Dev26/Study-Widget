import json
import os
from datetime import datetime

class Config:
    def __init__(self):
        self.config_file = "study_timer_config.json"
        self.default_config = {
            "theme": "cyberpunk",
            "opacity": 0.92,
            "font_size": 32,
            "position": {"x": 100, "y": 100},
            "timezone": "Local",
            "sound_enabled": True,
            "volume": 0.5,
            "tick_sound": False,
            "pomodoro_work": 25,
            "pomodoro_break": 5,
            "pomodoro_long_break": 15,
            "auto_start_break": False,
            "show_notifications": True,
            "keyboard_shortcuts": True,
            "system_tray": True,
            "auto_start": False,
            "last_task": "",
            "daily_goal": 8,
            "streak": 0,
            "last_study_date": "",
            "total_study_time": 0,
            "level": 1,
            "xp": 0
        }
        self.config = self.load_config()
    
    def load_config(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    return {**self.default_config, **loaded}
            except:
                return self.default_config.copy()
        return self.default_config.copy()
    
    def save_config(self):
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
        self.save_config()
