print("Welcome to the Love Calculator!")

Name1 = input("What is your name? \n").lower()
Name2 = input("What is their name? \n").lower()

comb = Name1 + Name2

# True
countTrue1 = comb.count("t")
countTrue2 = comb.count("r")
countTrue3 = comb.count("u")
countTrue4 = comb.count("e")

true_score = countTrue1 + countTrue2 + countTrue3 + countTrue4

# Love
countLove1 = comb.count("l")
countLove2 = comb.count("o")
countLove3 = comb.count("v")
countLove4 = comb.count("e")

love_score = countLove1 + countLove2 + countLove3 + countLove4

score = int(str(true_score) + str(love_score))
if score<10 or score>90:
    txt = "you go together like coke and mentos😜🔥"
if score>40 and score<50:
    txt = "you are all right together!😍💞"
else:
    txt = ""
    # TODO: write code...
print(f"your score is {score}% {txt}")

