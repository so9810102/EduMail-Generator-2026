"""
Color codes for terminal output
Provides ANSI color codes for colored terminal text
Updated: September 2026
"""

# ANSI Color Codes - FIXED VERSION
fc = '\033[36m'   # Foreground Cyan
fg = '\033[32m'   # Foreground Green
fr = '\033[31m'   # Foreground Red
fy = '\033[33m'   # Foreground Yellow
fb = '\033[34m'   # Foreground Blue
fm = '\033[35m'   # Foreground Magenta
sd = '\033[0m'    # Reset/Default
sb = '\033[1m'    # Bold

# Alternative names
CYAN = fc
GREEN = fg
RED = fr
YELLOW = fy
BLUE = fb
MAGENTA = fm
DEFAULT = sd
BOLD = sb

# Reset code for terminal
RESET = '\033[0m'
