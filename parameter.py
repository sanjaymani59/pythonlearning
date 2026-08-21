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

def check_even(number):
    if number %2==0:
        return "even"
    else:
        return "odd"
print(check_even(49))



