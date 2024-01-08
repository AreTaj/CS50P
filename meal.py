# Meal Time
# Problem Set 1

def main():
    time = input("What time is it? ")
    time = convert(time)
    if(7.00 <= time and time <= 8.00):
        print("breakfast time")
    elif(12.00 <= time and time <= 13.00):
        print("lunch time")
    elif(18.00 <= time and time <= 19.00):
        print("dinner time")
    else:
        print("Error")

def convert(time):
    hours,minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    time = hours + (minutes/60)
    return time


if __name__ == "__main__":
    main()