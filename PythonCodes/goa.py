class goa:
    name=""
    drink=""

    def party(self):
        print("come let is party")
    
    def beach(self):
        print("come let go to beach")


ramesh =goa()
sureash =goa()


ramesh.name="ramesh"
ramesh.drink="yes"
print(ramesh.name)
print(ramesh.drink)


sureash.name="sureash"
sureash.drink="No"
print(sureash.name)
print(sureash.drink)

ramesh.party()
sureash.beach()