THEMES = {
    "midnight": {
        "name": "Midnight Focus",
        "bg": "#1e1b4b",  # Deep purple-blue
        "fg": "#dbeafe",  # Light blue
        "accent": "#a78bfa",  # Purple
        "secondary": "#312e81",  # Darker purple
        "success": "#a78bfa",
        "warning": "#fbbf24",
        "danger": "#ef4444",
        "glow": "#a78bfa",
        "timer": "#93c5fd"  # Light blue for timer
    },
    "sunrise": {
        "name": "Sunrise Energy",
        "bg": "#fff7ed",  # Warm cream
        "fg": "#1f2937",  # Dark gray
        "accent": "#ea580c",  # Orange
        "secondary": "#fed7aa",  # Light orange
        "success": "#ea580c",
        "warning": "#f59e0b",
        "danger": "#dc2626",
        "glow": "#fb923c",
        "timer": "#c2410c"  # Deep orange
    },
    "forest": {
        "name": "Forest Calm",
        "bg": "#064e3b",  # Deep green
        "fg": "#d1fae5",  # Light mint
        "accent": "#34d399",  # Bright green
        "secondary": "#065f46",  # Medium green
        "success": "#10b981",
        "warning": "#fbbf24",
        "danger": "#ef4444",
        "glow": "#34d399",
        "timer": "#6ee7b7"  # Mint green
    },
    "coffee": {
        "name": "Coffee Break",
        "bg": "#fef3c7",  # Light cream
        "fg": "#78350f",  # Dark brown
        "accent": "#d97706",  # Amber
        "secondary": "#fde68a",  # Light yellow
        "success": "#d97706",
        "warning": "#f59e0b",
        "danger": "#dc2626",
        "glow": "#f59e0b",
        "timer": "#92400e"  # Deep brown
    },
    "ocean": {
        "name": "Ocean Depth",
        "bg": "#0c4a6e",  # Deep blue
        "fg": "#cffafe",  # Light cyan
        "accent": "#22d3ee",  # Bright cyan
        "secondary": "#075985",  # Medium blue
        "success": "#06b6d4",
        "warning": "#fbbf24",
        "danger": "#ef4444",
        "glow": "#22d3ee",
        "timer": "#67e8f9"  # Light cyan
    },
    "minimal": {
        "name": "Minimal Dark",
        "bg": "#111827",  # Very dark gray
        "fg": "#f3f4f6",  # Light gray
        "accent": "#9ca3af",  # Medium gray
        "secondary": "#1f2937",  # Dark gray
        "success": "#6b7280",
        "warning": "#9ca3af",
        "danger": "#ef4444",
        "glow": "#6b7280",
        "timer": "#d1d5db"  # Light gray
    }
}

def get_theme(theme_name):
    return THEMES.get(theme_name, THEMES["midnight"])
