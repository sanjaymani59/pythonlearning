likes=0

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
        print("Invalid choice")