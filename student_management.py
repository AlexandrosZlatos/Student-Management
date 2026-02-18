import json

# Keeping all the data from the user
def saveData():
    json_string = json.dumps(students,indent=4)
    f = open("studentsData.json","w")
    f.write(json_string)
    f.close()

def loadData():
    global students 
    try:
        with open("studentsData.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        print("No data found")
        
students = {}

# Here we are checking if the student id have a digit AND a char in its value
def checkID(student_id):

    hasDigit = any(char.isdigit() for char in student_id)
    hasAlpha = any(char.isalpha() for char in student_id)
    return hasDigit and hasAlpha

# Here we are adding students
def addStudent(uid,name,grades):

    if checkID(uid):
        students[uid] = {
            "name": name, 
            "grades": grades
        }
        saveData()
        print(f"Student {name} added.")
    else:
        print("The ID is invalid.Use letters and numbers.")

# Here we are getting the average number of the grades
def getAverage(uid):

    if uid in students:
        gradesList = students[uid]["grades"]
        if len(gradesList) > 0:
            return sum(gradesList) / len(gradesList)
        return 0
    return None

# Here we show a list of all the students and their info
def showStudents():

    if not students:
        print("No students.")
    else:
        for uid,info in students.items():
            print(f"ID: {uid} | Name: {info['name']} | Grades: {info['grades']}") 

# Here can we update the info of a specific student
def updateStudent(uid):

    if uid in students:
        print(f"Editing student: {students[uid]['name']}")
        choice = input("What do you want to change? 1. Name, 2. Grades: ")

        if choice == "1":
            newName = input("Enter new name: ")
            students[uid]["name"] = newName
            saveData()
            print("New name updated.")
            
        elif choice == "2":
            newGrades = [float(x) for x in input("Enter new grades (space separated): ").split()]
            students[uid]["grades"] = newGrades
            saveData()
            print("New grades upgraded.")
        else:
            print("Invalid output.")
    else:
        print("Student not found.")
# Here we delete a student
def deleteStudent(uid):
    removedStudent = students.pop(uid, None)
    
    if removedStudent:
        saveData()
        print(f"Student {removedStudent['name']} deleted.")
    else:
        print(f"Student ID {uid} not found.")


loadData()
while True:

    print("\n*** Student management system ***")
    choice = input(" 1. Add student\n 2. Get the average grades\n 3. Show data \n 4. Update student \n 5. Delete \n 6. Exit \n")

    if choice == "1":
        uid = input("Enter the student's ID: ")
        name = input("Enter the name of the student: ")
        grades = [float(x) for x in input("Enter grades (space separated): ").split()]
        addStudent(uid,name,grades)

    elif choice == "2":
        uid = input("Enter the student's ID: ")
        avg = getAverage(uid)
        if avg is not None:
            print(f"The average grade for {uid} is: {avg:.2f}")
        else:
            print("Student ID not found.")
    
    elif choice == "3":
        showStudents()

    elif choice == "4":
        uid = input("Enter the ID of the student you want to edit: ")
        updateStudent(uid)
        
    elif choice == "5":
        studentToDelete = input("What student you want to delete?")
        confirm = input(f"Are you sure you want to delete{studentToDelete} ?(y/n)")
        if confirm.lower() == 'y':
            deleteStudent(studentToDelete)
        else:
            print("Choice cancelled.")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Wrong input")