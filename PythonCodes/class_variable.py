class student:
    college= "annai college of engineering of america"

    def __init__(self,name):
        self.name=name

    def display(self):
        print("Name:"+self.name)
        print(student.college)

student1=student("vadakan sir")
student1.display()
        