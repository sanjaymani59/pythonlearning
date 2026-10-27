""" for i in range(1,6):
    
    for j in range(1,6):
        print("1" ,end='')
    print("")
    for n in range(1,6):
        print("0" ,end='')

    print('') """


""" for i in range(1,6):
    
    for j in range(1,6):
        print("0" ,end='')
        for n in range(1,2):
            print("1" ,end='')

    print('') """

""" for i in range(1,6): 
    for j in range(1,6):
        print("*",end='')
    print('') """

""" print("enter list of numbers enter x to exit : ")
list_num =[]
while True:
    inp = input()
    if inp =="x":
        break

    list.append(int(inp))
print(list) """

str="a,s,d,g,e,w,q"
str1=""

for i in str: 
    if i ==",":
        continue
    str1=str1+i
print(str1)
    