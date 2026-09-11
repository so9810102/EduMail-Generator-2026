"""
Setup Script for EduMail Generator 2026
========================================
This script sets up the EduMail Generator by:
1. Installing required Python packages
2. Detecting and downloading WebDrivers (ChromeDriver, GeckoDriver)
3. Asking user to select their preferred browser
4. Saving browser preference for bot.py

Usage:
    python setup.py

Compatibility: Python 3.7+
Last Updated: September 2026
"""

import subprocess
import sys
import os

# Import driver setup functions from versions.py
from __dwnldDrivers.versions import (
    get_firefox_version,
    get_chrome_version,
    setup_firefox_driver,
    setup_chrome_driver
)

# Import colors for terminal output
try:
    from __colors__.colors import fc, fg, fr, fy, fb, fm, sd, sb
except ImportError:
    # Fallback if colors module not available
    fc = fg = fr = fy = fb = fm = sd = sb = ""

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########

# List of required Python packages
REQUIRED_PACKAGES = [
    'requests',              # HTTP library for web requests
    'faker',                 # Generate fake student data
    'selenium',              # Browser automation (Selenium 4.x)
    'colorama',              # Colored terminal output
    'webdriver-manager'      # Automatic WebDriver management (NEW - 2026)
]

def install_package(package_name):
    """
    Install a Python package using pip.
    
    Args:
        package_name (str): Name of the package to install
        
    Returns:
        bool: True if successful, False if failed
    """
    try:
        print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}Installing {package_name}...", end=" ")
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', package_name, '-q'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"{fg}✓ Done")
        return True
    except subprocess.CalledProcessError:
        print(f"{fr}✗ Failed")
        return False
    except Exception as e:
        print(f"{fr}✗ Error: {str(e)}")
        return False

def install_all_packages():
    """
    Install all required packages.
    
    Returns:
        bool: True if all packages installed, False if any failed
    """
    print(f"\n{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}Installing Required Packages")
    print(f"{fc}{sd}{'='*50}\n")
    
    all_success = True
    for package in REQUIRED_PACKAGES:
        if not install_package(package):
            all_success = False
    
    print(f"\n{fc}{sd}{'='*50}")
    
    if all_success:
        print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fg}All packages installed successfully!\n")
        return True
    else:
        print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fr}Some packages failed to install\n")
        return False

def setup_browsers():
    """
    Detect installed browsers and setup WebDrivers.
    
    Returns:
        list: List of available browsers ['Firefox', 'Chrome', etc.]
    """
    available_browsers = []
    
    print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}Detecting Installed Browsers\n")
    
    # Check Firefox
    print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}Checking Firefox...", end=" ")
    firefox_ver = get_firefox_version()
    
    if firefox_ver:
        print(f"{fg}Found (v{firefox_ver})")
        print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}Setting up GeckoDriver...", end=" ")
        
        try:
            setup_firefox_driver()
            print(f"{fg}✓ Done")
            available_browsers.append('Firefox')
        except Exception as e:
            print(f"{fr}✗ Failed: {str(e)}")
    else:
        print(f"{fr}Not Found")
    
    # Check Chrome
    print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}Checking Chrome...", end=" ")
    chrome_ver = get_chrome_version()
    
    if chrome_ver:
        print(f"{fg}Found (v{chrome_ver})")
        print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}Setting up ChromeDriver...", end=" ")
        
        try:
            setup_chrome_driver()
            print(f"{fg}✓ Done")
            available_browsers.append('Chrome')
        except Exception as e:
            print(f"{fr}✗ Failed: {str(e)}")
    else:
        print(f"{fr}Not Found")
    
    return available_browsers

def select_browser(available_browsers):
    """
    Ask user to select their preferred browser.
    
    Args:
        available_browsers (list): List of available browsers
        
    Returns:
        str: Selected browser name ('firefox' or 'chrome') or None if failed
    """
    if not available_browsers:
        return None
    
    print(f"\n{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}Select Your Preferred Browser:")
    print(f"{fc}{sd}{'='*50}\n")
    
    # Display available browsers
    for index, browser in enumerate(available_browsers, 1):
        print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fg}{index}. {browser}")
    
    print(f"\n{fc}{sd}[{fm}{sb}*{fc}{sd}] ", end="")
    
    # Get user input with validation
    while True:
        try:
            print(f"{fy}Enter browser number (e.g., 1 or 2): ", end="")
            user_input = int(input().strip())
            
            # Validate input
            if 1 <= user_input <= len(available_browsers):
                selected = available_browsers[user_input - 1]
                print(f"{fg}✓ Selected: {selected}\n")
                return selected.lower()
            else:
                print(f"{fr}✗ Invalid number! Please try again.")
                print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] ", end="")
        
        except ValueError:
            print(f"{fr}✗ Invalid input! Please enter a number.")
            print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] ", end="")
        except KeyboardInterrupt:
            print(f"\n{fr}Setup cancelled by user")
            sys.exit(1)
        except Exception as e:
            print(f"{fr}✗ Error: {str(e)}")
            print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] ", end="")

def save_browser_preference(browser_name):
    """
    Save browser preference to prefBrowser.txt.
    
    Args:
        browser_name (str): Browser name ('firefox' or 'chrome')
        
    Returns:
        bool: True if saved successfully, False otherwise
    """
    try:
        with open('prefBrowser.txt', 'w') as f:
            f.write(browser_name.lower())
        return True
    except Exception as e:
        print(f"{fr}Error saving browser preference: {str(e)}")
        return False

def create_directories():
    """
    Create required directory structure.
    """
    directories = [
        '__banner',
        '__colors__',
        '__constants',
        '__dwnldDrivers'
    ]
    
    for directory in directories:
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except Exception as e:
            pass

def main():
    """
    Main setup function - orchestrates the entire setup process.
    
    Flow:
        1. Display welcome message
        2. Install required packages
        3. Detect and setup browsers
        4. Let user select preferred browser
        5. Save preference
        6. Display completion message
    """
    
    # Welcome message
    print(f"\n{fc}{sd}{'='*50}")
    print(f"{fm}{sb}  EduMail Generator 2026 - Setup")
    print(f"{fc}{sd}{'='*50}\n")
    
    # Step 1: Create directories
    create_directories()
    
    # Step 2: Install packages
    if not install_all_packages():
        print(f"{fr}Setup failed during package installation")
        sys.exit(1)
    
    # Step 3: Setup browsers
    available_browsers = setup_browsers()
    
    print()
    
    # Step 4: Validate that at least one browser is available
    if not available_browsers:
        print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fr}Error - No browsers found!")
        print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}Please install Chrome or Firefox to continue")
        sys.exit(1)
    
    # Step 5: Select browser
    selected_browser = select_browser(available_browsers)
    
    if not selected_browser:
        print(f"{fr}Browser selection failed")
        sys.exit(1)
    
    # Step 6: Save preference
    print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}Saving browser preference...", end=" ")
    
    if save_browser_preference(selected_browser):
        print(f"{fg}✓ Done")
    else:
        print(f"{fr}✗ Failed")
        sys.exit(1)
    
    # Step 7: Success message
    print(f"\n{fc}{sd}{'='*50}")
    print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fg}Setup Completed Successfully!")
    print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}You can now run: {fb}python bot.py")
    print(f"{fc}{sd}{'='*50}\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{fr}Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n{fr}Unexpected error: {str(e)}")
        sys.exit(1)
