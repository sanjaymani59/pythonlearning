# https://youtu.be/ONcT716N2_M?si=wu0kZgaiFu9Dly7V


weight= float(input("Enter The Weight : "))
unit= input("kilogram or pounds :(k or L )")

if unit=="k":
    weight = weight*2.205
    unit="lds"
    print(f"The Weigth in lbs is {weight} {unit}")

elif unit =="L":
    weight= weight/2.205
    unit= "kgs"
    print(f"The Weigth in lbs is {weight} {unit}")




else:
    print(f"{unit} is not valid")
