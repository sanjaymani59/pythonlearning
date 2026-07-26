class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

    def display(self):
        print(self.name)
        print(self.mark)

    def result(self):
        if (self.mark < 35):

            print("your are failed")

        else:
            print("you got pass")

student1=student("sam",45)

student1.display()
student1.result()