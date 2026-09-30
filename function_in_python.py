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

""" def square(x):
    return x*x 

square=lambda x:x*x

total=square(5)
print(total)


multiply = lambda a,b:a*b
print(multiply(9,4)) """

# Level 14 — Function with List

""" def find_large(num):

    large=num[0]

    for nums in num:

        if nums >large:

            large=nums
    return large




num =[85,45,25,69,99]
ans=find_large(num)
print(ans) """

# Level 15 — Function with Dictionary

""" def cal_total(marks):
    total=0

    for mark in marks.values():
        total+=mark

    return total

marks ={
    "python": 45,
    "java": 54,
    "sql": 50
}

total=cal_total(marks)
print(total) """

# Level 16 — Recursion
# Now we reach an important advanced concept.

# A function can call itself.

# This is called recursion.

# Example: factorial.


""" def fact(n):
    if n==0:
        return 1

    return n*fact(n-1)
print(fact(5))
 """
# Level 17 — Recursion + List

""" def recursive(num):
    if len(num)==0:
        return 0

    return num[0]+recursive(num[1:])

num=[10,39,33,94,94]
print(recursive(num)) """


# Level 18 — Advanced: Function as an Argument

""" def squre(x):
    return x*x
def process(num,operation):
    resutl=[]

    for num in nums:
        resutl.append(operation(num))

    return resutl

nums=[1,2,3,4,5]

ans=process(nums,squre)
print(ans) """

# Level 19 — Decorators

# This is an advanced Python function concept.

# A decorator allows us to add extra behavior to an existing function.


""" def my_decorator():
    def wrapper():
        print("Before function")
        function()
        print("after function")
    return wrapper

@my_decorator
def  hello():
    print("hello python")

hello() """


# Level 20 — Hard Example: Student Result System


""" student =[{
    "name": "Arun",
    "marks":[45,45,67]
},
{
    "name": "ram",
    "marks":[68,45,67]
},
{
    "name": "jau",
    "marks":[40,89,90]
},


]


def calculate_total(marks):
    total =0

    for mark in marks:

        total +=mark
    return total

def calculate_average(marks):
    total=calculate_total(marks)

    return total/len(marks)

def get_grade(average):
    if average>=90:
        return "A"
    elif average>=80:
        return "B"

    elif average>=70:
        return "c"
    else:
        return "f"

def create_report(student):
    name=student["name"]
    marks=student["marks"]

    total=calculate_total(marks)
    average =calculate_average(marks)
    grade=get_grade(average)

    return {
        "name":name,
        "total":total,
        "average":average,
        "grade":grade
    }
for students in student:
    report=create_report(students)
    print("\n name" , report["name"])
    print("total" , report["total"])
    print("average" , report["average"])
    print("grade" , report["grade"])
 """

