""" def cal_tax(price,tax):
    amount=price*tax

    total=price+amount

    return total


final_tax= cal_tax(450,5)

print (f"your tax is: ${final_tax}")
 """


""" check = lambda x:"pos" if x>0 else "neg"
print (check(10)) """

check=lambda x:"even " if x%2==0 else "odd"
print(check(5))