#               Welcom to pizza shop!
#   _____________________menu_____________________
#   |      Small Pizza:                     $15   |
#   |      Medium Pizza:                    $20   |
#   |      Large Pizza:                     $25   |
#   | Pepperoni for Small Pizza:           +$2    |
#   | Pepperoni for Medium or Large Pizza: +$3    |
#   | Extra cheese for any size pizza:     +$1    |
#   |_____________________________________________|
size = input("what size of pizza do you want? \n(s for small)\n(m for Medium)\n(l for large)\n:")
Pepperoni = input("do you want Pepperoni? yes or no  ")
extraCheese = input("do you want extra cheese? yes or no  ")
bill = int(0)
if size=="s":
    bill=15
    if Pepperoni=="yes":
       bill += 2
    if extraCheese=="yes":
        bill +=1
    print(f"your bill is {bill}")
elif size=="m":
    bill=20
    if Pepperoni=="yes":
       bill += 3
    if extraCheese=="yes":
        bill +=1
    print(f"your bill is {bill}")
elif size=="l":
    bill=25
    if Pepperoni=="yes":
       bill += 3
    if extraCheese=="yes":
        bill +=1
    print(f"your bill is {bill}")
else:
    print("we dont have that size! sorry(not really)")

    

