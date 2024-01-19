# Little Professor
# Problem Set 4

import random


def main():
    generate_integer(get_level())


def get_level():    # Prompts user for level; input must be 1, 2, or 3.
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                continue
            return level
        except:
            ValueError
            continue
        

def generate_integer(level):    # Randomly generates 10 math problems (X + Y = ?), with 'level' digits.
    score = 0
    for i in range(10):
        attempts = 1
        if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
        else:
            x = random.randint(100,999)
            y = random.randint(100,999)
#        Below does not work for level = 1, possibly because of how autochecker functions.
#        x = random.randint(10**(level-1), 10**level - 1)
#        y = random.randint(10**(level-1), 10**level - 1)
        while True:
            print(f"{x} + {y} = ", end = "")
            answer = input()
            if answer == str(x + y):
                score += 1
                break
            elif answer != str(x + y) and attempts != 3:
                print("EEE")
                attempts +=1
                continue
            else:
                print("EEE")
                print(f"{x} + {y} = {x + y}")
                break
    print(score)


if __name__ == "__main__":
    main()