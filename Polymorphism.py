class car:
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
    vars.move()