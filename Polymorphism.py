""" class car:

    def move(self):
        print("car is moving")

class bus:
    def move(self):
        print("bus is moving")


class got:
    def move(self):
        print("got is moving")

var=[car(),bus(),got()]

for vars in var:
    vars.move() """

""" class payment:
    def pay(self):
        pass

class googlepay:
    def pay(self):
        print("payment made using googlepay")

class phonepay:
    def pay(self):
        print("payment mabe using phonepay")
class cared:
    def pay(self):
        print ("payment mabe using card")

payments=[googlepay(),phonepay(),cared()]


for payment in payments:
    payment.pay() """


class A:
    def action(self):
        print("Action A")

class B:
    def action(self):
        print("Action B")

objects=[A(),B()]

for obj in objects:
    obj.action()
