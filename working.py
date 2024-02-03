# Working 9 to 5
# Problem Set 7

# Used https://regex101.com/ to check functionality of regular expressions.

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regex ensures input is in format "xx A/PM to yy A/PM"
    check_format = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if check_format:
        segment = check_format.groups()
        # If 12hr time is out of range for either start or end, raise VE
        if int(segment[1])>12 or int(segment[5])>12:
            raise ValueError
        #              start hour   start min   start AM/PM       
        start = format(segment[1],segment[2],segment[3])
        #              end hour   end min   end AM/PM
        end = format(segment[5],segment[6],segment[7])
        return start + " to " + end
    else:
        raise ValueError


def format(hours, minutes, am_pm):
    # To determine AM/PM conversion to 24hr
    if am_pm == "PM":
        if int(hours) == 12:
            new_hours = 12
        else:
            new_hours = int(hours) + 12
    else:   # If AM...
        if int(hours) == 12:
            new_hours = 0
        else:
            new_hours = int(hours)
    # To translate minutes
    if minutes == None:
        new_minutes = ":00"
        new_time = f"{new_hours:02}" + new_minutes
    else:
        new_time = f"{new_hours:02}" + ":" + minutes
    return new_time


    


if __name__ == "__main__":
    main()