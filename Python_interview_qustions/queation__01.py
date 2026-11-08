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

text=input("Enter a string :")

count=0

for ch in text:
    if ch.lower() in "aeiou":
        count+=1
print("vowels ",count)