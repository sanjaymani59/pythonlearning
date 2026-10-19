
# nested loop 
""" for i in range(1,7):
    print()
    for j in range(1,i+1):
        print("*",end='-')
print() """

#  whilw nested loop

""" i=1
while(i<2):
    j=1
    while(j<3):
        print(f"outer:{i}, inner{j}")
        j+=1
    i+=1
 """

""" def fact(n):
    
    if n==1:
        return n
    else:
        return n*fact(n-1)
num=int(input("Enter The Number : "))

print("The Factorial of ",num,"is ",fact(num)) """
  
    # return

def area(r):
    a =math.pi*r**2
    return a
import math
r=int(input("Enter the value: "))
x=area(r)
print(x)
        
        

