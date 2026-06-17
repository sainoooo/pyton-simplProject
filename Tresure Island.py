print("Welcome to Tresure Island.\nYour mission is to find the treasure.")
first = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
first2 = first.lower()
if first2=="left":
    second = input('''You come to a lake. There is an island in the middle of the lake.
    Type 'wait' to wait for a boat or type 'swim' to start swimming\n''')
    second2 = second.lower()
else:
    print("GAME OVER\nyou fall of and die😬")
    exit()
if second2=="wait":
    third = input('''You arrive at the island unharmed. There is a house with 3 doors.
    One red, one yellow and one blue. Which colour do you choose?\n''')
    third2 = third.lower()
else:
    print("GAME OVER\nThe crocodiles ate your flesh and bones to the last. you died💘")
    exit()
if third2=="blue" or third2=="yellow":
    print('''GAME OVER\nIn this room, there was a lion, a giant,
    and a space alien who were friends, but when you entered,
    they hated you and tore you into pieces and threw you into the lava.''')
    exit()
else:
    print('''YoU WIN IT! you find the treasure and entered to heaven and live hapyy ever after💜💚💛🧡
    \n (just beac0us i'm ferrari fan)''')
    
    


