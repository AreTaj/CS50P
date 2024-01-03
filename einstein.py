# Einstein
# Problem Set 0

def main():
    mass = int(input("Enter a mass in kilograms. "))
    speed = 300000000
    speed2 = square(speed)
    print(mass*speed2, "Joules")

def square(n):
    return pow(n, 2)

main()