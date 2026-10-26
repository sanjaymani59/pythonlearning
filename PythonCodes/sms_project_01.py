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

    print(name)
    print(age)

    # 2. Display Students

def display_students():
    if len (students) ==0:
        print("NO students found")
        return 
    print("\n ========students list======")

    for student in students:
        print("Name:",student["name"])
        print("Age:" , student["age"])
        print("Departmen:" , student["department"])
        print("---------------------------------")

# 3. Search Student

def search_student():
    search_student=input("Enter Student name to search :")
    found =False

    for student in students:
        if student["name"].lower()== search_student.lower():

            print("\n Student Found")
            print("Name:" ,student["name"])
            print("Age :" , student["age"])
            print("Department:" , student["department"])

            found =True

            break
        if not found:
            print("student not found")

# 4. Delete Student

def delete_student():

    delete_student = input("Enter student name to delete :")

    for student in students:

        if student["name"].lower()== delete_student.lower():
            students.remove(student)

            print("stusent deleted successfully !")
            return 
    print("student not found .")


while True:

    print("\n ------------------------------------------")
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("============================================")

    print("1. Add Student ")
    print("2.Display Student")
    print("3. Search Student ")
    print("4. Delete Student ")
    print("5. Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        add_student()

    if choice=="2":
        display_students()

    if choice=="3":
        search_student()

    if choice=="4":
        delete_student()

    if choice=="5":
        print("Thank u !!!!!")
        break

    else:
        print("Invalid Choice . Try again")
    
    

            




















































