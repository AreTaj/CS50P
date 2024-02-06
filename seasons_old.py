# Seasons of Love
# Problem Set 8

import sys
import re
# import inflect
import datetime
from datetime import date, datetime     # class datetime.date(year, month, day)
from num2words import num2words

"""
Prompt user for date of birth in YYYY-MM-DD format
Print how old user is in minutes rounded to nearest integer, but using English words instead of numerals without any "and".
Assume the user was born at midnight and that current time is also midnight.
If input date not in YYYY-MM-DD format, sys.exit.
"""

def main():
    today = date.today()
    try:
        birth_date = datetime.strptime(input("Date of Birth: "), "%Y-%m-%d").date()
        difference = today - birth_date     # datetime.timedelta object
        days_difference = difference.days
        minutes_difference = days_difference * 24 * 60
        print(convert(minutes_difference))
    except ValueError:
        sys.exit("Invalid date")

def convert(s):
    words = num2words(s) +" minutes"
    words = words.replace(" and", "")
    return words.capitalize()



if __name__ == "__main__":
    main()