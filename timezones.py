from datetime import datetime, timezone, timedelta

TIMEZONES = {
    "Local": 0,
    "UTC": 0,
    "USA - Eastern (EST)": -5,
    "USA - Central (CST)": -6,
    "USA - Mountain (MST)": -7,
    "USA - Pacific (PST)": -8,
    "UK - London (GMT)": 0,
    "Europe - Paris (CET)": 1,
    "Europe - Berlin (CET)": 1,
    "Europe - Moscow (MSK)": 3,
    "India - Delhi (IST)": 5.5,
    "China - Beijing (CST)": 8,
    "Japan - Tokyo (JST)": 9,
    "Australia - Sydney (AEDT)": 11,
    "Brazil - São Paulo (BRT)": -3,
    "Canada - Toronto (EST)": -5,
    "Dubai (GST)": 4,
    "Singapore (SGT)": 8,
    "Hong Kong (HKT)": 8,
    "South Korea - Seoul (KST)": 9,
    "Thailand - Bangkok (ICT)": 7,
    "Indonesia - Jakarta (WIB)": 7,
    "Philippines - Manila (PHT)": 8,
    "Pakistan - Karachi (PKT)": 5,
    "Bangladesh - Dhaka (BST)": 6,
    "Turkey - Istanbul (TRT)": 3,
    "South Africa - Cape Town (SAST)": 2,
    "Egypt - Cairo (EET)": 2,
    "Argentina - Buenos Aires (ART)": -3,
    "Mexico - Mexico City (CST)": -6,
    "New Zealand - Auckland (NZDT)": 13
}

def get_time_for_timezone(tz_name):
    if tz_name == "Local":
        return datetime.now()
    
    offset = TIMEZONES.get(tz_name, 0)
    utc_time = datetime.now(timezone.utc)
    tz_time = utc_time + timedelta(hours=offset)
    return tz_time

def get_timezone_list():
    return sorted(TIMEZONES.keys())
