"""
WebDriver Management Module for EduMail Generator 2026
Handles ChromeDriver and GeckoDriver detection and setup
"""

import platform
import subprocess
import os

def get_chrome_version():
    """
    Get installed Chrome browser version
    
    Returns:
        str: Chrome version or None if not found
    """
    try:
        system = platform.system()
        
        if system == 'Windows':
            # Check common Chrome installation paths on Windows
            paths = [
                r'C:\Program Files\Google\Chrome\Application\chrome.exe',
                r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
            ]
            
            for path in paths:
                if os.path.exists(path):
                    result = subprocess.run(
                        [path, '--version'],
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    if result.returncode == 0:
                        return result.stdout.strip().split()[-1]
        
        elif system == 'Darwin':  # macOS
            result = subprocess.run(
                ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                return result.stdout.strip().split()[-1]
        
        elif system == 'Linux':
            result = subprocess.run(
                ['google-chrome', '--version'],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                return result.stdout.strip().split()[-1]
        
        return None
    
    except Exception as e:
        return None

def get_firefox_version():
    """
    Get installed Firefox browser version
    
    Returns:
        str: Firefox version or None if not found
    """
    try:
        system = platform.system()
        
        if system == 'Windows':
            paths = [
                r'C:\Program Files\Mozilla Firefox\firefox.exe',
                r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe',
            ]
            
            for path in paths:
                if os.path.exists(path):
                    result = subprocess.run(
                        [path, '--version'],
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    if result.returncode == 0:
                        return result.stdout.strip().split()[-1]
        
        elif system == 'Darwin':  # macOS
            result = subprocess.run(
                ['/Applications/Firefox.app/Contents/MacOS/firefox', '--version'],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                return result.stdout.strip().split()[-1]
        
        elif system == 'Linux':
            result = subprocess.run(
                ['firefox', '--version'],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                return result.stdout.strip().split()[-1]
        
        return None
    
    except Exception as e:
        return None

def setup_chrome_driver():
    """
    Setup ChromeDriver using webdriver-manager
    webdriver-manager handles automatic download and caching
    
    Returns:
        bool: True if successful
    """
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        ChromeDriverManager().install()
        return True
    except Exception as e:
        raise Exception(f"Failed to setup ChromeDriver: {str(e)}")

def setup_firefox_driver():
    """
    Setup GeckoDriver (Firefox) using webdriver-manager
    webdriver-manager handles automatic download and caching
    
    Returns:
        bool: True if successful
    """
    try:
        from webdriver_manager.firefox import GeckoDriverManager
        GeckoDriverManager().install()
        return True
    except Exception as e:
        raise Exception(f"Failed to setup GeckoDriver: {str(e)}")
