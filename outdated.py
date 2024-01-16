# Problem Set 3
# Outdated

# Prompt user for date in "mm/dd/yyyy" order or "Month dd, yyyy" order and outputs date in "yyyy/mm/dd" order

month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    # Input a date in 'mm/dd/yyyy' or 'Month dd, yyyy' format.
    if "/" in date:
        month, day, year = date.split("/")
    elif "," in date:
        date = date.replace(",", "")
        month, day, year = date.split(" ")
        if month in month_list:
            month = month_list.index(month) + 1
    else:
        continue
    try:
        if int(month) >= 12 or int(day) >= 31:
            continue
        else:
            break
    except ValueError:
        continue

print(f"{int(year)}" + "-" + f"{int(month):02}" + "-" + f"{int(day):02}")