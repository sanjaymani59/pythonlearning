class mobile:

    exprience='five';
    def __init__ (self,brand,model):
        self.brand=brand;
        self.model=model;
        # self.exprience=exprience;

    def display(self):
        print("Brand:"+self.brand)
        print("model:"+self.model)
        print("exprience:"+self.exprience)

sam=mobile("samsang","i5rag")
sam.display()



jay=mobile("moto","i10 rag")
jay.display()
