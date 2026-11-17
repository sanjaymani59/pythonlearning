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

""" for num in a:
    if num>first:
        second=first
        first =num
    elif first>num>second:
        second=num

print(second) """
# 8. Remove Duplicate Elements

""" a=[1,2,3,4,5,6,1]

result=[]

for num in a:
    if num not in result:
        result.append(num)

print(result) """


# 9. Count Vowels

""" text ="education " 
count=0

for ch in text:
    if ch in "aeiou":
        count+=1
print(count) """

# 10. Check Palindrome String
""" 
text = "madm"

if text == text [::-1]:
    print("palindrome")
else:
    print("Not palindrome")


# 13. Count Character Frequency

text="banana"

for ch in set(text):
    print(ch,text.count(ch)) """

# 14. Swap Two Numbers

""" a=10
b=20

a,b=b,a
print(a,b)
 """

# 15. Find Missing Number

""" a=[1,2,3,4,5]

n=5

miss=n*(n+1)//2-sum(a)
print(miss) """


# 1. Check Whether Two Strings Are Anagrams

a='listen'
b='silent'
if sorted(a)==sorted(b):
    print("Anagram")
else:
    print("not anagram")

# 2. Find Common Elements in Two Lists

a=[39,34,56,54]
b=[45,65,34,23]

for num in a:
    if num in b:
        print(num)