a=[]
for i in range(10):
    num=int(input("enter a number:"+str(i+1)))
    a.append(num)
print(a)

sum =0

for i in a:
    sum=sum+i
print(sum)