# 1. Reverse a String

""" text=input("Enter the string :")

reverse=text[::-1]
print("Reversed string : ",reverse)
 """
# 2. Check Palindrome

""" text=input("Enter the word :")
if text==text[::-1]:
    print("palindrome")
else:
    print("not palindrome") """

# 3. Find the Largest Number in an Array

""" number=[10,20,30,40,50]
largest=number[0]

for num in number:
    if num>largest:
        largest=num
print("largest number:",largest) """

# 4. Count Vowels in a String

""" text=input("Enter a string :")

count=0

for ch in text:
    if ch.lower() in "aeiou":
        count+=1
print("vowels ",count) """
# 1. Reverse a Number

n=12345
rev=0

while n>0:
    digit =n%10
    rev=rev*10+digit

    n=n//10

print(rev)

# 2. Check Even or Odd

""" n=10
if n%10==0:
    print("even")
else:
    print("odd ") """

    # 3. Check Prime Number
n=7

count=0

""" for i in range(1,n+1):
    if n%i==0:
        count +=1

if count ==2:
    print("prime ")

else:
    print("not prime ")
 """
    # 4. Fibonacci Series

""" a=0
b=1

for i in  range(10):
    print(a,end=" ")
    a,b=b,a+b """

# 5. Armstrong Number

n=153
temp=n
total=0

""" while temp>0:
    digit=temp%10
    total +=digit**3
    temp//=10

if total ==n:
    print("armstrong")
else:
    print("not armstrong ")
 """
# 6. Find Largest Number in a List

""" a=[10,349,40,404,49]

lar=a[0]


for num in a:
    if num >lar:
        lar=num
print(lar) """
 
# 7. Find Second Largest Number

a=[10,30,34,67,76]

first=second=float("-inf")

for num in a:
    if num>first:
        second=first
        first =num
    elif first>num>second:
        second=num

print(second)
