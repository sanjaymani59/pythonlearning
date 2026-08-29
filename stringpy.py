""" name="sam"
print(name)

print(len(name)) """

""" word='python'
print(word[0])
print(word[1])
print(word[5])

print(word[-1]) """



""" word='python'

print(word[0:3])

print(word[:4])
print(word[-4:])
print(word[:-1])
print(word[-1:])

print(word[::-1]) """


""" name="python sam"
print(name.upper())

print(name.lower())
print(name.capitalize()) """

""" text="i like java"

newtext=text.replace('java','python')

print(newtext)

print(text.count("a")) """

# text='helloaa'

# print(text.find('h'))

# name=input("enter ypur name:")
# print("hello,",name)

# print("Length :",len(name))

# print(name.upper)

# word= "samsam"

# # for n in word:
# #     print (n)

# count=0d

# for n in word:
#     count+=1
# print("character:",count)

""" 
word=input("enter any word:")
count=0

for i in word.lower():
    if i in "aeiou":
        count+=1
print("vowles:",count) """

# consonants

# word=input("enter any word:")
# count=0

# for ch in word.lower():

#     if ch.isalpha() and ch not in 'aeiou':
#         count +=1

# print(count)


# word=input("enter any word:")

# if word==word[::-1]:
#     print("palindronme")

# else:
#     print("not palindrome")

# 32. Reverse Without [::-1]

# word =input("enter the word:")

# reverse ='' 

# for ch in word:
#     reverse = ch + (word[::-1])
# print('reversed:',reverse)

# 24. Check Character

# text0=input("Enter the text:")
# text1=input('ente the text:')
# if text0==text1:
#     print("both are same")
# else:
#     print("Different")

# if 'a' in text :
#     print('text is a is found')

# else:
#     print('letter a is not found')


sent= input("enter sent:")

words= sent.split()
print("num of words:",len(words))



