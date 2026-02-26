import json

class studentsManager():
    
    def __init__(self,filename="studentsData.json"):
        self.filename = filename
        self.students = {}
        self.loadData()

    # Keeping all the data from the user
    def saveData(self):
        json_string = json.dumps(self.students,indent=4)
        f = open("studentsData.json","w")
        f.write(json_string)
        f.close()

    def loadData(self):
        try:
            with open(self.filename, "r") as file:
                self.students = json.load(file)
        except FileNotFoundError:
            print("No data found")
            
    # Here we are checking if the student id have a digit AND a char in its value
    def checkID(self,student_id):

        hasDigit = any(char.isdigit() for char in student_id)
        hasAlpha = any(char.isalpha() for char in student_id)
        return hasDigit and hasAlpha

    # Here we are adding students
    def addStudent(self,uid,name,grades):

        if self.checkID(uid):
            self.students[uid] = {
                "name": name, 
                "grades": grades
            }
            self.saveData()
            print(f"Student {name} added.")
        else:
            print("The ID is invalid.Use letters and numbers.")

    # Here we are getting the average number of the grades
    def getAverage(self,uid):

        if uid in self.students:
            gradesList = self.students[uid]["grades"]
            if len(gradesList) > 0:
                return sum(gradesList) / len(gradesList)
            return 0
        return None

    # Here we show a list of all the students and their info
    def showStudents(self):

        if not self.students:
            print("No students.")
        else:
            for uid,info in self.students.items():
                print(f"ID: {uid} | Name: {info['name']} | Grades: {info['grades']}") 

    # Here can we update the info of a specific student
    def updateStudent(self,uid):

        if uid in self.students:
            print(f"Editing student: {self.students[uid]['name']}")
            choice = input("What do you want to change? 1. Name, 2. Grades: ")

            if choice == "1":
                newName = input("Enter new name: ")
                self.students[uid]["name"] = newName
                self.saveData()
                print("New name updated.")
                
            elif choice == "2":
                newGrades = [float(x) for x in input("Enter new grades (space separated): ").split()]
                self.students[uid]["grades"] = newGrades
                self.saveData()
                print("New grades upgraded.")
            else:
                print("Invalid output.")
        else:
            print("Student not found.")
    # Here we delete a student
    def deleteStudent(self,uid):
        removedStudent = self.students.pop(uid, None)
        
        if removedStudent:
            self.saveData()
            print(f"Student {removedStudent['name']} deleted.")
        else:
            print(f"Student ID {uid} not found.")


manager = studentsManager()
while True:

    print("\n*** Student management system ***")
    choice = input(" 1. Add student\n 2. Get the average grades\n 3. Show data \n 4. Update student \n 5. Delete \n 6. Exit \n")

    if choice == "1":
        uid = input("Enter the student's ID: ")
        name = input("Enter the name of the student: ")
        grades = [float(x) for x in input("Enter grades (space separated): ").split()]
        manager.addStudent(uid,name,grades)

    elif choice == "2":
        uid = input("Enter the student's ID: ")
        avg = manager.getAverage(uid)
        if avg is not None:
            print(f"The average grade for {uid} is: {avg:.2f}")
        else:
            print("Student ID not found.")
        
    elif choice == "3":
        manager.showStudents()

    elif choice == "4":
        uid = input("Enter the ID of the student you want to edit: ")
        manager.updateStudent(uid)
            
    elif choice == "5":
        studentToDelete = input("What student you want to delete?")
        confirm = input(f"Are you sure you want to delete{studentToDelete} ?(y/n)")
        if confirm.lower() == 'y':
            manager.deleteStudent(studentToDelete)
        else:
            print("Choice cancelled.")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Wrong input")