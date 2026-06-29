hights = input("enter student's hight(cm) \n example: 156 164 181 \n").split(" ")
temp = 0
for n in hights:
    temp = temp+1

for i in range(0,temp):
    hights[i] = float(hights[i])
    
    
print(hights)

sum = 0

for n in range(0,temp):
    sum = sum + hights[n]

average  = sum/temp
x = round(average,2)
print(f"the average hight of class is {x}")







