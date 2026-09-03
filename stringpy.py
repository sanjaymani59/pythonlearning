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


# sent= input("enter sent:")

# words= sent.split()
# print("num of words:",len(words))


# text="hello sir"
# print(text.replace("",""))

# languag= text.split()
# print(languag)

# text = input("Ente The Text:")

# if text.isalpha():
#     print ("only alphabets")

# else:l
#     print("contains other characters")


# word =["apple","is ", "red"]
# words =" ".join(word)
# print(words)


# word=["cat","window","python ","code","hello" ]

# filter_word=[w.upper() for w in word if len(w)>=4]

# print(filter_word)



# di_a={'a':1,'b':2}
# di_b={'b':3,'c':4}

# merge={**di_a,**di_b}

# print(merge)



# deliver ="swiggy"

# def order():
#     print('curd rice')

#     def quentity():
#         print("5 ")
#     quentity()

# order()


amount= 3000

tax = amount*0.10

total = amount+tax

print(total)


if total>1000:

    discount = total*0.10

    total -= discount

print(total)
