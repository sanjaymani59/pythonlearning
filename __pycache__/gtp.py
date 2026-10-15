name= input("Enter your name:")

mark1=int(input("Enter tamil mark :"))
mark2=int(input("Enter English mark :"))
mark3=int(input("Enter computer mark :"))


total =mark1+mark2+mark3

average=total/3


print("\n ------------student result-----------")
print("Name: ",name)
print("total Mark : ", total)

print("average : ", average)

if average >50:
    print("pass")
else :
    print("fail")