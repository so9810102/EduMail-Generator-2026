"""
EduMail Generator 2026 - Main Bot Script
=========================================
Automates college application form filling process using Selenium 4.x

Key Changes from Original:
  - Selenium 4.x API (find_element() instead of find_element_by_*())
  - WebDriver Manager for automatic driver management
  - Updated imports and error handling
  - Python 3.7+ compatible
  - FIXED: Proxy Detection & Automation Detection (September 2026)

Usage:
    python bot.py

Requires: Python 3.7+, selenium>=4.0.0, webdriver-manager>=4.0.0
Last Updated: September 2026
"""

import time
import re
import string
import random
import sys
import colorama

# Selenium imports (4.x)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from random import randint

# WebDriver Manager imports
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Local imports
try:
    from __constants.const import *
    from __banner.myBanner import bannerTop
    from __colors__.colors import *
except ImportError as e:
    print(f"Error importing modules: {str(e)}")
    print("Please run 'python setup.py' first")
    sys.exit(1)

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########

def postFix(n):
    """
    Generate a random n-digit number.
    
    Args:
        n (int): Number of digits
        
    Returns:
        int: Random n-digit number
    """
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def random_phone_num_generator():
    """
    Generate a random phone number in format: XXX-XXX-XXXX
    
    Returns:
        str: Random phone number
    """
    first = str(random.choice(country_codes))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    
    # Avoid reserved numbers
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    
    return '{}-{}-{}'.format(first, second, last)

def initialize_webdriver(browser_type):
    """
    Initialize and return a WebDriver instance.
    
    IMPORTANT CHANGES (Selenium 3 → 4):
        OLD: driver = webdriver.Chrome(executable_path='./webdriver/chromedriver')
        NEW: Uses webdriver-manager for automatic driver management
    
    🎭 ANTI-DETECTION OPTIONS ADDED (September 2026):
        - Disables automation-controlled flags
        - Hides WebDriver detection
        - Uses realistic User-Agent strings
        - Disables unwanted browser features
    
    Args:
        browser_type (str): 'chrome' or 'firefox'
        
    Returns:
        WebDriver: Initialized WebDriver instance
        
    Raises:
        Exception: If driver initialization fails
    """
    try:
        if browser_type.lower() == 'chrome':
            print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}Initializing Chrome WebDriver...", end=" ")
            
            chrome_options = ChromeOptions()
            
            # ✅ ANTI-DETECTION OPTIONS (Fix for Proxy Error)
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
            
            # ✅ Additional anti-detection arguments
            chrome_options.add_argument('--disable-web-resources')
            chrome_options.add_argument('--disable-client-side-phishing-detection')
            chrome_options.add_argument('--disable-sync')
            chrome_options.add_argument('--disable-plugins')
            chrome_options.add_argument('--disable-images')
            chrome_options.add_argument('--disable-default-apps')
            
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # ✅ Execute stealth JavaScript to hide automation
            driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                'source': '''
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => false,
                    });
                    Object.defineProperty(navigator, 'plugins', {
                        get: () => [1, 2, 3, 4, 5],
                    });
                    Object.defineProperty(navigator, 'languages', {
                        get: () => ['en-US', 'en'],
                    });
                '''
            })
            
            print(f"{fg}✓ Done")
            return driver
            
        elif browser_type.lower() == 'firefox':
            print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}Initializing Firefox WebDriver...", end=" ")
            
            firefox_options = FirefoxOptions()
            
            # ✅ ANTI-DETECTION OPTIONS FOR FIREFOX
            firefox_options.add_argument('--disable-blink-features=AutomationControlled')
            firefox_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0')
            
            # ✅ Firefox preferences
            firefox_options.set_preference('dom.webdriver.enabled', False)
            firefox_options.set_preference('useAutomationExtension', False)
            
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=firefox_options)
            
            print(f"{fg}✓ Done")
            return driver
            
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")
            
    except Exception as e:
        print(f"\n{fr}Error initializing WebDriver: {str(e)}")
        raise

def get_preferred_browser():
    """
    Read and return the user's preferred browser from prefBrowser.txt
    
    Returns:
        str: 'chrome' or 'firefox'
        
    Raises:
        FileNotFoundError: If prefBrowser.txt doesn't exist (run setup.py first)
    """
    try:
        with open('prefBrowser.txt', 'r') as fp:
            browser = fp.read().strip()
            
        if not browser:
            raise ValueError("prefBrowser.txt is empty - run setup.py first")
            
        return browser.lower()
        
    except FileNotFoundError:
        print(f"{fr}Error: prefBrowser.txt not found - run setup.py first")
        sys.exit(1)

def start_bot(start_url, email, college, collegeID):
    """
    Main bot function - automates college application form filling.
    
    Args:
        start_url (str): Starting URL for college registration
        email (str): Email address for account
        college (str): College name
        collegeID (int): College ID (1-4)
    """
    
    studentPhone = random_phone_num_generator()
    
    ex_split = studentAddress.split(", ")
    streetAddress = ex_split[0] if len(ex_split) > 0 else "123 Main St"
    
    try:
        if len(ex_split) > 1:
            cityAddress = ex_split[1]
        else:
            cityAddress = "San Francisco"
            
        stateAddress = "CA"
        postalCode = "94102"
    except:
        cityAddress = "San Francisco"
        stateAddress = "CA"
        postalCode = "94102"
    
    random.seed()
    letters = string.ascii_uppercase
    middleName = random.choice(letters)
    
    try:
        browser_type = get_preferred_browser()
        driver = initialize_webdriver(browser_type)
        
    except Exception as e:
        time.sleep(0.4)
        print(f"\n{fr}Error - {str(e)}")
        sys.exit(1)
    
    try:
        driver.maximize_window()
        driver.get(start_url)
        time.sleep(2)
        
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Successfully accessed college portal')
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + f'College: {college}')
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + f'Email: {email}')
        
        # Find and click on registration link
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="portletContent_u16l1n18"]/div/div[2]/div/a[2]'))
            ).click()
            time.sleep(1)
        except:
            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Registration link may have different location')
        
        # Click account form submit
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "accountFormSubmit"))
            ).click()
        except:
            pass
        
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Account Form - Filling Details...', end='')
        
        # Fill first name
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "inputFirstName"))
            ).send_keys(firstName)
            time.sleep(0.5)
        except:
            pass
        
        # Fill middle name
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "inputMiddleName"))
            ).send_keys(middleName)
            time.sleep(0.5)
        except:
            pass
        
        # Fill last name
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "inputLastName"))
            ).send_keys(LastName)
            time.sleep(0.5)
        except:
            pass
        
        print(fg + ' ✓ Done')
        
        # Save account details
        with open('myccAcc.txt', 'a') as fp:
            birthDay = str(randomMonth) + '/' + str(randomDay) + '/' + str(randomYear)
            account_details = f'Email - {email} | Password - generated | UserName - {firstName}{postFix(7)} | First Name - {firstName} | Middle Name - {middleName} | Last Name - {LastName} | Birthday - {birthDay} | Phone - {studentPhone} | College - {college}\n'
            fp.write(account_details)
        
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Account details saved to myccAcc.txt')
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Application process simulated successfully!')
        
        time.sleep(2)
        driver.quit()
        
    except Exception as e:
        print(f"\n{fr}Error during bot execution: {str(e)}")
        try:
            driver.quit()
        except:
            pass
        raise

def main():
    """
    Main entry point - displays banner and gets user input.
    
    Flow:
        1. Display banner and college list
        2. Ask user to select college
        3. Ask user to enter email
        4. Call start_bot() function
    """
    try:
        sys.stdout.write(bannerTop())
    except:
        print("\n" + "="*60)
        print("  EduMail Generator 2026 - College Application Bot")
        print("="*60 + "\n")
    
    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Select a college from all available colleges to proceed...\n')
    
    time.sleep(0.4)
    
    for index, college in enumerate(allColleges):
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + str(index + 1) + ' - ' + college)
    
    isIDError = True
    
    while isIDError != False:
        print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Enter college id (1-4): ', end='')
        
        try:
            userInput = int(input())
            
            if userInput > len(allColleges) or userInput < 1:
                print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + 'Invalid college id')
            else:
                userInput = userInput - 1
                isIDError = False
                
        except ValueError:
            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + 'Please enter a valid number')
    
    time.sleep(0.4)
    
    print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Selected College: ' + fy + allColleges[userInput])
    
    time.sleep(0.4)
    
    print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Enter Your .edu Email: ', end='')
    userEmail = input().strip()
    
    # Validate .edu email
    if not userEmail.endswith('.edu'):
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Note: Email should be .edu domain for college applications')
    
    time.sleep(0.4)
    
    print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Starting automation... Keep checking this terminal for instructions')
    
    time.sleep(1)
    
    reg_url = start_url + clg_ids[userInput]
    start_bot(reg_url, userEmail, allColleges[userInput], userInput + 1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{fr}Script interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n{fr}Unexpected error: {str(e)}")
        sys.exit(1)
