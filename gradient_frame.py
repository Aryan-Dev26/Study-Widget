import tkinter as tk
from tkinter import Canvas

class GradientFrame(Canvas):
    """A frame with gradient background"""
    def __init__(self, parent, color1, color2, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.color1 = color1
        self.color2 = color2
        self.bind("<Configure>", self._draw_gradient)
        
    def _draw_gradient(self, event=None):
        """Draw gradient on canvas"""
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = height
        
        # Parse colors
        r1, g1, b1 = self._hex_to_rgb(self.color1)
        r2, g2, b2 = self._hex_to_rgb(self.color2)
        
        # Create gradient
        for i in range(limit):
            ratio = i / limit
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.create_line(0, i, width, i, tags=("gradient",), fill=color)
        
        # Lower gradient to back
        self.tag_lower("gradient")
    
    def _hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
