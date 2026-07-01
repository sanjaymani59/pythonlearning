secret_number=55

while True:
    number_input=int(input("Enter your number:"))

    if secret_number==number_input:
        print("you won")
        break
    else:
        print ("you lost")
