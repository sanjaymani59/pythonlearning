# email slicer
# gh222@gmail.com

 
email=input("Enter the email :")

index= email.index("@")

username=email[:index]

domine= email[index+1:]

print(f"The username is {username} and domain is {domine}")