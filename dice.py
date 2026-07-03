import random

print("dice rolled:");
while True:

    roll= random.randint(1,6);
    print("you rolled:",roll);

    again=input("roll again;(y/n)");
    if again.lower() !="y":
     break

