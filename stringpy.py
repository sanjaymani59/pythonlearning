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


word=input("enter any word:")
count=0

for i in word.lower():
    if i in "aeiou":
        count+=1
print("vowles:",count)


