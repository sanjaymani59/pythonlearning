class Animal:
    def sound(self):
        print("animal are only real to me in my life")

class Dog(Animal):
    def sound(self):
       print("dog is the great frind of any one")

class Cat(Animal):
    def sound(self):
        print("cat are notty one ")

dog1=Dog()
cat1=Cat()

dog1.sound()
cat1.sound()