# Problem Set 3
# Grocery List

grocery = {}

while True:
    try:
        item = input().upper()
    except EOFError:
        print()
        break
    if item in grocery:
        grocery[item] += 1
        # Adds to existing key in dictionary.
    else:
        grocery[item] = 1
        # Creates new key, adds to dictionary, and sets value = 1.

for item in sorted(grocery.keys()):
    print(grocery[item], item)