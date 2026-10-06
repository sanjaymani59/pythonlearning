# LEVEL 1 — LIST
# A list stores multiple values.

""" num=[10,20,30,40,50]
print(num) """

""" # Access elements
print(num[0])
print(num[1]) """

# LEVEL 2 — Changing a List
# Lists are mutable, meaning we can change them.

"""num[2]=400
print(num)


# LEVEL 3 — Adding Elements
# append()
# Adds one item at the end
num.append(100)
print(num)

# insert()
# Adds an item at a particular position.
num.insert(0,10101)
print (num)

# LEVEL 4 — Removing Elements
# remove()

num.remove(20)
print(num) """


""" # pop()
num.pop(4)
print(num) """


# LEVEL 5 — List + Loop

""" nums=[10,20,30,40]

for num in nums:
    print(num)
Find the total

total=0
for num in nums:
    total =total+num
print(total) """


# LEVEL 6 — Find Largest Number

""" nums=[10,20,30,40,50]

largest =nums[0]
for num in nums:
    if num>largest:
        largest=num
print(largest) """


# LEVEL 7 — List Slicing



""" nums=[10,20,30,40,50]
# list[start:end]
# The end index is not included.
print(nums[1:4])
 """




# LEVEL 8 — Tuple





""" coordinates =(10,20)
print(coordinates)
print(coordinates[0])
print(coordinates[1])

# example 

student=("sam  ",45,"cse")

name=student[0]
age=[1]
dept=student[2]

print(name)
print(age)
print(dept) """


""" # LEVEL 9 — Set
# A set stores unique values.

num={10,20,30,30,50,40,50}
print(num)

# Duplicates are automatically removed. """

# Real use

""" names=[
    "Arun",
    "Ragul",
    "Arun",
    'Aids'
]

unique_name=set(names)
print(unique_name) """


# LEVEL 10 — Set Operations
# Sets become powerful when comparing groups.


""" py_std={"Arun","Ragul","sam","kumar"}
java_std={"Arun","jayam","sam","kumar"}
# Students learning both
print(py_std & java_std)
# Students learning either subject
print(py_std | java_std)
# Students learning Python but not Java
print(py_std - java_std)
 """

# LEVEL 11 — Dictionary
# A dictionary stores:
# key → value

""" std={
    "name":"monish ",
    "age": 21,
    "depatrment":"cse"
}
# print(std)
# print(std["name"])
# print(std["age"])

# LEVEL 12 — Modify Dictionary

std["age"]=25
std["college"]="smm"
print(std)
 """
# LEVEL 13 — Dictionary + Loop

""" marks={
    'python':85,
    'java':78,
    'dbms':90
}
for sub,mark in marks.items():
    print(sub,":" ,mark) """

# LEVEL 14 — Nested Data Structures

""" students=[
    {
        'name':'ARUN',
     'age':21,
     'marks':85
     },
     {
         'name':'Ruhul',
         'age':20,
         'marks':78
     },
     {
         'name':'priya',
         'age':21,
         'marks': 92
     }

]
print(students[2])
 """


# LEVEL 15 — Nested Dictionary

""" students={
    '101': {
        'name':'arun',
        'marks':80
    },

    '102':{
        'name':'Ragul',
        'marks':78

    }
}

print(students['101']['name']) """

# LEVEL 16 — List Comprehension

""" numders=[1,2,3,4,5]
squares=[]

for number in numders:
    squares.append(number *number)
print(squares) """

""" squares=[number*number for number in numders]
print(squares)  """


# LEVEL 17 — List Comprehension + Condition

""" numbers=[1,2,3,4,5,6,7,8]
evennum = [
    number
    for number in numbers
    
    if number %2==0
    ]
print(evennum) """

# LEVEL 18 — Dictionary Comprehension

""" numbers=[1,2,3,4,5,6,7,8]
squres={
    num:num*num
    for num in numbers
}
print(squres) """


# LEVEL 19 — Stack
# A stack follows:
# LIFO = Last In, First Out

""" stack=[]
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')

print(stack)
item=stack.pop()
print('removed:',item)
print(stack) """

# LEVEL 20 — Queue
# A queue follows:
# FIFO = First In, First Out

""" from collections import deque
queue=deque()

queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")

print(queue)

person =queue.popleft()

print("Removed :", person)
print(queue) """


# LEVEL 21 — Counter
# Python provides useful data structures in collections.
# Example: count characters.

""" from collections import Counter
text='apple'
count =Counter(text)
print(count) """ 


# LEVEL 22 — Real Coding Problem: Frequency Count

""" from collections import Counter
numbers=[1,2,2,3,3,4,4,4,4]
frequency = Counter(numbers)
for number,count in frequency.items():
    print(number ,"append", count , "times") """

# LEVEL 23 — defaultdict

from collections import defaultdict

st=[
    ('arun','cse'),
    ('ams','cse'),
    ('sam','it')
]

group =defaultdict(list)

for name,dept in st:
    group[dept].append(name)

print(dict(group))