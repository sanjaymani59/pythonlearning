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

""" str="a,s,d,g,e,w,q" """
# str1=

""" for i in str: 
    if i ==",":
        continue
    str1=str1+i
print(str1)
     """


""" sti_in = 'hi it me and you '
split_list = sti_in.split(' ')
print(split_list)

sti_join='-'.join(split_list)
print(sti_join) """



""" users=[]
user={"name":'ram',"age":35, "gender":"male"}
n=users.append(user)
user={"name":'ramya', 'age':36,"gender":'female'}
n=users.append(user)
print(users[0])  """


""" def greet():
    print("hello")
greet() """

""" def sum(num):
    sum_result=num*(num+1)/2
    return sum_result
result=sum(11)
print(result)
print(sum(20)) """


# def welcome(name):
#     print("welcome "+name)
# welcome("Radha")
""" num=4
while num <=40:
    print(num)
    num+=4 """

""" def total(num1,num2,num3):
    return num1+num2+num3
print(total(4,5,8)) """

def total(*args):
    sum =0

    for i in args:
        sum =sum+i

    return sum
print(total(4,5,5,9,7))