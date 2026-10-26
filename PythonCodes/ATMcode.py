balance=int(input("Enter Amount:"))
    
    
while True :

    print(" \n 1. check balance")
    print("2. deposit amount")
    print("3. exit")

    choice = input("Enter the choice:");

    if choice =="1":
             print("Balance=",balance)

    elif choice =="2":
                amount = int(input("Enter amount:"))
                balance += amount
                print("successfully deposited")
    
    elif choice=="3":
             print("Thank you!")
             break

    else:
         print("Invalide value")





        