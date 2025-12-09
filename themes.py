THEMES = {
    "cyberpunk": {
        "bg": "#0a0e27",
        "fg": "#00ff9f",
        "accent": "#ff006e",
        "secondary": "#1a1f3a",
        "success": "#00ff9f",
        "warning": "#ffbe0b",
        "danger": "#ff006e",
        "glow": "#00ff9f"
    },
    "neon": {
        "bg": "#0d0221",
        "fg": "#7df9ff",
        "accent": "#ff10f0",
        "secondary": "#1a0b2e",
        "success": "#39ff14",
        "warning": "#ffaa00",
        "danger": "#ff0080",
        "glow": "#7df9ff"
    },
    "matrix": {
        "bg": "#000000",
        "fg": "#00ff00",
        "accent": "#00ff00",
        "secondary": "#0a0a0a",
        "success": "#00ff00",
        "warning": "#ffff00",
        "danger": "#ff0000",
        "glow": "#00ff00"
    },
    "synthwave": {
        "bg": "#2b213a",
        "fg": "#f9f2e7",
        "accent": "#ff6c11",
        "secondary": "#3d2e4f",
        "success": "#72dec2",
        "warning": "#ffd319",
        "danger": "#fe4450",
        "glow": "#ff6c11"
    },
    "dark": {
        "bg": "#0f0f0f",
        "fg": "#e0e0e0",
        "accent": "#4a9eff",
        "secondary": "#1a1a1a",
        "success": "#4caf50",
        "warning": "#ffa500",
        "danger": "#ff6b6b",
        "glow": "#4a9eff"
    },
    "arctic": {
        "bg": "#0c1821",
        "fg": "#c0e0ff",
        "accent": "#00d9ff",
        "secondary": "#1b2a3a",
        "success": "#00ffc8",
        "warning": "#ffd700",
        "danger": "#ff4757",
        "glow": "#00d9ff"
    }
}

def get_theme(theme_name):
    return THEMES.get(theme_name, THEMES["dark"])
