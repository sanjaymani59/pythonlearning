secret =55

num=int (input("Enter any number :"))

if(num==secret):
    print("you gussed the number correctly",+num)

elif(num<secret):
    print("your numer is too small")
else:
    print("your number is too big")
    