class laptop:

    def __init__(self):
        self.ram=""
        self.processor=""
        

    def display(self):
        print("ram", self.ram)
        print("processor",self.processor)


hp=laptop()
dell=laptop()

hp.ram="i5"
hp.processor="8gb"

dell.ram="i7"
dell.processor="16gb"

hp.display()
dell.display()