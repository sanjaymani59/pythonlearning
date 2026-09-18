import random


while True:
    chooice= input("Want to roll your dice (y/n):").lower()

    if chooice== 'y' or chooice =='Y':
        ran1=random.randint(1,6)
        ran2=random.randint(1,6)

        print(f"({ran1},{ran2})")

    elif chooice== 'n':
        print("Thanking you playing")
        break

    else:

        print("Invalide value")


        

10:18
https://youtu.be/yVl_G-F7m8c?si=ntsJQ0Y1i-GQihOe





