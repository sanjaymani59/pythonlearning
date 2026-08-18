""" import random
num=random.randint(0,9)
print("Random:",num)

def add(a,b):
    return a+b
ans=add(10,49)

print(ans)
print(ans*2)

def greet(name):
    return "Hello "+name
message=greet("sam")
print (message)

def check(age):
    if age >=18:
        return "eligible"

    return "not Eligible"

print(check(20))
print(check(15)) """


""" def list_nnum():
    return[10,43]
num =list_nnum

print(num) """


def number(num,target):
    for nums in num:

        if num==target:
            return "found"

        return "not Found"

num=[45,4,43,6,2,]


print(number(num,4))

 

