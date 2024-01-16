# Problem Set 3
# Fuel Gauge

while True:
    num = input("Fraction: ")
    index = num.find("/")
    try:
        x = int(num[:index])
        # Takes slice of input string "num" at position specified by "index", then converts to int.
        y = int(num[index+1:])
        # Takes slice of input string "num" at position specified by ("index" + 1), then converts to int.
        fraction = x / y
        if x > y:
            continue
        break
    except (ValueError, ZeroDivisionError):
        continue

percentage = fraction * 100
percentage = percentage.__round__()

if fraction > 0.9:
    print("F")
elif fraction < 0.1:
    print("E")
else:
    print(str(percentage) + '%')
