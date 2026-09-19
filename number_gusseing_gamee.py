import random


num_guess=random.randint(1,100)
while True:
        try:
            guess=int (input("Enter Your Number : (1-100):"))

            if guess<num_guess:

                print("Too Low")

            elif guess>num_guess:
                print("Too High")

            else:
                print("congrulation ")
                break

        except ValueError:
            print("invalide value ")





""" inpute_=int(input('gusse number 1 to 100'))

    if inpute_ < number_gusseing_gameel:
        print('too low')





except ValueError:
    print("please ente valisd number")

print(guess) """



""" 17;26
https://www.youtube.com/watch?v=yVl_G-F7m8c """
