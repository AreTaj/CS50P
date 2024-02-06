# Seasons of Love
# Problem Set 8

import sys
import re
import inflect
import datetime
from datetime import date, datetime     # class datetime.date(year, month, day)

"""
Prompt user for date of birth in YYYY-MM-DD format
Print how old user is in minutes rounded to nearest integer, but using English words instead of numerals without any "and".
Assume the user was born at midnight and that current time is also midnight.
If input date not in YYYY-MM-DD format, sys.exit.
"""

p = inflect.engine()        # Necessary for library inflect

def main():
    try:
        birth_date = input("Date of Birth: ")
        year, month, day = check_birthday(birth_date)
    except:
        sys. exit("Invalid date")
    print(date_to_minutes(year, month, day))

def date_to_minutes(year, month, day):
    date_of_birth = date(int(year), int(month), int(day))
    today_date = date.today()
    diff_date = today_date - date_of_birth
    total_minutes = diff_date.days * 24 * 60
    convert_words = p.number_to_words(total_minutes, andword="")
    return convert_words.capitalize() + " minutes"

def check_birthday(birth_date):
    # Regex looks for four digits (0-9), two digits (0-9), two digits (0-9)
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day



if __name__ == "__main__":
    main()