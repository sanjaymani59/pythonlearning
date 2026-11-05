""" likes=0

comment=[]

while True:
    print("\n 1.like")
    print("2. commeny "
          )
    print("3. Show ")
    print("4. Exit")


    choice=input("Enter Choice")

    if choice=="1":
        likes+=1

    elif choice=="2":
        c=input("Enter commet:")
        comment.append(c)
        print("comment added")

    elif choice=="3":
        print("total likes ", likes)
        print("comments",comment
              )

    elif choice=="4":
        break

    else:
        print("Invalid choice") """


""" print("hello")
a =2
b=8

for i in range(1,a+1):
    b=b*i

for i in range(1,b):
    print(b,"x",i,"-",b*i)

print(b) """

""" def get_user_info():
    user={'name':"vishnu",'age':39}
    return user
hi=get_user_info()
print(hi) """

# resursion


""" def fact(num):
    if num==0:
        return 1
    return num*fact (num-1)

print(fact(4)) """


""" def sq_num(num):
    sq=[]
    for i in range(1,num+1):
        sq.append(i*i)
    return sq """

# def sq_num_gen(num):
#     for i in range(1,num+1):
#         yield i*i
# su =sq_num_gen(10)
# for i in su:
#     print(i)
# # print (sq_num(10))


class stu:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display():
        print(self.name)
        print(self.age)

s1.stu("sam",43)
s1.display()