#Upgrad of BMI calculator:
weight = float(input("enter your weight(kg): "))
hieght = float(input("enter your hieght(m): "))
BMI = weight/ hieght**2
if BMI<=18.5:
    massage = ("underweight")
elif BMI <= 25:
    massage = ("normal weight")
elif BMI <= 30:
    massage = ("overweght")
elif BMI <= 35:
    massage = ("obese")
else:
    massage = ("clinically obese")
newBMI = "{:.2f}" .format(BMI)
print(f"your BMI is {newBMI} you are {massage}")





