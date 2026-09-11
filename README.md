# 🎓 EduMail Generator 2026

**Advanced Student Account Generator** — Fully compatible with Python 3.7+ and Selenium 4.x

> ⚠️ **DISCLAIMER**: This tool is for **educational purposes only**. Use at your own risk. The authors are not responsible for any misuse or damage caused by this application.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Recent Updates](#recent-updates)
- [License](#license)

---

## 🎯 Overview

**EduMail Generator 2026** is an automated student account generator that creates realistic fake student data with beautiful formatted output. It supports:

- ✅ 10+ Universities/Colleges worldwide
- ✅ Auto-generates realistic student data (Faker library)
- ✅ Beautiful account information display
- ✅ Multiple email domain support (.edu, .ac.bd, .ac.uk, .edu.au, .ca)
- ✅ Comprehensive student information generation
- ✅ File export with timestamp

### Use Cases
- Testing educational platforms
- Generating sample student data
- Database population for testing
- Educational demonstrations

---

## ⭐ Key Features

### 🤖 Fully Automated Workflow
- Automatically generates student accounts
- Generates realistic fake student data
- Validates and formats all fields
- Beautiful terminal output

### 🌐 Multi-University Support
- Harvard University (MIT, Stanford, etc.)
- UK Universities (Oxford, Cambridge)
- Canadian Universities (Toronto)
- Australian Universities (Melbourne)
- Bangladeshi Universities (BUET, Dhaka, North South)

### 📊 Data Generation
- Random phone number generation
- Realistic name generation (via Faker)
- Address parsing and formatting
- Birth date generation
- Student IDs, Roll numbers, Admission numbers

### 🎨 User-Friendly Interface
- Colored terminal output with ANSI codes
- Progress indicators
- Interactive university selection
- Detailed formatted output

---

## 💻 System Requirements

### Minimum Requirements
- **Python**: 3.7+ (Tested on 3.11+)
- **OS**: Windows, macOS, or Linux
- **RAM**: 2GB minimum
- **Disk Space**: 500MB
- **Internet**: Required for initial setup

### Python Packages
```
faker>=8.0.0
requests>=2.28.0
selenium>=4.0.0
colorama>=0.4.0
webdriver-manager>=4.0.0
```

---

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/so9810102/EduMail-Generator-2026.git
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
2. ✅ Create necessary directory structure
3. ✅ Test browser compatibility (if needed)

---

## 🎮 Usage

### Basic Usage
```bash
python bot.py
```

### Interactive Flow
```
════════════════════════════════════════════════════════════
              🎓 EduMail Generator 2026
════════════════════════════════════════════════════════════

[*] Select a University/College to generate student account...

[*] 1. Harvard University (harvard.edu)
[*] 2. MIT (mit.edu)
[*] 3. Stanford University (stanford.edu)
[*] 4. University of Oxford (ox.ac.uk)
[*] 5. University of Cambridge (cam.ac.uk)
[*] 6. University of Toronto (utoronto.ca)
[*] 7. University of Melbourne (unimelb.edu.au)
[*] 8. BUET (buet.ac.bd)
[*] 9. University of Dhaka (du.ac.bd)
[*] 10. North South University (northsouth.edu)

[*] Enter university number (1-10): 3

[*] Selected: Stanford University

[*] Generating student account...

════════════════════════════════════════════════════════════
              🎓 STUDENT ACCOUNT INFORMATION
════════════════════════════════════════════════════════════

🔐 ACCOUNT INFORMATION
────────────────────────────────────────────────────────────
Student Email      : john1234@stanford.edu
Username           : john1234567890
Password           : [Auto-generated]
Account Status     : Active ✓

[... More account details ...]

✓ Account saved to: student_account_1694520000.txt
```

---

## 📁 Project Structure

```
EduMail-Generator-2026/
├── bot.py                          # Main bot script
├── setup.py                        # Setup and configuration script
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation (this file)
│
├── __banner/                       # Terminal banner display
│   ├── __init__.py                # Module initialization
│   └── myBanner.py                # Banner display functions
│
├── __colors__/                     # Terminal color codes
│   ├── __init__.py                # Module initialization
│   └── colors.py                  # ANSI color definitions
│
├── __constants/                    # Constants and configuration
│   ├── __init__.py                # Module initialization
│   └── const.py                   # Universities, student data, constants
│
└── __dwnldDrivers/                 # WebDriver management (legacy)
    ├── __init__.py                # Module initialization
    └── versions.py                # Browser version detection
```

---

## ⚙️ Configuration

### Add or Modify Universities
Edit `__constants/const.py` and add to `universities_db`:

```python
universities_db = {
    # Existing entries...
    11: {
        "name": "Your University Name",
        "domain": "youruniversity.edu",
        "country": "Country Name",
        "state": "State/Province",
        "city": "City Name",
        "departments": ["Department1", "Department2", "Department3"],
        "degrees": ["Bachelor's", "Master's", "PhD"],
    },
}
```

### Customize Colors
Edit `__colors__/colors.py` to change terminal colors:

```python
fc = '\033[36m'   # Foreground Cyan
fg = '\033[32m'   # Foreground Green
fr = '\033[31m'   # Foreground Red
# ... more colors
```

---

## 🐛 Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'faker'"
**Solution**: Install requirements
```bash
pip install -r requirements.txt
```

### Problem: "Import error from __constants"
**Solution**: Ensure you're running from repository root
```bash
cd EduMail-Generator-2026
python bot.py
```

### Problem: "No such file or directory: '__banner/myBanner.py'"
**Solution**: Check directory structure and run setup
```bash
python setup.py
```

---

## 📝 Recent Updates (September 2026)

### Fixed Issues
- ✅ **Color codes**: Fixed duplicate ANSI codes (fc, fb were same)
- ✅ **File consolidation**: Merged universities.py into const.py
- ✅ **Module exports**: Enhanced __init__.py files for better imports
- ✅ **Documentation**: Updated with all 10 universities

### Code Quality Improvements
- ✅ Better ANSI color definitions
- ✅ Comprehensive constants organization
- ✅ Enhanced module initialization
- ✅ Cleaner import structure

---

## 📄 License

This project is provided **"as-is"** for educational purposes only.

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
- [ ] Run `pip install -r requirements.txt`
- [ ] Run `python bot.py`
- [ ] Select university (1-10)
- [ ] View generated account
- [ ] Check student_account_*.txt file

---

## 📧 Support

For issues or questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the code comments
3. Ensure all dependencies are installed

---

**Last Updated**: September 11, 2026  
**Version**: 2.0 (Fixed & Enhanced)  
**Repository**: [EduMail-Generator-2026](https://github.com/so9810102/EduMail-Generator-2026)
