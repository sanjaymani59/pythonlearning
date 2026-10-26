class student:
    def __init__(self):
        self.roll=None
        self.name=None

    def input(self):
        self.roll= int(input("Enter the roll number:"))
        self.name=input("Enter name:")

    def display(self):
            print("Roll number:",self.roll)
            print("Name:",self.name)

obj=student()
obj.input()
obj.display()