class mobile:
    def __init__ (self,brand,model,exprience):
        self.brand=brand;
        self.model=model;
        self.exprience=exprience;

    def display(self):
        print("Brand:"+self.brand)
        print("model:"+self.model)
        print("exprience:"+self.exprience)

sam=mobile("samsang","i5rag","5 years")
sam.display()



jay=mobile("moto","i10 rag","10 years")
jay.display()
