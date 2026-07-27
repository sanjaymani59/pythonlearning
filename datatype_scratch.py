"""1__usint integer """

age=50
mark=70

print(age)
print(mark)
print(type( age))
print(type(mark))

""" 2___flote """
print("---------------------------------------------")

height=5.6
weight=60.6
print(height)
print(weight)
print(type(height))
print(type(weight))

print("---------------------------------------------")

""" 
3. string(str) """

name="san"
dept="cse"
print(name)
print(dept)
print(type(name))
print(type(dept))

print("---------------------------------------------")

""" 4. Boolean (bool) """

student=True
raining=False
print(student)
print(raining)
print(type(student))
print(type(raining))

print("----------------------------------------------")

""" 6. Tuple (tuple) """

list=["apple","orange","bananna"]
print(list)
print(type(list))
print("-----------------------------------------------")

""" 7. Set (set) """

set=("dog","goat","hen")
print(set)
print(type(set))

print("------------------------------------------------")

student1={
    "name":"sam",
    "age":"56",
    "applause":"everyone"
    }

print(student1)
print(type(student1))
print("------------------------------------------------")

""" 9. Multiple Data Types Together """

name="sopesticated"
age=34
classs="fifth"
mark=4.5
print(name)
print(age)
print(classs)
print(mark)
print(type(name))
print(type(age))
print(type(classs))
print(type(mark))
print("--------------------------------------------------")

""" 10. Type Conversion """
num="55"
print(num)
print(type(num))

num=int(num)
print(num+50)
print(type(num))

print("--------------------------------------------------")

""" 11. User Input """

name=input("Enter your name:")
age=int(input("Enter Your Name:"))

print("Name=",name)
print("Age=",age)

print("----------------------------------------------------")


""" 12. Arithmetic Using Data Types """

a=5
b=6

print("add:",a+b)
print("sub:",a-b)
print("multi:",a*b)
print("div",a/b)
print("------------------------------------------------------")

""" 13. List of Different Data Types """

data=["sam",6.78,50,True]
print(data)
print(type(data))
print("------------------------------------------------------")

""" 15. Using isinstance() """

a=59
b="hello"
print(isinstance(a,int))
print(isinstance(b,str))
print(isinstance(a,float))
print("------------------------------------------------------")

""" 
18. Empty Data Types """

a=()
b={}
c=[]
# d=set()

print(type(a))
print(type(b))
print(type(c))
# print(type(d))


print("-------------------------------------------------------")



name=input("Enter The name:")
age=int(input("Enter The Age:"))
salary=float(input("Enter The Salary:"))
married=input("Enter your married true/false:")=="true"

print("Name:",name)
print("Age:",age)
print("Salary:",salary)
print("Married:",married)

print(type(name))
print(type(age))
print(type(salary))
print(type(married))