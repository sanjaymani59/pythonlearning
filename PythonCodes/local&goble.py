
""" //local variable or scope """
""" def test():
    x=20
    print(x)

test() """

""" global scope """

""" x=59
def test():
    print(x)
test() """


""" both local and global  """
""" x=59
def test():
    x=30
    print("inside:",x)
test()

print("outside:",x) """




""" def change():
    global x
    x=6
change()
print(x)


def student(name):
    print("student:"+name)

student("sam")
 """

college="sam college"

""" def student():
    print ("student belongs to "+college)

def stuff():
    print("stuff belongs to "+college)

student()
stuff() """

""" for i in range(3):
    x=i
print(x) """

""" x=3
def outer():
    def inner():
        x=9
        print(x)
    inner()
print(x)
outer() """

count=0

def increase():
    global count
    count+=1
    print(count)

increase()
increase()
increase()
increase()

