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


""" larger=lambda a,b: a if a>b else b
print (larger(9,4 ))


multiplay=lambda a,b: a*b
print(multiplay(5,5))


sub=lambda a,b:a-b
print (sub(5,5))

def muktiplay(a,b):
    return a*b """

def total(old_avg,new_avg,incorr,corr):

    total_cha=corr-incorr

    total_avg=new_avg-old_avg


    if avg==0:
        raise ValueError ("Average is not found")

    avge=total_cha/total_cha

    return int (avg)
o_a=59
n_a=56
in_cor=4
cor=6

total_std=total(o_a,n_a,in_cor,cor)

print(f"total student:{total_std}")
