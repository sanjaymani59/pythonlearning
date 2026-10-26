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


# amount= 3000

# tax = amount*0.10

# total = amount+tax

# print(total)


# if total>1000:

#     discount = total*0.10

#     total -= discount

# print(total)


# text='python'

# rev=""

# for c in text:
#     rev=rev+c

# print(rev)



# total =0

# for i in range(1,10):
#     total+=i

# print("total:" ,total)



# def dup(inlist):
#     un=[]

#     for item in inlist:
#         if item not in un:
#             un.append(item)

#     return un
# num =[3,5,6,5,4,3,2]

# print(num)
# print(dup(num))
# w="helloo"

# d=len(w)-1
# print(d)
""" 
# makes all first letter captial 
word1="hello of My"

word2="not A number"
formating =f"{word1.title()}--{word2.title()}"
print(formating)
 """


# replacing 
""" location ="delhi"
new_location= location.replace("delhi","chennai")

print(new_location) """


# string splliting

""" word = "hello to all my friends and students are present in room .at 005 and 0055"

sp=word.split("at")[1].split("and") [0] .strip()

print(sp) """


# find exacet word 

""" word=" all my friends and students are present in room"
if "students" in word:
    print("yes") """


# word=" all my friends and students are present in room"
# w=word.find("my")
# print(w)


# mark=59
# attendance=45

""" if mark >=59 and attendance>=44:
    print("okay")
else:
    print("not alloweded") """


# name="hello boy of boy"

# inite= ''.join([word[0].upper() for word in name.split()])
# print(inite)


# """ word="     airport    "
# s=word.strip()
# print(s) """

# w="hi i'm in dubai and americal at same time in a video conference"

# r=len(w.split(a))
# print(r)


""" 
mark =50

if mark>= 90:
    print("A")

elif mark>=70:
    print("B")

elif mark>=50:
    print("C")
else:
    print("fail~") """


age=18

has_licence="yes"

if age>=80:
    if has_licence=="yes":
        print("you drink ")

    else:
        print("go")

else:
    print("you young")