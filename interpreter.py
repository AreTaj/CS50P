# Math Interpreter
# Problem Set 1

expression = input("Expression: ")
x, y, z = expression.split(" ")

x = int(x)
z = int(z)

if(y=="+"):
    math = (x + z)

elif(y=="-"):
    math = (x - z)

elif(y=="*"):
    math = (x * z)

elif(y=="/"):
    math = (x / z)

else:
    print("Bad user input.")
    exit()

math = math.__round__(1)
math = float(math)
print(math)
