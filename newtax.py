def cal_tax(price,tax):
    amount=price*tax

    total=price+amount

    return total


final_tax= cal_tax(450,5)

print (f"your tax is: ${final_tax}")
