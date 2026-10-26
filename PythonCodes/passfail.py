def passfail(a):
    if(a>=35):
        print("pass")
        if(a>=50):
            print("super")
            
    else:
        print("fail")

a=int(input("enter mark:"))
passfail(a)