#welcom
import random
print("who is going to pay the bill today? LETS SEE!")
names = input("enter the names seperated by a comma.(,)")
namesList = names.split(",")

randomName = random.choice(namesList)
print(f"{randomName} is going to pay the bill today!")




