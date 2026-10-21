a=12
b=18

gcd=1

for i in range(a , min(a,b) + 1):
    if i%b == 0 and i%a != 0:
        gcd=i

    print("Gcd",gcd)


lcm=max(a,b)

while True:
    if lcm%a == 0 and lcm%b == 0:
        break
    lcm+=1
print("LCM",lcm)