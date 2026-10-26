def tempexchange():

    x=int(input("Enter X:"))
    y= int (input("Enter Y:"))

    print( "before exchange")

    print("X",x)
    print("Y",y)

    temp=x
    x=y
    y=temp

    print("after exchange")
    print("X",x)
    print("Y",y)


tempexchange()