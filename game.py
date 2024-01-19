# Guessing Game
# Problem Set 4

import random

while True:
    try:
        n = int(input("Level: "))
    except:
        ValueError
        continue
    if n <= 0:
        continue
    integer = random.randint(1,n)
    break

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0 :
            continue
    except:
        ValueError
        continue
    if guess > integer:
        print("Too large!")
        # Prompt again.
    elif guess < integer:
        print("Too small!")
        # Prompt again.
    elif guess == integer:
        print("Just right!")
        break
        # Ends the program.