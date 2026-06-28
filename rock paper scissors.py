import random
act = -1
while (act<0 or act>2):
    print("welcom to rock paper scissors bot!")
    act = int(input("enter your choice: \n 0 for rock \n 1 for paper \n 2 for scissors \n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = [rock,paper,scissors]
campAct = random.randint(0,2)

print("camputer : \n" + choice[campAct])
act = str(act)
campAct = str(campAct)
result = act + campAct
if result =="02" or result =="10" or result =="21":
    print("you WIN !!")
if result =="00" or result =="11" or result =="22":    
    print("you tie :/")
if result =="01" or result =="12" or result =="20":   
    print("you loose... :(")







