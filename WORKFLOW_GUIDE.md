"""
═══════════════════════════════════════════════════════════════════════════════
                    🎓 EDUMAIL GENERATOR 2026 - COMPLETE WORKFLOW
═══════════════════════════════════════════════════════════════════════════════

COMPLETE STEP-BY-STEP WORK FLOW GUIDE
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 1: PREPARATION & INSTALLATION
# ═══════════════════════════════════════════════════════════════════════════════

"""
STEP 1: VERIFY PYTHON INSTALLATION
───────────────────────────────────────────────────────────────────────────────

Command:
    python --version

Expected Output:
    Python 3.11.0  (or 3.7+)

If Python not installed:
    Windows: Download from https://www.python.org/downloads/
    macOS:   brew install python@3.11
    Linux:   sudo apt install python3.11
"""

# ═══════════════════════════════════════════════════════════════════════════════

"""
STEP 2: CLONE REPOSITORY
───────────────────────────────────────────────────────────────────────────────

Command:
    git clone https://github.com/so9810102/EduMail-Generator-2026.git
    cd EduMail-Generator-2026

Expected Output:
    Cloning into 'EduMail-Generator-2026'...
    remote: Enumerating objects: XX, done.
    ...
    
Directory Structure Created:
    EduMail-Generator-2026/
    ├── bot.py                    ← Main script
    ├── setup.py                  ← Setup script
    ├── requirements.txt          ← Dependencies
    ├── README.md                 ← Documentation
    ├── __banner/
    │   └── myBanner.py          ← Terminal banner
    ├── __colors__/
    │   └── colors.py            ← Color codes
    ├── __constants/
    │   ├── const.py             ← Constants & data
    │   └── universities.py      ← Universities database
    └── __dwnldDrivers/
        └── versions.py          ← WebDriver management
"""

# ═══════════════════════════════════════════════════════════════════════════════

"""
STEP 3: RUN SETUP SCRIPT
───────────────────────────────────────────────────────────────────────────────

Command:
    python setup.py

What This Does:
    ✓ Installs all required Python packages
    ✓ Detects installed browsers (Chrome/Firefox)
    ✓ Asks you to select preferred browser
    ✓ Saves browser preference to prefBrowser.txt
    ✓ Downloads WebDriver automatically

Package Installation Details:
    - requests>=2.28.0           (HTTP library)
    - faker>=8.0.0               (Fake data generation)
    - selenium>=4.0.0            (Browser automation)
    - colorama>=0.4.0            (Terminal colors)
    - webdriver-manager>=4.0.0   (WebDriver management)

Setup Output:
    ═════════════════════════════════════════════
      EduMail Generator 2026 - Setup
    ═════════════════════════════════════════════
    
    [*] Installing Required Packages
    [*] Installing requests... ✓ Done
    [*] Installing faker... ✓ Done
    [*] Installing selenium... ✓ Done
    [*] Installing colorama... ✓ Done
    [*] Installing webdriver-manager... ✓ Done
    
    [*] Detecting Installed Browsers
    [*] Checking Firefox... Found (v121.0)
    [*] Checking Chrome... Found (v120.0)
    
    [*] Select Your Preferred Browser:
    ═════════════════════════════════════════════
    [*] 1. Firefox
    [*] 2. Chrome
    
    [*] Enter browser number (e.g., 1 or 2): 2
    ✓ Selected: Chrome
    
    [*] Saving browser preference... ✓ Done
    ═════════════════════════════════════════════
    [*] Setup Completed Successfully!
    [*] You can now run: python bot.py
    ═════════════════════════════════════════════
    
Files Created After Setup:
    - prefBrowser.txt  (Contains: chrome or firefox)
    - WebDriver cache  (~200MB per browser)
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 2: RUNNING THE BOT
# ═══════════════════════════════════════════════════════════════════════════════

"""
STEP 4: RUN THE BOT
───────────────────────────────────────────────────────────────────────────────

Command:
    python bot.py

Initial Output (Banner):
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║         _____    _ _   __  __       _ _    ____              ║
    ║        | ____|__| | |_   |  \/  | __ _(_) |  / ___| ___ _ __  ║
    ║        |  _| / _` | | | | | \/| |/ _` | | | | |  _ / _ \ '_ \ ║
    ║        | |__| (_| | |_| | | |  | | (_| | | | | |_| |  __/ | | |║
    ║        |_____\__,_|\__,_| |_|  |_|\__,_|_|_|  \____|\____|_| |_║
    ║                                                              ║
    ║                2026 Edition - Selenium 4.x Compatible        ║
    ║             Advanced College Application Automation          ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
"""

# ═══════════════════════════════════════════════════════════════════════════════

"""
STEP 5: SELECT UNIVERSITY/COLLEGE
───────────────────────────────────────────────────────────────────────────────

Output:
    [*] Select a University/College to generate student account...
    
    [*] 1. Harvard University (harvard.edu)
    [*] 2. MIT (Massachusetts Institute of Technology) (mit.edu)
    [*] 3. Stanford University (stanford.edu)
    [*] 4. University of Oxford (ox.ac.uk)
    [*] 5. University of Cambridge (cam.ac.uk)
    [*] 6. University of Toronto (utoronto.ca)
    [*] 7. University of Melbourne (unimelb.edu.au)
    [*] 8. Bangladesh University of Engineering and Technology (buet.ac.bd)
    [*] 9. University of Dhaka (du.ac.bd)
    [*] 10. North South University (northsouth.edu)
    
    [*] Enter university number (1-10): 

User Action:
    ➤ Type: 1 (or any number 1-10)
    ➤ Press: ENTER

Output After Selection:
    [*] Selected: Harvard University
"""

# ═══════════════════════════════════════════════════════════════════════════════

"""
STEP 6: ACCOUNT GENERATION IN PROGRESS
───────────────────────────────────────────────────────────────────────────────

Output:
    [*] Generating student account...
    
Behind the Scenes:
    ✓ Generates fake student name
    ✓ Generates realistic email: john1234567@harvard.edu
    ✓ Generates phone number: 408-555-1234
    ✓ Generates birth date: 07/15/2000
    ✓ Selects random department: Engineering
    ✓ Selects random campus: Main Campus
    ✓ Generates student ID: STU456789
    ✓ Generates admission number: ADM654321
    ✓ Formats all information beautifully
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 3: ACCOUNT INFORMATION DISPLAY
# ═══════════════════════════════════════════════════════════════════════════════

"""
STEP 7: BEAUTIFUL ACCOUNT INFORMATION DISPLAY
───────────────────────────────────────────────────────────────────────────────

Output Format:

    ════════════════════════════════════════════════════════════════
                    🎓 STUDENT ACCOUNT INFORMATION
    ════════════════════════════════════════════════════════════════
    
    🔐 ACCOUNT INFORMATION
    ──────────────────────────────────────────────────────────────
    Student Email      : john1234567@harvard.edu
    Username           : john7654321
    Password           : [Auto-generated]
    Account Status     : Active ✓
    
    👤 PERSONAL INFORMATION
    ──────────────────────────────────────────────────────────────
    First Name         : John
    Middle Name        : A
    Last Name          : Doe
    Full Name          : John A Doe
    Gender             : Male
    Birth Date         : 07/15/2000
    Nationality        : American
    Country            : United States 🌍
    
    📞 CONTACT INFORMATION
    ──────────────────────────────────────────────────────────────
    Phone              : 408-555-1234
    Alt. Phone         : 415-333-5678
    Personal Email     : john.doe@gmail.com
    
    🏠 ADDRESS INFORMATION
    ──────────────────────────────────────────────────────────────
    Country            : United States
    State/Province     : Massachusetts
    City               : Cambridge
    Postal/ZIP Code    : 02138
    Street Address     : 123 Main Street
    
    🎓 EDUCATIONAL INFORMATION
    ──────────────────────────────────────────────────────────────
    University/College : Harvard University
    Email Domain       : harvard.edu
    Campus             : Main Campus
    Department         : Engineering
    Program/Course     : Engineering Program
    Degree Level       : Master's
    Academic Year      : 2026
    Semester           : Fall
    Session            : 2026–2027
    
    🆔 STUDENT IDENTIFICATION
    ──────────────────────────────────────────────────────────────
    Student ID         : STU456789
    Registration No    : 45678
    Roll Number        : 78901
    Admission Number   : ADM654321
    
    📅 ACCOUNT DETAILS
    ──────────────────────────────────────────────────────────────
    Account Created    : 09/11/2026
    Expected Grad.     : 05/2028
    
    ════════════════════════════════════════════════════════════════
    
    ✓ Account saved to: student_account_1694432400.txt
    ✓ Student account generated successfully!
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 4: DATA STORAGE
# ═══════════════════════════════════════════════════════════════════════════════

"""
STEP 8: DATA SAVED TO FILE
───────────────────────────────────────────────────────────────────────────────

File Location:
    student_account_TIMESTAMP.txt
    Example: student_account_1694432400.txt

File Contents:
    (Same as displayed in console - plain text format)

File Storage Location:
    C:\Users\USERNAME\EduMail-Generator-2026\  (Windows)
    /Users/USERNAME/EduMail-Generator-2026/     (macOS)
    /home/username/EduMail-Generator-2026/      (Linux)

Multiple Runs:
    Each run creates a NEW file with unique timestamp
    All previous accounts are preserved
    No data is overwritten
"""

# ═══════════════════════════════════════════════════════════════════════════════
# COMPLETE WORKFLOW SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════

"""
🎯 COMPLETE WORKFLOW AT A GLANCE
═══════════════════════════════════════════════════════════════════════════════

START
  ↓
[STEP 1] Verify Python 3.7+
  ├─ Command: python --version
  └─ Expected: Python 3.7+
  ↓
[STEP 2] Clone Repository
  ├─ Command: git clone https://github.com/so9810102/EduMail-Generator-2026.git
  └─ Creates: Project folder with all files
  ↓
[STEP 3] Navigate to Project
  ├─ Command: cd EduMail-Generator-2026
  └─ Current Directory: Project root
  ↓
[STEP 4] Run Setup Script (ONE-TIME ONLY)
  ├─ Command: python setup.py
  ├─ Installs: All Python packages
  ├─ Detects: Chrome/Firefox browser
  ├─ Asks: Select browser preference
  └─ Creates: prefBrowser.txt, WebDriver cache
  ↓
[STEP 5] Run Bot Script (MAIN)
  ├─ Command: python bot.py
  └─ Displays: Banner & University list
  ↓
[STEP 6] Select University (USER INPUT)
  ├─ Prompt: "Enter university number (1-10):"
  ├─ User: Types 1-10 and presses ENTER
  └─ System: Validates input
  ↓
[STEP 7] Generate Student Account (AUTO)
  ├─ Generates: Realistic student data
  ├─ Creates: Student email with correct domain
  ├─ Generates: Phone, ID, address, etc.
  └─ System: Formats all information beautifully
  ↓
[STEP 8] Display Account Information (OUTPUT)
  ├─ Console: Shows all account details
  ├─ Colors: Formatted with ANSI colors
  ├─ File: Saves to student_account_TIMESTAMP.txt
  └─ Success: Prints completion message
  ↓
END
  ↓
[REPEAT] Run "python bot.py" again for another account
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# QUICK REFERENCE COMMANDS
# ═══════════════════════════════════════════════════════════════════════════════

"""
📋 QUICK REFERENCE - ALL COMMANDS
═══════════════════════════════════════════════════════════════════════════════

FIRST TIME SETUP (Run Once):
    python setup.py

GENERATE STUDENT ACCOUNTS (Run Multiple Times):
    python bot.py

UPDATE FROM GITHUB:
    git pull origin main

REINSTALL PACKAGES:
    pip install -r requirements.txt

CHECK PYTHON VERSION:
    python --version

VIEW GENERATED ACCOUNTS:
    student_account_*.txt  (Open with any text editor)

DELETE OLD ACCOUNTS:
    rm student_account_*.txt  (macOS/Linux)
    del student_account_*.txt (Windows CMD)
    Remove-Item student_account_*.txt (Windows PowerShell)

TROUBLESHOOTING:
    If setup fails:
        python setup.py
    
    If bot.py fails:
        python setup.py
        python bot.py
    
    If packages missing:
        pip install faker selenium webdriver-manager colorama requests
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SUPPORTED UNIVERSITIES (10 TOTAL)
# ═══════════════════════════════════════════════════════════════════════════════

"""
📚 SUPPORTED UNIVERSITIES & COLLEGES
═══════���═══════════════════════════════════════════════════════════════════════

1. HARVARD UNIVERSITY
   Domain: harvard.edu
   Country: United States
   Departments: Engineering, Business, Medicine, Law, Arts & Sciences
   
2. MIT (MASSACHUSETTS INSTITUTE OF TECHNOLOGY)
   Domain: mit.edu
   Country: United States
   Departments: Engineering, Science, Management, Architecture
   
3. STANFORD UNIVERSITY
   Domain: stanford.edu
   Country: United States
   Departments: Engineering, Business, Medicine, Law, Humanities
   
4. UNIVERSITY OF OXFORD
   Domain: ox.ac.uk
   Country: United Kingdom
   Departments: Engineering, Medicine, Law, Science, Humanities
   
5. UNIVERSITY OF CAMBRIDGE
   Domain: cam.ac.uk
   Country: United Kingdom
   Departments: Engineering, Science, Law, Medicine, Humanities
   
6. UNIVERSITY OF TORONTO
   Domain: utoronto.ca
   Country: Canada
   Departments: Engineering, Business, Medicine, Law
   
7. UNIVERSITY OF MELBOURNE
   Domain: unimelb.edu.au
   Country: Australia
   Departments: Engineering, Business, Law, Medicine, Science
   
8. BANGLADESH UNIVERSITY OF ENGINEERING AND TECHNOLOGY (BUET)
   Domain: buet.ac.bd
   Country: Bangladesh
   Departments: Civil, Electrical, Mechanical, Chemical Engineering
   
9. UNIVERSITY OF DHAKA
   Domain: du.ac.bd
   Country: Bangladesh
   Departments: Science, Arts, Engineering, Business, Law
   
10. NORTH SOUTH UNIVERSITY
    Domain: northsouth.edu
    Country: Bangladesh
    Departments: Engineering, Business, Humanities, Science
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# EMAIL DOMAIN FORMATS BY UNIVERSITY TYPE
# ═══════════════════════════════════════════════════════════════════════════════

"""
📧 EMAIL DOMAIN FORMATS SUPPORTED
═══════════════════════════════════════════════════════════════════════════════

United States Universities:
    Format: firstname + number @ .edu
    Example: john1234567@harvard.edu
    Example: mary5678901@mit.edu

United Kingdom Universities:
    Format: firstname + number @ .ac.uk
    Example: john1234567@ox.ac.uk
    Example: mary5678901@cam.ac.uk

Canadian Universities:
    Format: firstname + number @ .ca
    Example: john1234567@utoronto.ca

Australian Universities:
    Format: firstname + number @ .edu.au
    Example: john1234567@unimelb.edu.au

Bangladeshi Universities (.edu):
    Format: firstname + number @ .edu
    Example: john1234567@northsouth.edu

Bangladeshi Universities (.ac.bd):
    Format: firstname + number @ .ac.bd
    Example: john1234567@du.ac.bd

Bangladeshi Universities (.edu.bd):
    Format: firstname + number @ .edu.bd
    Example: john1234567@buet.edu.bd
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# GENERATED DATA FIELDS
# ═══════════════════════════════════════════════════════════════════════════════

"""
📊 AUTO-GENERATED DATA FIELDS
═══════════════════════════════════════════════════════════════════════════════

ACCOUNT INFORMATION:
    ✓ Student Email (with university-specific domain)
    ✓ Username (FirstName + 7 random digits)
    ✓ Password (Auto-generated)
    ✓ Account Status (Always: Active)

PERSONAL INFORMATION:
    ✓ First Name (From Faker)
    ✓ Middle Name (Random letter A-Z)
    ✓ Last Name (From Faker)
    ✓ Full Name (Combination)
    ✓ Gender (Random: Male/Female/Other)
    ✓ Birth Date (Random: 1996-2005)
    ✓ Nationality (Random from list)
    ✓ Country (Based on selected university)

CONTACT INFORMATION:
    ✓ Phone (XXX-XXX-XXXX format)
    ✓ Alternative Phone (XXX-XXX-XXXX format)
    ✓ Personal Email (Gmail/Yahoo from Faker)

ADDRESS INFORMATION:
    ✓ Country (From university)
    ✓ State/Province (From university)
    ✓ City (From university)
    ✓ Postal/ZIP Code (Random based on country)
    ✓ Street Address (From Faker)

EDUCATIONAL INFORMATION:
    ✓ University/College Name
    ✓ Email Domain (Correct for university)
    ✓ Campus (Random from list)
    ✓ Department (Random from university list)
    ✓ Program/Course (Department + " Program")
    ✓ Degree Level (Bachelor's/Master's/PhD)
    ✓ Academic Year (2026)
    ✓ Semester (Fall/Spring/Summer)
    ✓ Session (2026–2027)

STUDENT IDENTIFICATION:
    ✓ Student ID (STU + 6 random digits)
    ✓ Registration Number (5 random digits)
    ✓ Roll Number (5 random digits)
    ✓ Admission Number (ADM + 6 random digits)

ACCOUNT DETAILS:
    ✓ Account Created (Current date: MM/DD/YYYY)
    ✓ Expected Graduation (05/2028)
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# FILE OUTPUT EXAMPLES
# ═══════════════════════════════════════════════════════════════════════════════

"""
📁 OUTPUT FILE EXAMPLE
═══════════════════════════════════════════════════════════════════════════════

Filename: student_account_1694432400.txt
Location: C:\Users\SOFIKUL\EduMail-Generator-2026\

Contents (plain text):
───────────────────────────────────────────────────────────────────────────────
============================================================
          🎓 STUDENT ACCOUNT INFORMATION
============================================================

🔐 ACCOUNT INFORMATION
────────────────────────────────────────────────────────────
Student Email      : john1234567@harvard.edu
Username           : john7654321
Password           : [Auto-generated]
Account Status     : Active ✓

👤 PERSONAL INFORMATION
────────────────────────────────────────────────────────────
First Name         : John
Middle Name        : A
Last Name          : Doe
Full Name          : John A Doe
Gender             : Male
Birth Date         : 07/15/2000
Nationality        : American
Country            : United States

📞 CONTACT INFORMATION
────────────────────────────────────────────────────────────
Phone              : 408-555-1234
Alt. Phone         : 415-333-5678
Personal Email     : john.doe@gmail.com

🏠 ADDRESS INFORMATION
────────────────────────────────────────────────────────────
Country            : United States
State/Province     : Massachusetts
City               : Cambridge
Postal/ZIP Code    : 02138
Street Address     : 123 Main Street

🎓 EDUCATIONAL INFORMATION
────────────────────────────────────────────────────────────
University/College : Harvard University
Email Domain       : harvard.edu
Campus             : Main Campus
Department         : Engineering
Program/Course     : Engineering Program
Degree Level       : Master's
Academic Year      : 2026
Semester           : Fall
Session            : 2026–2027

🆔 STUDENT IDENTIFICATION
────────────────────────────────────────────────────────────
Student ID         : STU456789
Registration No    : 45678
Roll Number        : 78901
Admission Number   : ADM654321

📅 ACCOUNT DETAILS
────────────────────────────────────────────────────────────
Account Created    : 09/11/2026
Expected Grad.     : 05/2028
───────────────────────────────────────────────────────────────────────────────
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DIRECTORY STRUCTURE AFTER COMPLETION
# ═══════════════════════════════════════════════════════════════════════════════

"""
📂 FINAL DIRECTORY STRUCTURE
═══════════════════════════════════════════════════════════════════════════════

EduMail-Generator-2026/
│
├── bot.py                          ← Main script (RUNNABLE)
├── setup.py                        ← Setup script (ONE-TIME USE)
├── requirements.txt                ← Python dependencies
├── README.md                       ← Documentation
├── prefBrowser.txt                 ← Browser preference (auto-created)
│
├── student_account_1694432400.txt  ← Generated account 1
├── student_account_1694432500.txt  ← Generated account 2
├── student_account_1694432600.txt  ← Generated account 3
│   ... (more accounts from multiple runs)
│
├── __banner/
│   ├── __init__.py
│   └── myBanner.py                 ← ASCII art banner
│
├── __colors__/
│   ├── __init__.py
│   └── colors.py                   ← ANSI color codes
│
├── __constants/
│   ├── __init__.py
│   ├── const.py                    ← Main constants
│   └── universities.py             ← Universities database
│
└── __dwnldDrivers/
    ├── __init__.py
    └── versions.py                 ← WebDriver management
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# TROUBLESHOOTING GUIDE
# ═══════════════════════════════════════════════════════════════════════════════

"""
🔧 TROUBLESHOOTING GUIDE
═══════════════════════════════════════════════════════════════════════════════

PROBLEM 1: "Python not found"
SOLUTION:
    1. Install Python 3.7+ from python.org
    2. Add Python to PATH (Windows)
    3. Use python3 instead of python (macOS/Linux)
    
PROBLEM 2: "ModuleNotFoundError: No module named 'faker'"
SOLUTION:
    1. Run: python setup.py
    2. Or: pip install faker
    
PROBLEM 3: "prefBrowser.txt not found"
SOLUTION:
    1. Run: python setup.py
    2. Select browser (Chrome/Firefox)
    
PROBLEM 4: "No browsers detected"
SOLUTION:
    1. Install Chrome: https://www.google.com/chrome/
    2. Or Install Firefox: https://www.mozilla.org/firefox/
    3. Run: python setup.py
    
PROBLEM 5: "Bot.py crashes or closes immediately"
SOLUTION:
    1. Run: python setup.py (Again)
    2. Check Python version: python --version
    3. Clear and reinstall: pip install --upgrade faker
    
PROBLEM 6: "Generated accounts not saving"
SOLUTION:
    1. Check folder permissions
    2. Ensure disk space available
    3. Run from a different location
═══════════════════════════════════════════════════════════════════════════════
"""

print(__doc__)
