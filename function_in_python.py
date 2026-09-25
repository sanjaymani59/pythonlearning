""" def check (num):
    if num>0:
        return "positive "
    elif num<0:
        return "negative"
    else:
        return "zero"

print(check(4))
print(check(-3))
print(check(0))
 """

# // Level 7 — Function Returning Multiple Values

""" def cal(a,b):
    add =a+b
    sub=a-b
    multip=a*b

    return add,sub,multip

x,y,z=cal(34,3)

print(x)
print(y)
print(z) """

# Level 8 — Default Parameter

""" def greet(name ='std'):
    print("hello",name)

greet()
greet("sam") """


# Level 10 — *args

# Suppose you don't know how many numbers the user will give.

# You can use *args.



""" def add(*num):
    total=0
    for nums in num:
        total=total+nums

    return total


print(add(10,34,45,))
print(add(45,65,33,11)) """


# Level 11 — **kwargs

# **kwargs allows multiple keyword arguments.

""" def std_detial(**detials):
    for key,value in detials.items():
        print(key," ",value)


std_detial(
    name="sam",
    age=45,
    dept="cse",
    college="kkm"
) """


# Level 12 — Function Calling Another Function

""" def get_total(a,b,c):
    return a+b+c
def get_average(total):
    return total/3

total=get_total(23,45,43)
average=get_average(total)

print(total)
print(average) """

# Level 13 — Lambda Function

def square(x):
    return x*x 

square=lambda x:x*x

total=square(5)
print(total)


multiply = lambda a,b:a*b
print(multiply(9,4))