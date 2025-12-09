import pystray
from PIL import Image, ImageDraw
import threading

class SystemTray:
    def __init__(self, app):
        self.app = app
        self.icon = None
        self.running = False
        
    def create_icon_image(self):
        """Create a simple icon for the system tray"""
        # Create a 64x64 image with a timer icon
        width = 64
        height = 64
        image = Image.new('RGB', (width, height), color='#1e1b4b')
        dc = ImageDraw.Draw(image)
        
        # Draw a clock circle
        dc.ellipse([8, 8, 56, 56], fill='#a78bfa', outline='#93c5fd', width=3)
        
        # Draw clock hands
        dc.line([32, 32, 32, 16], fill='#1e1b4b', width=3)  # Hour hand
        dc.line([32, 32, 44, 32], fill='#1e1b4b', width=2)  # Minute hand
        
        # Center dot
        dc.ellipse([28, 28, 36, 36], fill='#1e1b4b')
        
        return image
    
    def show_window(self, icon=None, item=None):
        """Show the main window"""
        self.app.root.deiconify()
        self.app.root.lift()
        self.app.root.focus_force()
    
    def hide_window(self):
        """Hide the main window to tray"""
        self.app.root.withdraw()
    
    def quit_app(self, icon=None, item=None):
        """Quit the application"""
        self.running = False
        if self.icon:
            self.icon.stop()
        self.app.on_close()
    
    def toggle_window(self, icon=None, item=None):
        """Toggle window visibility"""
        if self.app.root.state() == 'withdrawn':
            self.show_window()
        else:
            self.hide_window()
    
    def start_timer(self, icon=None, item=None):
        """Start the timer from tray"""
        self.show_window()
        self.app.start_timer()
    
    def stop_timer(self, icon=None, item=None):
        """Stop the timer from tray"""
        self.app.stop_timer()
    
    def create_menu(self):
        """Create the system tray menu"""
        return pystray.Menu(
            pystray.MenuItem("Show/Hide", self.toggle_window, default=True),
            pystray.MenuItem("Start Timer", self.start_timer),
            pystray.MenuItem("Stop Timer", self.stop_timer),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Quit", self.quit_app)
        )
    
    def run(self):
        """Run the system tray icon"""
        self.running = True
        image = self.create_icon_image()
        self.icon = pystray.Icon(
            "StudyTimer",
            image,
            "Study Timer Pro",
            self.create_menu()
        )
        
        # Run in a separate thread
        def run_icon():
            self.icon.run()
        
        thread = threading.Thread(target=run_icon, daemon=True)
        thread.start()
    
    def update_tooltip(self, text):
        """Update the tray icon tooltip"""
        if self.icon:
            self.icon.title = text
