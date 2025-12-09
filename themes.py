THEMES = {
    "midnight": {
        "name": "Midnight Focus",
        "gradient_start": "#1e293b",  # slate-900
        "gradient_end": "#581c87",    # purple-900
        "bg": "#1e1b4b",
        "card_bg": "#1e293b",         # slate-800 with transparency effect
        "fg": "#dbeafe",              # blue-100
        "accent": "#a78bfa",          # purple-400
        "secondary": "#334155",       # slate-700
        "success": "#a78bfa",
        "warning": "#fbbf24",
        "danger": "#ef4444",
        "glow": "#a78bfa",
        "timer": "#93c5fd",           # blue-300
        "border": "#a78bfa"
    },
    "sunrise": {
        "name": "Sunrise Energy",
        "gradient_start": "#fed7aa",  # orange-200
        "gradient_end": "#fef3c7",    # yellow-100
        "bg": "#fff7ed",
        "card_bg": "#ffffff",
        "fg": "#1f2937",              # gray-800
        "accent": "#ea580c",          # orange-600
        "secondary": "#fed7aa",       # orange-200
        "success": "#ea580c",
        "warning": "#f59e0b",
        "danger": "#dc2626",
        "glow": "#fb923c",
        "timer": "#c2410c",           # orange-700
        "border": "#fb923c"
    },
    "forest": {
        "name": "Forest Calm",
        "gradient_start": "#064e3b",  # emerald-900
        "gradient_end": "#115e59",    # teal-800
        "bg": "#064e3b",
        "card_bg": "#065f46",         # emerald-800
        "fg": "#d1fae5",              # emerald-50
        "accent": "#34d399",          # green-400
        "secondary": "#047857",       # emerald-700
        "success": "#10b981",
        "warning": "#fbbf24",
        "danger": "#ef4444",
        "glow": "#34d399",
        "timer": "#6ee7b7",           # green-300
        "border": "#34d399"
    },
    "coffee": {
        "name": "Coffee Break",
        "gradient_start": "#fef3c7",  # amber-100
        "gradient_end": "#fde68a",    # yellow-200
        "bg": "#fef3c7",
        "card_bg": "#fde68a",
        "fg": "#78350f",              # amber-900
        "accent": "#d97706",          # amber-700
        "secondary": "#fde68a",
        "success": "#d97706",
        "warning": "#f59e0b",
        "danger": "#dc2626",
        "glow": "#f59e0b",
        "timer": "#92400e",           # amber-800
        "border": "#f59e0b"
    },
    "ocean": {
        "name": "Ocean Depth",
        "gradient_start": "#164e63",  # cyan-900
        "gradient_end": "#1e3a8a",    # blue-900
        "bg": "#0c4a6e",
        "card_bg": "#1e3a8a",
        "fg": "#cffafe",              # cyan-50
        "accent": "#22d3ee",          # cyan-400
        "secondary": "#0e7490",       # cyan-700
        "success": "#06b6d4",
        "warning": "#fbbf24",
        "danger": "#ef4444",
        "glow": "#22d3ee",
        "timer": "#67e8f9",           # cyan-300
        "border": "#22d3ee"
    },
    "minimal": {
        "name": "Minimal Dark",
        "gradient_start": "#111827",  # gray-900
        "gradient_end": "#1f2937",    # gray-800
        "bg": "#111827",
        "card_bg": "#1f2937",
        "fg": "#f3f4f6",              # gray-100
        "accent": "#9ca3af",          # gray-400
        "secondary": "#374151",       # gray-700
        "success": "#6b7280",
        "warning": "#9ca3af",
        "danger": "#ef4444",
        "glow": "#6b7280",
        "timer": "#d1d5db",           # gray-300
        "border": "#6b7280"
    }
}

def get_theme(theme_name):
    return THEMES.get(theme_name, THEMES["midnight"])
