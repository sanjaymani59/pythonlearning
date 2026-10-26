def exchange(x,y):
    x,y=y,x

    print("After exchange x,y")
    print("X=",x)
    print("Y=",y)

x=int(input("Enter the x:"))
y=int (input("Entre the y:"))

print("before exchange")
print("X=",x)
print("y=",y)

exchange(x,y)