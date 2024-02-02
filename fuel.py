# Refueling
# Problem Set 5

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    output = gauge(percentage)
    print(output)

def convert(fraction):
    while True:
        try:
            numerator, denominator = fraction.split("/")
            new_n = int(numerator)
            new_d = int(denominator)
            f = new_n / new_d
            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):   
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + '%'

if __name__ == "__main__":
    main()