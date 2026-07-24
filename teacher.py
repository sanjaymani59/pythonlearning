class Teacher:
    def __init__(self,name,reg):
        self.name=name;
        self.reg=reg;
    def display(self):
        print("Name:"+self.name)
        print("regno:"+self.reg)

t1=Teacher("sam","102")
t2=Teacher("jay","566")

t1.display()
t2.display()