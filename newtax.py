""" def cal_tax(price,tax):
    amount=price*tax

    total=price+amount

    return total


final_tax= cal_tax(450,5)

print (f"your tax is: ${final_tax}")
 """


""" check = lambda x:"pos" if x>0 else "neg"
print (check(10)) """

""" check=lambda x:"even " if x%2==0 else "odd"
print(check(5)) """


larger=lambda a,b: a if a>b else b
print (larger(9,4 ))


multiplay=lambda a,b: a*b
print(multiplay(5,5))


sub=lambda a,b:a-b
print (sub(5,5))

def muktiplay(a,b):
    return a*b