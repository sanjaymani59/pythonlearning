print("simple calculator")

num1=float(input("Enter First Number:"))
num2=float(input("Enter Second Number:"))

print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.divide")

choice=input("choice(1-4):")

if choice=="1":
    print("Answer:",num1+num2)

elif choice=="2":
    print("Answer:",num1-num2)

elif choice=="3":
    print("Answer:",num1*num2)

elif choice=="4":
    if num2 !=0:
        print("Answer:",num1/num2)
    else:
         print("cannot divide by zero.")
else:
    print("Invalide choice")


