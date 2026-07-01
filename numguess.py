secret_number=55

for i in range(0,5):
    
    number_input =int(input("Enter the number:"))

    if secret_number==number_input:
        print("you won")
        break
    else:
        print("you lost")