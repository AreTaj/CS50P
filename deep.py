# Deep Thought
# Problem Set 1

x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
x = x.strip()
x = x.lower()

if(x == "42" or x == "forty two" or x == "forty-two"):
    print("Yes")
else:
    print("No")