import json
global students
students=[]
def show_menu():
    print("\n===== Student Management =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Find student")
    print("4. Remove Student")
    print("5. update Student")
    print("6. Exit")

def create_student(student_id, name, age, major):
    return {"id": student_id, "name": name, "age": age, "major": major}

def get_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please Enter a valid integer number.")

def add_student() :
    student_id = get_integer("Entet the Student ID: ")
    if student_exists(student_id) :
        print(f"The Student by ID {student_id} already exists.")
        return
    name = input("Name: ")
    age = get_integer("Enter the Age: ")
    major = input("Major: ")

    student = create_student(student_id, name, age, major)
    students.append(student)
    print("student added successfully.")
    save_students()

def student_exists(student_id):
    for student in students:
        if student["id"] == student_id:
            return True
    return False
def find_student(student_id):
    """
    Return the student dictionary by student ID.
    Returns None if the student is not found.
    """
    for student in students:
        if student["id"] == student_id:
            return student
    return None

def edit_student():
    student_id = int(input("Enter Student ID : "))
    student = find_student(student_id)
    if student is None:
        print("Student Not Found.")
        return
    student["name"] = input("Enter new name: ")
    student["age"] = input("Enter New age: ")
    student["major"] = input("Enter New major: ")
    save_students()
    print(f"Student with id {student_id} updated successfully")

def delete_student(student_id):
    for index,student in enumerate(students):
        if student["id"] == student_id:
            del students[index]
            print(f"student ID {student_id} deleted successfully.")
            return True
    return False

def load_student():
    global students
    try:
        with open("C:/Users/hosseini/Documents/GitHub/python-learning/projects/student_management/students.json", "r", encoding="utf-8") as file:
            students = json.load(file)
    except FileNotFoundError:
        print("Json File not found")
        students = []
    except:
        print("there was an error. may be json file is empty")
        students = []
    print(" Students Loaded successfully")


def show_students() :
    if len(students) == 0:
        print("No registered students found")
        return
    print("\n ========== Students List ==========")
    for student in students:
        print(f"ID       :{student['id']}")
        print(f"Name     :{student['name']}")
        print(f"Age      :{student['age']}")
        print(f"Major    :{student['major']}")
        print("--------------------------")
    print("====================================")

def save_students():
    global students
    with open("C:/Users/hosseini/Documents/GitHub/python-learning/projects/student_management/students.json", "w", encoding="utf-8") as file:
        #json.dump(students, file)
        json.dump(students, file, indent=4, ensure_ascii=False)

load_student()
while True:
    show_menu()
    choice=input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        student_id=input("Enter student number for search: ")
        student = find_student(student_id)
        if student is not None:
            print(student)
        else:
            print(f"student by ID : {student_id} not exist in the list" )
    elif choice == "4":
        student_id = get_integer("Enter student number that you want to delete : ")
        if delete_student(student_id):
            save_students()
    elif choice == "5":
        edit_student()
    #elif choice == "S" or choice == "s" :
    #    save_students()
    elif choice == "6":
        print("Thanks for using this program; Goodbye.")
        break
    else:
        print("Invalid Choice.")
    