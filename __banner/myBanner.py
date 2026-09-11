"""
Banner display module for EduMail Generator 2026
Shows welcome banner when bot starts
"""

def bannerTop():
    """
    Display welcome banner at startup
    
    Returns:
        str: Banner text
    """
    banner = """
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║         _____    _ _   __  __       _ _    ____              ║
║        | ____|__| | |_   |  \\/  | __ _(_) |  / ___| ___ _ __   ║
║        |  _| / _` | | | | | |\\/| |/ _` | | | | |  _ / _ \ '_ \  ║
║        | |__| (_| | |_| | | |  | | (_| | | | | |_| |  __/ | | |_║
║        |_____\__,_|\__,_| |_|  |_|\__,_|_|_|  \____|\____|_| |_(_)║
║                                                                ║
║                2026 Edition - Selenium 4.x Compatible          ║
║             Advanced College Application Automation            ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
"""
    return banner

def display_banner():
    """Display banner to console"""
    print(bannerTop())
