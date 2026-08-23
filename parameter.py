""" def greet(name):##name=parameter
    print("hello",name) 

greet("sam") ##function call ## "sam"=argument
 """
## one parameter
""" def greet(name):
    print("hello",name)
greet("sam")
greet("jayam")
greet("surya") """

## number parameter
""" def square(number):
    print(number*number)

square(5) """

##two parameter
""" def add (a,b):
    print(a+b)
add(49,45) """

##three parameter

""" def student(name,age,course):
    print("Name:",name)
    print("Age:",age)
    print("Course",course)

student("sam",43,"cse") """


        ##LEVEL 2 PERAMETER +RETURN

##addition
""" def add (a,b):
    return a+b
result=add(34,54)
print(result)
new=result*3
print(new) """

##multiplication

""" def multiplay(a,b):
    return a*b
result=multiplay(20,10)
print(result) """

## even or odd

""" def check_even(number):
    if number %2==0:
        return "even"
    else:
        return "odd"
print(check_even(49)) """

""" 

def larger(a,b):
    if a>b:
        return a
    else:
        return b
git a print(larger(10,34)) """



""" def larthree(a,b,c):

    if a>=b and a>c:
        return a
    elif b>=a and b>=c:
        return b

    else:
        return c

print(larthree(34,53,56)) """


##fraction

""" def factorial(n):
    result= 1

    for i in range(1,n+1):

        result *=i

    return result

n=int(input("Enter the number:"))
print("factorial:",factorial(n)) """


""" def calculator(a,b,operator):

    if operator =="+":
        return a+b

    elif operator =="-":
        return a-b
    elif operator =="*":
        return a*b

    elif operator =="/":

        if b !=0:

            return a/b
        else: 
            return "connot divided by zero"

    else:
        return "invalide operator"


a=float(input("enter the number :"))
b=float(input("enter the number :"))
operator=input("Enter operator(+,_,*,/")

result= calculator(a,b,operator)

print("result:",result) """

def multi(num):
    for i in range(1,11):
        print(num,"X",i,"=",i*num)

num=int(input("Enter the number:"))
multi(num)