print("======================")
print("                 MEN'S FASHIION STORE         ")
print("=======================")


print("\n 1. Shirt            -Rs.499")
print("2. Jeans               -Rs. 799")
print("3. Hoodie              -Rs. 1199")
print("4. jacket              -Rs. 1299")
print("5, shoes               -Rs. 1499")

total=0

while True:
choice=int(input("\n Select your product (1-6):"))

    if choice==1:
        total +=499
        print("T-shirt added to cart ")

    elif choice==2:
        total+=799
        print("shirt added to cart ")

    elif choice==3:
        total +=1199
        print("jeans added to cart")

    elif choice==4:
            total+=1299
            print("shoes added to cart ")
    
    elif choice==5:
            total +=1499
            print("hoddie added to cart")

    elif choice==6:
            total+=1000
            print("jacket added to cart ")
    
    else:
          print("Ivalide selection")
          continue

    more=input("\n Do you want to buy more (yes/no)::")

    if more.lower() !="yes":
          break

    print("\n ==========================")
    print("       BILL DETAILS ")
    print("=============================")

    print("Total Amount : ",total)

    print("thank you ")
print("======================================")