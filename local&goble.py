
""" //local variable or scope """
def test():
    x=20
    print(x)

test()

""" global scope """

x=59
def test():
    print(x)
test()


""" both local and global  """
x=59
def test():
    x=30
    print("inside:",x)
test()

print("outside:",x)