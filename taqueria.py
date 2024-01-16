# Problem Set 3
# Felipe's Taqueria

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
while True:
    try:
        item = input("Item: ").title()
    except EOFError:
        print()
        break
    if item in menu:
        total += menu[item]
        print("Total: $", f"{total:.2f}", sep = "")


"""
Prompts for items until the user inputs control-d.
Treats the user’s input case insensitively. 
Ignores any input that isn’t an item. 
Assumes that every item on the menu will be titlecased.
"""