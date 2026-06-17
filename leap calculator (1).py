#is the year you enter is leap or not
year = int(input("enter a year: "))
if year%4 != 0:
    message = "not leap"
elif year%100 != 0:
    massage = "leap"
elif year%400 == 0:
    massage = "leap"
else:
    massage = "not leap"

print(f"{year} is {massage}")
