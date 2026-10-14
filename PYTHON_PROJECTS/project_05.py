# cafe order simulation 


menu={
    "pizza":150.00,
    "popcorn": 120.00,
    "fish chips":450.00,
    "fries": 100.00,
    "hamburger": 200.75,
    "chicken nuggets ":350.00,
    "soda": 55.00,
    "browed coffe": 99.00
}


cart=[]

total_price=0

print("------------------------MENU-----------------")

for key , value in menu.items():

    print(f"{key}:₹{value:.2f}")

print("-----------------------------------")

while True:
    food=input("Enter The Food That you want to eate (press q to quit):").lower()

    if(food=="q"):
        break
    elif menu.get(food) is not None :
        cart.append(food)

print("your order is : ")
for item in cart:
    print(item)

print()


for item in cart:
    total_price= total_price+menu.get(item)

print("your  total bill amount :", total_price)
