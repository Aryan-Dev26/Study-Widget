THEMES = {
    "dark": {
        "bg": "#1e1e1e",
        "fg": "#e0e0e0",
        "accent": "#4a9eff",
        "secondary": "#2d2d2d",
        "success": "#4caf50",
        "warning": "#ffa500",
        "danger": "#ff6b6b"
    },
    "light": {
        "bg": "#f5f5f5",
        "fg": "#333333",
        "accent": "#2196f3",
        "secondary": "#e0e0e0",
        "success": "#4caf50",
        "warning": "#ff9800",
        "danger": "#f44336"
    },
    "blue": {
        "bg": "#0d1b2a",
        "fg": "#e0e1dd",
        "accent": "#00b4d8",
        "secondary": "#1b263b",
        "success": "#06ffa5",
        "warning": "#ffba08",
        "danger": "#d00000"
    },
    "green": {
        "bg": "#1a2f1a",
        "fg": "#e8f5e9",
        "accent": "#66bb6a",
        "secondary": "#2e4a2e",
        "success": "#81c784",
        "warning": "#ffb74d",
        "danger": "#e57373"
    },
    "purple": {
        "bg": "#1a0033",
        "fg": "#e1d5e7",
        "accent": "#9c27b0",
        "secondary": "#2d1b3d",
        "success": "#ba68c8",
        "warning": "#ffb74d",
        "danger": "#ef5350"
    },
    "nord": {
        "bg": "#2e3440",
        "fg": "#eceff4",
        "accent": "#88c0d0",
        "secondary": "#3b4252",
        "success": "#a3be8c",
        "warning": "#ebcb8b",
        "danger": "#bf616a"
    }
}

def get_theme(theme_name):
    return THEMES.get(theme_name, THEMES["dark"])
