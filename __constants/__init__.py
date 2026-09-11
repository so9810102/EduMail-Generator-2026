"""
Enhanced __init__.py for constants module
Imports from const.py (consolidated module)
"""

from .const import (
    universities_db,
    CAMPUSES,
    SEMESTERS,
    GENDERS,
    NATIONALITIES,
    country_codes,
    firstName,
    LastName,
    studentAddress,
    randomMonth,
    randomDay,
    randomYear,
    randomEduMonth,
    randomEduDay,
    randomEduYear,
    allColleges
)

__all__ = [
    'universities_db',
    'CAMPUSES',
    'SEMESTERS',
    'GENDERS',
    'NATIONALITIES',
    'country_codes',
    'firstName',
    'LastName',
    'studentAddress',
    'randomMonth',
    'randomDay',
    'randomYear',
    'randomEduMonth',
    'randomEduDay',
    'randomEduYear',
    'allColleges'
]
