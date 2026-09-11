"""
Enhanced __init__.py for colors module
Imports all ANSI color codes
"""

from .colors import (
    fc, fg, fr, fy, fb, fm, sd, sb,
    CYAN, GREEN, RED, YELLOW, BLUE, MAGENTA, DEFAULT, BOLD, RESET
)

__all__ = [
    'fc', 'fg', 'fr', 'fy', 'fb', 'fm', 'sd', 'sb',
    'CYAN', 'GREEN', 'RED', 'YELLOW', 'BLUE', 'MAGENTA', 'DEFAULT', 'BOLD', 'RESET'
]
