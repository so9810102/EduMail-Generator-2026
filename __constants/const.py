from faker import Faker
import random

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########

# ============================================
# UNIVERSITIES AND COLLEGES DATABASE
# ============================================

universities_db = {
    1: {
        "name": "Harvard University",
        "domain": "harvard.edu",
        "country": "United States",
        "state": "Massachusetts",
        "city": "Cambridge",
        "departments": ["Engineering", "Business", "Medicine", "Law", "Arts & Sciences"],
        "degrees": ["Bachelor's", "Master's", "PhD"],
    },
    2: {
        "name": "MIT (Massachusetts Institute of Technology)",
        "domain": "mit.edu",
        "country": "United States",
        "state": "Massachusetts",
        "city": "Cambridge",
        "departments": ["Engineering", "Science", "Management", "Architecture"],
        "degrees": ["Bachelor's", "Master's", "PhD"],
    },
    3: {
        "name": "Stanford University",
        "domain": "stanford.edu",
        "country": "United States",
        "state": "California",
        "city": "Stanford",
        "departments": ["Engineering", "Business", "Medicine", "Law", "Humanities"],
        "degrees": ["Bachelor's", "Master's", "PhD"],
    },
    4: {
        "name": "University of Oxford",
        "domain": "ox.ac.uk",
        "country": "United Kingdom",
        "state": "England",
        "city": "Oxford",
        "departments": ["Engineering", "Medicine", "Law", "Science", "Humanities"],
        "degrees": ["Bachelor's", "Master's", "PhD"],
    },
    5: {
        "name": "University of Cambridge",
        "domain": "cam.ac.uk",
        "country": "United Kingdom",
        "state": "England",
        "city": "Cambridge",
        "departments": ["Engineering", "Science", "Law", "Medicine", "Humanities"],
        "degrees": ["Bachelor's", "Master's", "PhD"],
    },
    6: {
        "name": "University of Toronto",
        "domain": "utoronto.ca",
        "country": "Canada",
        "state": "Ontario",
        "city": "Toronto",
        "departments": ["Engineering", "Business", "Medicine", "Law"],
        "degrees": ["Bachelor's", "Master's", "PhD"],
    },
    7: {
        "name": "University of Melbourne",
        "domain": "unimelb.edu.au",
        "country": "Australia",
        "state": "Victoria",
        "city": "Melbourne",
        "departments": ["Engineering", "Business", "Law", "Medicine", "Science"],
        "degrees": ["Bachelor's", "Master's", "PhD"],
    },
    8: {
        "name": "Bangladesh University of Engineering and Technology (BUET)",
        "domain": "buet.ac.bd",
        "country": "Bangladesh",
        "state": "Dhaka",
        "city": "Dhaka",
        "departments": ["Civil Engineering", "Electrical Engineering", "Mechanical Engineering", "Chemical Engineering"],
        "degrees": ["Bachelor's", "Master's", "PhD"],
    },
    9: {
        "name": "University of Dhaka",
        "domain": "du.ac.bd",
        "country": "Bangladesh",
        "state": "Dhaka",
        "city": "Dhaka",
        "departments": ["Science", "Arts", "Engineering", "Business", "Law"],
        "degrees": ["Bachelor's", "Master's", "PhD"],
    },
    10: {
        "name": "North South University",
        "domain": "northsouth.edu",
        "country": "Bangladesh",
        "state": "Dhaka",
        "city": "Dhaka",
        "departments": ["Engineering", "Business", "Humanities", "Science"],
        "degrees": ["Bachelor's", "Master's", "PhD"],
    },
}

# Campus Options
CAMPUSES = [
    "Main Campus",
    "Downtown Campus",
    "North Campus",
    "Central Campus",
]

# Semesters
SEMESTERS = ["Fall", "Spring", "Summer"]

# Gender Options
GENDERS = ["Male", "Female", "Other"]

# Nationalities
NATIONALITIES = [
    "American", "British", "Australian", "Canadian", "Bangladeshi",
    "Indian", "Chinese", "German", "French", "Japanese"
]

# Country codes for phone numbers
country_codes = [
    '201', '202', '203', '205', '206', '207', '208', '209',
    '212', '213', '214', '215', '216', '217', '218', '219',
    '220', '224', '225', '228', '229', '231', '234', '239',
    '240', '248', '251', '252', '253', '254', '256', '260',
    '262', '267', '269', '270', '276', '281', '283', '301',
    '302', '303', '304', '305', '307', '308', '309', '310',
    '312', '313', '314', '315', '316', '317', '318', '319',
    '320', '321', '323', '325', '330', '334', '336', '337',
    '339', '340', '341', '347', '352', '360', '361', '364',
    '385', '386', '401', '402', '404', '405', '406', '407',
    '408', '409', '410', '412', '413', '414', '415', '417',
    '419', '423', '425', '434', '435', '440', '442', '443',
    '445', '458', '464', '469', '470', '475', '478', '479',
    '480', '484', '501', '502', '503', '504', '505', '506',
    '507', '508', '509', '510', '512', '513', '514', '515',
    '516', '517', '518', '519', '520', '530', '540', '541',
    '551', '559', '561', '562', '563', '564', '567', '570',
    '571', '573', '574', '575', '580', '585', '586', '601',
    '602', '603', '605', '606', '607', '608', '609', '610',
    '612', '613', '614', '615', '616', '617', '618', '619',
    '620', '623', '626', '628', '630', '631', '636', '641',
    '646', '650', '651', '657', '660', '661', '662', '669',
]

# Generate random student data using Faker
fake = Faker('en_US')

ex = fake.name().split(' ')
firstName = ex[0]
LastName = ex[1] if len(ex) > 1 else 'Doe'

studentAddress = fake.address().replace('\n', ', ')

# Random dates
randomMonth = random.randint(1, 12)
randomDay = random.randint(1, 27)
randomYear = random.randint(1996, 2005)

randomEduMonth = random.randint(1, 12)
randomEduDay = random.randint(1, 27)
eduYears = [2019, 2020, 2021, 2022, 2023]
randomEduYear = random.choice(eduYears)
