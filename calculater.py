class calculater:

    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    def add(self):
        print("add",self.num1+self.num2);
    def sub(self):
        print("sub:",self.num1-self.num2)



obj1=calculater(5,8)

obj1.add()
obj1.sub()