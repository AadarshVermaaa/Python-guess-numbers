# CODE BY AADARSH VERMA
# FIND ME ON INSTAGRAM -- WWW.INSTAGRM.COM/@AADARSHVERMAAA -- (PRO ACCOUNT)
# FIND ME ON INSTAGRAM -- WWW.INSTAGRM.COM/@LV_ADARSH
import random
num = random.randint(1, 20)
name = str(input("Welcome to my game!... Please enter your name:- "))
print(f"Hello {name.title}... You have 10 chances to guess the correct number... Good Luck")
# CHANGE THE VALUE OF LIVES TO INCREASE OR DECREASE THE CHANCES OF GAME
lives = 10
# WRITING SIMPLE LOGIC OF GUESS GAME! 
while lives > 0:

    humaninput = int(input("Enter the Value between 1 and 20\n\n>>> "))
    lives = lives-1
    if humaninput == num:
        print(
            "Congratulations You WON, you took [", 10 - lives, "] chances to complete")
        break
    elif humaninput < num:
        print("----------INCREASE YOUR INPUT----------\n")
        print("[{}] Left".format(lives))
    elif humaninput > num:
        print("----------DECREASE YOUR INPUT----------\n")
        print("[{}] Left".format(lives))
    else:
        break
if lives == 0:
    print("\t\t----------GAME OVER!!----------")
else:
    print("WOW")
