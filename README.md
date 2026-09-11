# 🎓 EduMail Generator 2026

**Advanced College Application Form Automation** — Fully compatible with Python 3.11+ and Selenium 4.x

> ⚠️ **DISCLAIMER**: This tool is for **educational purposes only**. Use at your own risk. The authors are not responsible for any misuse or damage caused by this application.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [What's New in 2026](#whats-new-in-2026)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## 🎯 Overview

**EduMail Generator 2026** is an automated college application form filling system that uses Selenium WebDriver to interact with web-based college registration portals. It automates:

- ✅ Account creation (3-page form)
- ✅ Application form submission (8-page form)
- ✅ Personal information entry
- ✅ Education history
- ✅ Demographics and preferences
- ✅ Application submission

### Use Cases
- Batch testing college portals
- Integration testing for educational institutions
- Form validation automation
- Load testing college registration systems

---

## ⭐ Key Features

### 🤖 Fully Automated Workflow
- Automatically fills college application forms
- Handles multi-page forms seamlessly
- Generates realistic fake student data
- Validates and retries failed fields

### 🌐 Multi-Browser Support
- Chrome browser automation
- Firefox browser automation
- Automatic WebDriver management (no manual downloads needed)

### 🔐 Advanced Form Handling
- Handles dropdown selections
- Manages radio buttons and checkboxes
- Fills text inputs with realistic data
- Handles address validation and corrections
- Processes security questions
- CAPTCHA waiting mechanism

### 📊 Data Generation
- Random phone number generation
- Realistic name generation (via Faker)
- Address parsing and formatting
- Birth date generation

### 🎨 User-Friendly Interface
- Colored terminal output
- Progress indicators
- Detailed logging
- Interactive college selection

---

## 🆕 What's New in 2026

### Major Updates from Original Version

#### 1️⃣ **Selenium 4.x API Migration**
```python
# OLD (Selenium 3.x) - DEPRECATED
driver.find_element_by_id(\"id\")
driver.find_element_by_xpath(\"xpath\")
driver.find_element_by_class_name(\"class\")

# NEW (Selenium 4.x) - CURRENT STANDARD
from selenium.webdriver.common.by import By
driver.find_element(By.ID, \"id\")
driver.find_element(By.XPATH, \"xpath\")
driver.find_element(By.CLASS_NAME, \"class\")
```

#### 2️⃣ **Automatic WebDriver Management**
**Problem (2024)**: `chromedriver.storage.googleapis.com` was **shut down**, breaking manual driver management.

**Solution (2026)**: Using `webdriver-manager` for automatic driver detection and download.

#### 3️⃣ **Python 3.11+ Compatibility**
- All code follows Python 3.11+ standards
- No deprecated libraries
- Cross-platform support

#### 4️⃣ **Cross-Platform WebDriver Support**
- ✅ Windows (32/64-bit)
- ✅ macOS (Intel/Apple Silicon)
- ✅ Linux (all distributions)

---

## 💻 System Requirements

### Minimum Requirements
- **Python**: 3.7+ (Tested on 3.11+)
- **OS**: Windows, macOS, or Linux
- **RAM**: 2GB minimum
- **Disk Space**: 500MB (including WebDriver cache)
- **Internet**: Required for driver downloads

### Browser Requirements
- **Chrome**: v90+ installed
- **Firefox**: v88+ installed

### Python Packages
```
selenium>=4.0.0
webdriver-manager>=4.0.0
faker>=8.0.0
requests>=2.28.0
colorama>=0.4.0
```

---

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/mywebsidedata/EduMail-Generator-2026.git
cd EduMail-Generator-2026
```

### Step 2: Verify Python Version
```bash
python --version
# Should output: Python 3.7+ (preferably 3.11+)
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Setup

### Run Setup Script
```bash
python setup.py
```

This script will:
1. ✅ Install all required Python packages
2. ✅ Detect installed browsers (Chrome/Firefox)
3. ✅ Ask you to select your preferred browser
4. ✅ Save preferences to `prefBrowser.txt`

---

## 🎮 Usage

### Basic Usage
```bash
python bot.py
```

### Interactive Flow
```
[*] Select a college from all available colleges to proceed....

[*] 1 - College of Science & Engineering
[*] 2 - College of Liberal Arts
[*] 3 - College of Business Administration
[*] 4 - College of Medicine & Health Sciences

[*] Enter college id for ex - 1 or 2 or 3.... : 1

[*] Selected College: College of Science & Engineering

[*] Enter Your Email: student@example.com

[*] Hold on Starting now, Keep checking this terminal for instructions
```

---

## 📁 Project Structure

```
EduMail-Generator-2026/
├── bot.py                          # Main bot script
├── setup.py                        # Setup and configuration script
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── prefBrowser.txt                 # Browser preference (auto-generated)
├── myccAcc.txt                     # Account details (auto-generated)
│
├── __banner/                       # Terminal banner
│   └── myBanner.py                # Banner display
│
├── __colors__/                     # Terminal color codes
│   └── colors.py                  # Color constants for output
│
├── __constants/                    # Constants and configuration
│   └── const.py                   # College info, student data, URLs
│
└── __dwnldDrivers/                 # WebDriver management
    └── versions.py                # Browser detection & driver setup
```

---

## ⚙️ Configuration

### Modify College Information
Edit `__constants/const.py`:
```python
allColleges = [
    \"College A\",
    \"College B\",
    \"College C\",
    \"College D\"
]

clg_ids = [
    \"?clg=1\",
    \"?clg=2\",
    \"?clg=3\",
    \"?clg=4\"
]

start_url = \"https://your-college-portal.com/register\"
```

---

## 🐛 Troubleshooting

### Problem: \"No WebDriver found\"
**Solution**: Run `setup.py` again
```bash
python setup.py
```

### Problem: \"Browser not found\"
**Solution**: Install Chrome or Firefox, then run setup
```bash
# On Ubuntu
sudo apt-get install chromium-browser
# or
sudo apt-get install firefox

# On macOS
brew install google-chrome
# or
brew install firefox
```

### Problem: \"Selenium import error\"
**Solution**: Reinstall Selenium
```bash
pip install --upgrade selenium>=4.0.0
```

### Problem: \"prefBrowser.txt not found\"
**Solution**: Run setup script first
```bash
python setup.py
```

---

## 📝 Important Notes

### Legal & Ethical
- ⚠️ Only use on **test environments** or with explicit permission
- ⚠️ Respect **terms of service** of college websites
- ⚠️ Do not use for actual college fraud
- ⚠️ This is for **educational testing purposes only**

### Performance
- Each college application takes **10-15 minutes**
- WebDriver downloads are cached (~200MB per browser)
- First run may take longer due to dependencies
- Subsequent runs are faster

---

## 📄 License

This project is provided **\"as-is\"** for educational purposes.

---

## ⚠️ Disclaimer

```
THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY.

THE AUTHORS AND CONTRIBUTORS ARE NOT RESPONSIBLE FOR:
- Misuse of this tool
- Violation of terms of service
- Any legal consequences
- Damage or data loss
- Academic dishonesty

USE AT YOUR OWN RISK AND WITH EXPLICIT PERMISSION FROM INSTITUTIONS.
```

---

## 🚀 Quick Start Checklist

- [ ] Clone repository
- [ ] Verify Python 3.7+
- [ ] Run `python setup.py`
- [ ] Select browser (Chrome/Firefox)
- [ ] Run `python bot.py`
- [ ] Select college (1-4)
- [ ] Enter email address
- [ ] Monitor terminal for instructions

---

**Last Updated**: September 2026  
**Owner**: mywebsidedata  
**Repository**: [EduMail-Generator-2026](https://github.com/mywebsidedata/EduMail-Generator-2026)
