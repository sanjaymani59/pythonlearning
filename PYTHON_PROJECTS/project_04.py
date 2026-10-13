# RockPaperScissors  Game

import random

options=["rock","paper","scissors"]
# player=input("Enter your choice(Rock,Paper,Scissors):")
computer=random.choice(options)
player=None

while player not in options:
    player=input("Enter your choice(Rock,Paper,Scissors):")
    print("invalied value")

print(f"you chose:{player}")
print(f"computer chose:{computer}")

if player==computer:
    print("it is tie.")
elif player =="rock" and computer=="scissors":
    print("you won!")

elif player =="paper" and computer=="rock":
    print("you won!!")

elif player =="scissors" and computer=="rock":
    print("you won !!!")

else:
    print("you loos !!!!")


# 1:54