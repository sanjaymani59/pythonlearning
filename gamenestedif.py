import random

print("welcome to number guess game ")
print("enter the number 1-100")

secter_number = random.randint(1,100)


for i in range(1,11):
    user_input=int(input("enter a number:"))
    if secter_number<1 or secter_number>100:
        print("invalide number! enter number 1-100:")

    elif secter_number > user_input:
        print("enter number is greater than guess")

    elif secter_number<user_input:
        print("enter number is less than guess")

    else:
        print("you guess is correct")
        break

if secter_number==user_input:
     print(f"congrulation you guess the numbe  in {secter_number} in {i} attempts")
else:
    print("your guessing chance is over better luck next time")
    
    