# Problem Set 2
# Coke Machine

due = 50
print("Amount Due:", due)
valid_coins = [5,10,25]
insert = int(input("Insert Coin: "))

while(insert not in valid_coins):
    print("Amount Due:", due)
    insert = int(input("Insert Coin: "))
    if(insert in valid_coins):
        break
difference = int(due) - int(insert)

while difference > 0:
    print("Amount Due:", difference)
    insert = int(input("Insert Coin: ")) 
    if(insert in valid_coins):
        difference = int(difference) - int(insert)
        if difference <= 0:
          print("Change Owed:", -difference)
          break
    elif(insert not in valid_coins):
        while(insert not in valid_coins):
            insert = int(input("Insert Coin: "))
            if(insert in valid_coins):
                difference = int(difference) - int(insert)
                break
