# Federal Home Savings Bank
# Problem Set 1

greeting = input("Greeting: ")
greeting = greeting.strip()

if(greeting.__contains__("Hello")):
    print("$0")
elif(greeting.startswith("H")==True or greeting.startswith("h")==True ):
    print("$20")
else:
    print("$100")