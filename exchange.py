def exchange(x,y):
    x,y=y,x
    print("after exchange of x,y")
    print("x=",x)
    print("y=",y)
x=input("enter value of X:")
y=input("enter value of y:")
print("before exchange of x,y")
print("x=",x)
print("y=",y)
exchange(x,y)