"""
Comprehensive List of Universities and Colleges
Updated: September 2026
"""

# Format: (University/College Name, Email Domain, Department Options, Degree Options)
UNIVERSITIES = [
    # US Universities
    ("Harvard University", "harvard.edu", ["Engineering", "Business", "Medicine", "Law", "Arts & Sciences"], ["Bachelor's", "Master's", "PhD", "Diploma"]),
    ("MIT (Massachusetts Institute of Technology)", "mit.edu", ["Engineering", "Science", "Management", "Architecture", "Humanities"], ["Bachelor's", "Master's", "PhD"]),
    ("Stanford University", "stanford.edu", ["Engineering", "Business", "Medicine", "Law", "Humanities"], ["Bachelor's", "Master's", "PhD"]),
    ("Yale University", "yale.edu", ["Engineering", "Business", "Law", "Medicine", "Arts"], ["Bachelor's", "Master's", "PhD"]),
    ("Princeton University", "princeton.edu", ["Engineering", "Science", "Public Affairs", "Humanities"], ["Bachelor's", "Master's", "PhD"]),
    ("Columbia University", "columbia.edu", ["Engineering", "Business", "Journalism", "Law", "Medicine"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Pennsylvania", "upenn.edu", ["Engineering", "Business", "Law", "Medicine", "Wharton"], ["Bachelor's", "Master's", "PhD"]),
    ("Duke University", "duke.edu", ["Engineering", "Business", "Law", "Medicine", "Trinity"], ["Bachelor's", "Master's", "PhD"]),
    ("Northwestern University", "northwestern.edu", ["Engineering", "Business", "Journalism", "Law", "Medicine"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Chicago", "uchicago.edu", ["Business", "Law", "Medicine", "Booth", "Harris"], ["Bachelor's", "Master's", "PhD"]),
    
    # More US Universities
    ("California Institute of Technology", "caltech.edu", ["Engineering", "Science", "Physics", "Chemistry"], ["Bachelor's", "Master's", "PhD"]),
    ("Cornell University", "cornell.edu", ["Engineering", "Agriculture", "Arts", "Law", "Business"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Michigan", "umich.edu", ["Engineering", "Business", "Medicine", "Law", "Ross"], ["Bachelor's", "Master's", "PhD"]),
    ("University of California Berkeley", "berkeley.edu", ["Engineering", "Business", "Law", "Science", "Haas"], ["Bachelor's", "Master's", "PhD"]),
    ("UCLA", "ucla.edu", ["Engineering", "Business", "Law", "Medicine", "Anderson"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Texas at Austin", "utexas.edu", ["Engineering", "Business", "Law", "Medicine"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Southern California", "usc.edu", ["Engineering", "Business", "Cinematic Arts", "Marshall"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Washington", "uw.edu", ["Engineering", "Business", "Medicine", "Law", "Foster"], ["Bachelor's", "Master's", "PhD"]),
    ("New York University", "nyu.edu", ["Engineering", "Business", "Law", "Medicine", "Stern"], ["Bachelor's", "Master's", "PhD"]),
    ("Boston University", "bu.edu", ["Engineering", "Business", "Law", "Medicine", "Questrom"], ["Bachelor's", "Master's", "PhD"]),
    
    # UK Universities
    ("University of Oxford", "ox.ac.uk", ["Engineering", "Medicine", "Law", "Science", "Humanities"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Cambridge", "cam.ac.uk", ["Engineering", "Science", "Law", "Medicine", "Humanities"], ["Bachelor's", "Master's", "PhD"]),
    ("Imperial College London", "ic.ac.uk", ["Engineering", "Science", "Medicine", "Business"], ["Bachelor's", "Master's", "PhD"]),
    ("London School of Economics", "lse.ac.uk", ["Business", "Economics", "Law", "Political Science"], ["Bachelor's", "Master's", "PhD"]),
    ("University College London", "ucl.ac.uk", ["Engineering", "Medicine", "Law", "Business", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Manchester", "manchester.ac.uk", ["Engineering", "Business", "Medicine", "Law", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Edinburgh", "ed.ac.uk", ["Engineering", "Medicine", "Law", "Business", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("University of York", "york.ac.uk", ["Engineering", "Business", "Law", "Science", "Humanities"], ["Bachelor's", "Master's", "PhD"]),
    
    # Australian Universities
    ("University of Melbourne", "unimelb.edu.au", ["Engineering", "Business", "Law", "Medicine", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Sydney", "sydney.edu.au", ["Engineering", "Business", "Law", "Medicine", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("University of New South Wales", "unsw.edu.au", ["Engineering", "Business", "Law", "Medicine", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("Australian National University", "anu.edu.au", ["Engineering", "Business", "Law", "Medicine", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Queensland", "uq.edu.au", ["Engineering", "Business", "Law", "Medicine", "Science"], ["Bachelor's", "Master's", "PhD"]),
    
    # Canadian Universities
    ("University of Toronto", "utoronto.ca", ["Engineering", "Business", "Law", "Medicine", "Rotman"], ["Bachelor's", "Master's", "PhD"]),
    ("McGill University", "mcgill.ca", ["Engineering", "Business", "Law", "Medicine", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("University of British Columbia", "ubc.ca", ["Engineering", "Business", "Law", "Medicine", "Science"], ["Bachelor's", "Master's", "PhD"]),
    
    # Bangladeshi Universities
    ("University of Dhaka", "du.ac.bd", ["Engineering", "Science", "Business", "Law", "Arts"], ["Bachelor's", "Master's", "PhD"]),
    ("Bangladesh University of Engineering and Technology", "buet.ac.bd", ["Civil", "Electrical", "Mechanical", "Chemical"], ["Bachelor's", "Master's", "PhD"]),
    ("North South University", "northsouth.edu", ["Engineering", "Business", "Humanities", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("BRAC University", "bracu.ac.bd", ["Engineering", "Business", "Humanities", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("Dhaka University", "du.ac.bd", ["Engineering", "Medicine", "Law", "Arts", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("Independent University Bangladesh", "iub.edu.bd", ["Engineering", "Business", "Humanities", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("Jahangirnagar University", "juniv.edu.bd", ["Science", "Social Science", "Business", "Engineering"], ["Bachelor's", "Master's", "PhD"]),
    ("Rajshahi University", "ru.ac.bd", ["Engineering", "Science", "Arts", "Business"], ["Bachelor's", "Master's", "PhD"]),
    ("Chittagong University", "cu.ac.bd", ["Engineering", "Science", "Arts", "Business"], ["Bachelor's", "Master's", "PhD"]),
    ("Khulna University", "ku.ac.bd", ["Engineering", "Science", "Business"], ["Bachelor's", "Master's", "PhD"]),
    
    # Indian Universities
    ("Indian Institute of Technology Delhi", "iitd.ac.in", ["Engineering", "Science", "Design", "Management"], ["Bachelor's", "Master's", "PhD"]),
    ("Indian Institute of Technology Mumbai", "iitb.ac.in", ["Engineering", "Science", "Design", "Management"], ["Bachelor's", "Master's", "PhD"]),
    ("Delhi University", "du.ac.in", ["Science", "Arts", "Commerce", "Law"], ["Bachelor's", "Master's", "PhD"]),
    ("Mumbai University", "mu.ac.in", ["Science", "Arts", "Commerce", "Engineering"], ["Bachelor's", "Master's", "PhD"]),
    
    # Other Countries
    ("University of Tokyo", "u-tokyo.ac.jp", ["Engineering", "Science", "Medicine", "Law"], ["Bachelor's", "Master's", "PhD"]),
    ("National University of Singapore", "nus.edu.sg", ["Engineering", "Business", "Medicine", "Law"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Hong Kong", "hku.hk", ["Engineering", "Business", "Medicine", "Law"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Toronto", "utoronto.ca", ["Engineering", "Business", "Medicine", "Law"], ["Bachelor's", "Master's", "PhD"]),
    ("ETH Zurich", "ethz.ch", ["Engineering", "Science", "Architecture"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Paris", "sorbonne-universite.fr", ["Science", "Medicine", "Law", "Humanities"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Berlin", "fu-berlin.de", ["Engineering", "Medicine", "Law", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Amsterdam", "uva.nl", ["Engineering", "Business", "Law", "Medicine"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Copenhagen", "ku.dk", ["Engineering", "Medicine", "Law", "Science"], ["Bachelor's", "Master's", "PhD"]),
    ("University of Toronto", "utoronto.ca", ["Engineering", "Business", "Medicine", "Law"], ["Bachelor's", "Master's", "PhD"]),
]

# Email Domain Patterns
EMAIL_DOMAINS = {
    "harvard.edu": "harvard",
    "mit.edu": "mit",
    "stanford.edu": "stanford",
    "yale.edu": "yale",
    "princeton.edu": "princeton",
    "columbia.edu": "columbia",
    "upenn.edu": "penn",
    "duke.edu": "duke",
    "northwestern.edu": "northwestern",
    "uchicago.edu": "uchicago",
    "caltech.edu": "caltech",
    "cornell.edu": "cornell",
    "umich.edu": "umich",
    "berkeley.edu": "berkeley",
    "ucla.edu": "ucla",
    "utexas.edu": "utexas",
    "usc.edu": "usc",
    "uw.edu": "washington",
    "nyu.edu": "nyu",
    "bu.edu": "bu",
}

# Campus Options
CAMPUSES = [
    "Main Campus",
    "Downtown Campus",
    "North Campus",
    "South Campus",
    "East Campus",
    "West Campus",
    "Central Campus",
    "Virtual Campus",
]

# Country and State Information
COUNTRIES = {
    "United States": ["California", "Texas", "Florida", "New York", "Pennsylvania", "Illinois", "Ohio", "Georgia", "North Carolina", "Michigan"],
    "United Kingdom": ["England", "Scotland", "Wales", "Northern Ireland"],
    "Australia": ["New South Wales", "Victoria", "Queensland", "South Australia", "Western Australia", "Tasmania"],
    "Canada": ["Ontario", "British Columbia", "Quebec", "Alberta", "Manitoba", "Saskatchewan"],
    "Bangladesh": ["Dhaka", "Chittagong", "Khulna", "Rajshahi", "Sylhet", "Barisal", "Rangpur"],
    "India": ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Pune", "Ahmedabad"],
    "Japan": ["Tokyo", "Osaka", "Kyoto", "Yokohama", "Kobe"],
    "Singapore": ["Central", "North", "South", "East", "West"],
}

# Academic Years
ACADEMIC_YEARS = ["2024", "2025", "2026", "2027", "2028"]

# Semesters
SEMESTERS = ["Fall", "Spring", "Summer"]

# Gender Options
GENDERS = ["Male", "Female", "Other", "Prefer not to say"]

# Nationalities
NATIONALITIES = [
    "American", "British", "Australian", "Canadian", "Japanese",
    "Singaporean", "Indian", "Bangladeshi", "Chinese", "German",
    "French", "Spanish", "Italian", "Dutch", "Swedish"
]
