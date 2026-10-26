s_username="hello";
s_password=12345;


def validate():

    a =str(input("Enter username:"))
    b=int(input("enter a password:"))

    if(s_username==a and s_password==b):
            return True
    else:
            return False

a=validate()
print(a)
