Balance=5000
while True:
    print("/n---------menu----------")
    print("1. Balance")
    print("2. Deposit")
    print("3. withdraw")
    print("4. Thank you")

    choice=int(input("Enter Choice :"))

    if(choice==1):
        print("Balance:",Balance)

    elif(choice==2):
        Amount=int(input("Enter Deposit amount:"))
        Balance += Amount
        print("New Amount:", Balance)

    elif(choice==3):
        Amount=int(input("Enter Amount:"))
       
        if Amount<=Balance:
       
           Balance-=Amount
           print("Withdraw successfully")
           print("Current Balance:",Balance)

        else:
            print("Not sufficient Amount Is Available In Your Account")

    elif(choice==4):
        print("Thank You")


    else:
        print("Value Invalid")
           




    