# Scourgify
# Problem Set 6

import sys
import csv

def main():
    check_command_line_arg()
    # Initializes list "output" and preserves order of appended elements
    output = []
    try:
        # Reads before.csv, re-orders columns with formatting, and appends to output=[]
        with open(sys.argv[1],"r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader  :
                last,first = row["name"].split(",")
                output.append({'first':first.lstrip(), 'last':last.lstrip(), 'house':row['house']})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # Writes to after.csv: ordered fieldnames and data from output=[]
    with open(sys.argv[2],"w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["first","last","house"])
        #writer.writerow({"first": "first", "last": "last", "house": "house"})
        writer.writeheader()
        for dictionary in output:
            #writer.writerow({"first":row["first"], "last":row["last"], "house":row["house"]})
            writer.writerow(dictionary)


def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments.")
    if len(sys.argv) > 3:
        sys.exit("Too many command line arguments.")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()