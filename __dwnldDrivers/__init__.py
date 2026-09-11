"""WebDriver management module"""
from .versions import (
    get_chrome_version,
    get_firefox_version,
    setup_chrome_driver,
    setup_firefox_driver
)

__all__ = [
    'get_chrome_version',
    'get_firefox_version',
    'setup_chrome_driver',
    'setup_firefox_driver'
]
