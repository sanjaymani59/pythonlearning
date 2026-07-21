class student:
    def __init__(self):
        self.name="hello"
        self.age= "12"
    def display(self):
        print("Name:"+self.name)
        print("age:" +self.age)

s1=student()

print(s1.name)
print(s1.age)
s1.display()