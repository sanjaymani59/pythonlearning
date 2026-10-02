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

std={
    "name":"monish ",
    "age": 21,
    "depatrment":"cse"
}
print(std)
print(std["name"])
print(std["age"])