import math 

num = float(input( "Enter a number: "))
print("1. Square ")
print("2. cube")
print("3. Squre Root")
print("4. Double ")
print("5.Half")

choice = int(input("Choose an operation :"))

if choice==1:
    print("Square :", num**2)

elif choice==2:
    print("cube : " , num**3)

elif choice==3:
    if num>=0:
        print("Squre Root : ", math.sqrt(num))
    else:
        print("cannot calculate real sqare root ")

elif choice ==4:
    print("Double :", num*2)

elif choice ==5:
    print("Half :", num/2)

else:
    print("invalie choice ")
