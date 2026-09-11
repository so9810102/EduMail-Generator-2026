"""
EduMail Generator 2026 - Advanced Student Account Generator
=========================================
Automates student account creation with beautiful formatted output

Key Features:
  - 10+ Universities/Colleges to choose from
  - Auto-generates realistic student data
  - Beautiful account information display
  - Multiple email domain support (.edu, .ac.bd, .ac.uk, .edu.au)
  - Comprehensive student information

Usage:
    python bot.py

Requires: Python 3.7+, faker
Last Updated: September 2026
"""

import time
import string
import random
import sys
from datetime import datetime

# Faker import
try:
    from faker import Faker
except ImportError:
    print("❌ Faker not installed. Run: pip install faker")
    sys.exit(1)

# Local imports
try:
    from __constants.const import (
        universities_db, CAMPUSES, SEMESTERS, GENDERS, 
        NATIONALITIES, country_codes, firstName, LastName, 
        studentAddress, randomMonth, randomDay, randomYear
    )
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
    """Generate a random n-digit number"""
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

def random_phone_num_generator():
    """Generate a random phone number in format: XXX-XXX-XXXX"""
    first = str(random.choice(country_codes))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    
    return '{}-{}-{}'.format(first, second, last)

def generate_student_id():
    """Generate a student ID"""
    return f"STU{random.randint(100000, 999999)}"

def generate_roll_number():
    """Generate a roll number"""
    return f"{random.randint(10000, 99999)}"

def generate_admission_number():
    """Generate an admission number"""
    return f"ADM{random.randint(100000, 999999)}"

def get_student_email(first_name, domain):
    """Generate student email based on domain"""
    username = f"{first_name.lower()}{postFix(4)}".replace(" ", "")
    
    if domain.endswith('.edu'):
        return f"{username}@{domain}"
    elif domain.endswith('.ac.bd') or domain.endswith('.edu.bd'):
        return f"{username}@{domain}"
    elif domain.endswith('.ac.uk'):
        return f"{username}@{domain}"
    elif domain.endswith('.edu.au'):
        return f"{username}@{domain}"
    elif domain.endswith('.ca'):
        return f"{username}@{domain}"
    else:
        return f"{username}@{domain}"

def display_student_account(university_data, student_data):
    """Display beautiful student account information"""
    
    print("\n")
    print(f"{fc}{sd}{'═'*60}")
    print(f"{fg}{'🎓 STUDENT ACCOUNT INFORMATION':^60}")
    print(f"{fc}{sd}{'═'*60}\n")
    
    # Account Information Section
    print(f"{fy}{'🔐 ACCOUNT INFORMATION':^60}")
    print(f"{fc}{sd}{'-'*60}")
    print(f"{fg}Student Email      {fc}:{fg} {student_data['email']}")
    print(f"{fg}Username           {fc}:{fg} {student_data['username']}")
    print(f"{fg}Password           {fc}:{fg} [Auto-generated]")
    print(f"{fg}Account Status     {fc}:{fg} Active ✓")
    
    # Personal Information Section
    print(f"\n{fy}{'👤 PERSONAL INFORMATION':^60}")
    print(f"{fc}{sd}{'-'*60}")
    print(f"{fg}First Name         {fc}:{fg} {student_data['first_name']}")
    print(f"{fg}Middle Name        {fc}:{fg} {student_data['middle_name']}")
    print(f"{fg}Last Name          {fc}:{fg} {student_data['last_name']}")
    print(f"{fg}Full Name          {fc}:{fg} {student_data['full_name']}")
    print(f"{fg}Gender             {fc}:{fg} {student_data['gender']}")
    print(f"{fg}Birth Date         {fc}:{fg} {student_data['birth_date']}")
    print(f"{fg}Nationality        {fc}:{fg} {student_data['nationality']}")
    print(f"{fg}Country            {fc}:{fg} {university_data['country']} 🌍")
    
    # Contact Information Section
    print(f"\n{fy}{'📞 CONTACT INFORMATION':^60}")
    print(f"{fc}{sd}{'-'*60}")
    print(f"{fg}Phone              {fc}:{fg} {student_data['phone']}")
    print(f"{fg}Alt. Phone         {fc}:{fg} {student_data['alt_phone']}")
    print(f"{fg}Personal Email     {fc}:{fg} {student_data['personal_email']}")
    
    # Address Information Section
    print(f"\n{fy}{'🏠 ADDRESS INFORMATION':^60}")
    print(f"{fc}{sd}{'-'*60}")
    print(f"{fg}Country            {fc}:{fg} {university_data['country']}")
    print(f"{fg}State/Province     {fc}:{fg} {university_data['state']}")
    print(f"{fg}City               {fc}:{fg} {university_data['city']}")
    print(f"{fg}Postal/ZIP Code    {fc}:{fg} {student_data['postal_code']}")
    print(f"{fg}Street Address     {fc}:{fg} {student_data['street_address']}")
    
    # Educational Information Section
    print(f"\n{fy}{'🎓 EDUCATIONAL INFORMATION':^60}")
    print(f"{fc}{sd}{'-'*60}")
    print(f"{fg}University/College {fc}:{fg} {university_data['name']}")
    print(f"{fg}Email Domain       {fc}:{fg} {university_data['domain']}")
    print(f"{fg}Campus             {fc}:{fg} {student_data['campus']}")
    print(f"{fg}Department         {fc}:{fg} {student_data['department']}")
    print(f"{fg}Program/Course     {fc}:{fg} {student_data['program']}")
    print(f"{fg}Degree Level       {fc}:{fg} {student_data['degree']}")
    print(f"{fg}Academic Year      {fc}:{fg} {student_data['academic_year']}")
    print(f"{fg}Semester           {fc}:{fg} {student_data['semester']}")
    print(f"{fg}Session            {fc}:{fg} {student_data['session']}")
    
    # Student Identification Section
    print(f"\n{fy}{'🆔 STUDENT IDENTIFICATION':^60}")
    print(f"{fc}{sd}{'-'*60}")
    print(f"{fg}Student ID         {fc}:{fg} {student_data['student_id']}")
    print(f"{fg}Registration No    {fc}:{fg} {student_data['registration_no']}")
    print(f"{fg}Roll Number        {fc}:{fg} {student_data['roll_no']}")
    print(f"{fg}Admission Number   {fc}:{fg} {student_data['admission_no']}")
    
    # Account Details Section
    print(f"\n{fy}{'📅 ACCOUNT DETAILS':^60}")
    print(f"{fc}{sd}{'-'*60}")
    print(f"{fg}Account Created    {fc}:{fg} {student_data['created_date']}")
    print(f"{fg}Expected Grad.     {fc}:{fg} {student_data['graduation_date']}")
    
    print(f"\n{fc}{sd}{'═'*60}\n")
    
    # Save to file
    save_to_file(student_data, university_data)

def save_to_file(student_data, university_data):
    """Save student account information to file"""
    
    filename = f"student_account_{int(time.time())}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("          🎓 STUDENT ACCOUNT INFORMATION\n")
        f.write("=" * 60 + "\n\n")
        
        f.write("🔐 ACCOUNT INFORMATION\n")
        f.write("-" * 60 + "\n")
        f.write(f"Student Email      : {student_data['email']}\n")
        f.write(f"Username           : {student_data['username']}\n")
        f.write(f"Password           : [Auto-generated]\n")
        f.write(f"Account Status     : Active ✓\n\n")
        
        f.write("👤 PERSONAL INFORMATION\n")
        f.write("-" * 60 + "\n")
        f.write(f"First Name         : {student_data['first_name']}\n")
        f.write(f"Middle Name        : {student_data['middle_name']}\n")
        f.write(f"Last Name          : {student_data['last_name']}\n")
        f.write(f"Full Name          : {student_data['full_name']}\n")
        f.write(f"Gender             : {student_data['gender']}\n")
        f.write(f"Birth Date         : {student_data['birth_date']}\n")
        f.write(f"Nationality        : {student_data['nationality']}\n")
        f.write(f"Country            : {university_data['country']}\n\n")
        
        f.write("📞 CONTACT INFORMATION\n")
        f.write("-" * 60 + "\n")
        f.write(f"Phone              : {student_data['phone']}\n")
        f.write(f"Alt. Phone         : {student_data['alt_phone']}\n")
        f.write(f"Personal Email     : {student_data['personal_email']}\n\n")
        
        f.write("🏠 ADDRESS INFORMATION\n")
        f.write("-" * 60 + "\n")
        f.write(f"Country            : {university_data['country']}\n")
        f.write(f"State/Province     : {university_data['state']}\n")
        f.write(f"City               : {university_data['city']}\n")
        f.write(f"Postal/ZIP Code    : {student_data['postal_code']}\n")
        f.write(f"Street Address     : {student_data['street_address']}\n\n")
        
        f.write("🎓 EDUCATIONAL INFORMATION\n")
        f.write("-" * 60 + "\n")
        f.write(f"University/College : {university_data['name']}\n")
        f.write(f"Email Domain       : {university_data['domain']}\n")
        f.write(f"Campus             : {student_data['campus']}\n")
        f.write(f"Department         : {student_data['department']}\n")
        f.write(f"Program/Course     : {student_data['program']}\n")
        f.write(f"Degree Level       : {student_data['degree']}\n")
        f.write(f"Academic Year      : {student_data['academic_year']}\n")
        f.write(f"Semester           : {student_data['semester']}\n")
        f.write(f"Session            : {student_data['session']}\n\n")
        
        f.write("🆔 STUDENT IDENTIFICATION\n")
        f.write("-" * 60 + "\n")
        f.write(f"Student ID         : {student_data['student_id']}\n")
        f.write(f"Registration No    : {student_data['registration_no']}\n")
        f.write(f"Roll Number        : {student_data['roll_no']}\n")
        f.write(f"Admission Number   : {student_data['admission_no']}\n\n")
        
        f.write("📅 ACCOUNT DETAILS\n")
        f.write("-" * 60 + "\n")
        f.write(f"Account Created    : {student_data['created_date']}\n")
        f.write(f"Expected Grad.     : {student_data['graduation_date']}\n")
    
    print(f"{fg}✓ Account saved to: {filename}")

def generate_student_data(university_data):
    """Generate complete student data"""
    
    fake = Faker('en_US')
    
    # Parse address
    ex_split = studentAddress.split(", ")
    street_address = ex_split[0] if len(ex_split) > 0 else "123 Main St"
    
    # Postal code based on country
    if university_data['country'] == 'United States':
        postal_code = str(random.randint(10000, 99999))
    elif university_data['country'] == 'Bangladesh':
        postal_code = str(random.randint(1000, 9999))
    else:
        postal_code = str(random.randint(100000, 999999))
    
    middle_initial = random.choice(string.ascii_uppercase)
    
    student_data = {
        'first_name': firstName,
        'middle_name': middle_initial,
        'last_name': LastName,
        'full_name': f"{firstName} {middle_initial} {LastName}",
        'email': get_student_email(firstName, university_data['domain']),
        'username': f"{firstName.lower()}{postFix(7)}",
        'phone': random_phone_num_generator(),
        'alt_phone': random_phone_num_generator(),
        'personal_email': fake.email(),
        'gender': random.choice(GENDERS),
        'birth_date': f"{randomMonth:02d}/{randomDay:02d}/{randomYear}",
        'nationality': random.choice(NATIONALITIES),
        'street_address': street_address,
        'postal_code': postal_code,
        'campus': random.choice(CAMPUSES),
        'department': random.choice(university_data['departments']),
        'program': f"{random.choice(university_data['departments'])} Program",
        'degree': random.choice(university_data['degrees']),
        'academic_year': '2026',
        'semester': random.choice(SEMESTERS),
        'session': '2026–2027',
        'student_id': generate_student_id(),
        'registration_no': generate_roll_number(),
        'roll_no': generate_roll_number(),
        'admission_no': generate_admission_number(),
        'created_date': datetime.now().strftime("%m/%d/%Y"),
        'graduation_date': "05/2028",
    }
    
    return student_data

def main():
    """Main function"""
    
    # Display banner
    try:
        sys.stdout.write(bannerTop())
    except:
        print("\n" + "="*60)
        print("  EduMail Generator 2026 - Student Account Generator")
        print("="*60 + "\n")
    
    # Display universities list
    print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fg}Select a University/College to generate student account...\n")
    
    time.sleep(0.5)
    
    # Sort universities by key
    sorted_unis = sorted(universities_db.items())
    
    for key, university in sorted_unis:
        print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fy}{key}. {university['name']} ({university['domain']})")
    
    # Get user selection
    is_error = True
    selected_university = None
    
    while is_error:
        print(f'\n{fc}{sd}[{fm}{sb}*{fc}{sd}] {fg}Enter university number (1-10): ', end='')
        
        try:
            user_input = int(input())
            
            if user_input not in universities_db:
                print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fr}Invalid selection")
            else:
                selected_university = universities_db[user_input]
                is_error = False
                
        except ValueError:
            print(f"{fc}{sd}[{fm}{sb}*{fc}{sd}] {fr}Please enter a valid number")
    
    time.sleep(0.5)
    
    print(f'\n{fc}{sd}[{fm}{sb}*{fc}{sd}] {fg}Selected: {fy}{selected_university["name"]}')
    
    time.sleep(0.5)
    
    print(f'\n{fc}{sd}[{fm}{sb}*{fc}{sd}] {fg}Generating student account...')
    
    time.sleep(1)
    
    # Generate student data
    student_data = generate_student_data(selected_university)
    
    # Display account information
    display_student_account(selected_university, student_data)
    
    print(f"{fg}✓ Student account generated successfully!")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{fr}Script interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n{fr}Error: {str(e)}")
        sys.exit(1)
