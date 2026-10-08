students = []

# add student

def add_student():

    name=input("Enter student name:")
    age=int(input("Enter Student age:"))
    department=input("Enter department:")

    student={
        "name":name,
        "age":age,
        "department":department
    }

    students.append(student)
    print("student added successfully ")