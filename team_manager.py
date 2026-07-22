
class Employee:
    def __init__ (self,name):
        self.name=name

    def  login(self):
        return f"{self.name} is login"
    def view_task(self):
        return f"{self.name} is view "


class Teammember(Employee):
     def submit_task(self):
        return f"{self.name} is submmited"

class Manager(Employee):
    def assign_task(self):
        return f"{self.name} is assigined task"

sam = Teammember("saam")
jay = Manager("jaay")

print(sam.login())
print(sam.submit_task())
print(jay.login())
print(jay.assign_task())