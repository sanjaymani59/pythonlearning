num=int(input("Enter the number:"))

order= len(str(num))

sum_of_power = sum(int(digit)** order for digit in str(num))

if num == sum_of_power:

    print(num,"is an armstron number")
else:
    print(num,"is not an armstrong number")