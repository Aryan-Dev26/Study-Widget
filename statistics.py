import json
import os
from datetime import datetime, timedelta

class Statistics:
    def __init__(self):
        self.stats_file = "study_stats.json"
        self.stats = self.load_stats()
    
    def load_stats(self):
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, 'r') as f:
                    return json.load(f)
            except:
                return {"sessions": [], "daily_totals": {}}
        return {"sessions": [], "daily_totals": {}}
    
    def save_stats(self):
        try:
            with open(self.stats_file, 'w') as f:
                json.dump(self.stats, f, indent=4)
        except Exception as e:
            print(f"Error saving stats: {e}")
    
    def add_session(self, duration, task=""):
        session = {
            "date": datetime.now().isoformat(),
            "duration": duration,
            "task": task
        }
        self.stats["sessions"].append(session)
        
        today = datetime.now().strftime("%Y-%m-%d")
        if today not in self.stats["daily_totals"]:
            self.stats["daily_totals"][today] = 0
        self.stats["daily_totals"][today] += duration
        
        self.save_stats()
    
    def get_today_total(self):
        today = datetime.now().strftime("%Y-%m-%d")
        return self.stats["daily_totals"].get(today, 0)
    
    def get_week_total(self):
        total = 0
        today = datetime.now()
        for i in range(7):
            date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
            total += self.stats["daily_totals"].get(date, 0)
        return total
    
    def get_month_total(self):
        total = 0
        today = datetime.now()
        for i in range(30):
            date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
            total += self.stats["daily_totals"].get(date, 0)
        return total
    
    def export_csv(self, filename="study_export.csv"):
        try:
            with open(filename, 'w') as f:
                f.write("Date,Duration (seconds),Task\n")
                for session in self.stats["sessions"]:
                    f.write(f"{session['date']},{session['duration']},{session['task']}\n")
            return True
        except:
            return False
