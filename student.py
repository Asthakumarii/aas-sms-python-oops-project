import os

# ---------------------- Student Class ----------------------
class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.total = 0
        self.percentage = 0
        self.grade = ""

    def calculate_result(self):
        self.total = self.m1 + self.m2 + self.m3
        self.percentage = self.total / 3

        if self.percentage >= 90:
            self.grade = "A+"
        elif self.percentage >= 75:
            self.grade = "A"
        elif self.percentage >= 60:
            self.grade = "B"
        elif self.percentage >= 40:
            self.grade = "C"
        else:
            self.grade = "Fail"

# ---------------------- Manager Class ----------------------
class StudentManager:
    def __init__(self):
        self.students = []
        self.file_name = "students.txt"
        self.load_students()

    # Load data from file
    def load_students(self):
        if not os.path.exists(self.file_name):
            return
        
        with open(self.file_name, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 7:
                    name = data[0]
                    m1 = int(data[1])
                    m2 = int(data[2])
                    m3 = int(data[3])
                    total = int(data[4])
                    percentage = float(data[5])
                    grade = data[6]

                    student = Student(name, m1, m2, m3)
                    student.total = total
                    student.percentage = percentage
                    student.grade = grade
                    self.students.append(student)

    # Save data to file
    def save_students(self):
        with open(self.file_name, "w") as file:
            for s in self.students:
                file.write(f"{s.name},{s.m1},{s.m2},{s.m3},{s.total},{s.percentage},{s.grade}\n")

    # Add student
    def add_student(self):
        name = input("Enter name: ")
        m1 = int(input("Enter marks of Subject 1: "))
        m2 = int(input("Enter marks of Subject 2: "))
        m3 = int(input("Enter marks of Subject 3: "))

        student = Student(name, m1, m2, m3)
        student.calculate_result()
        self.students.append(student)
        self.save_students()
        print("Student Added Successfully ✅")

    # View students
    def view_students(self):
        if not self.students:
            print("No student data available.")
            return

        for s in self.students:
            print(f"\nName: {s.name}")
            print(f"Marks: {s.m1}, {s.m2}, {s.m3}")
            print(f"Total: {s.total}")
            print(f"Percentage: {round(s.percentage,2)}")
            print(f"Grade: {s.grade}")

    # Delete student
    def delete_student(self):
        name = input("Enter name to delete: ")
        for s in self.students:
            if s.name.lower() == name.lower():
                self.students.remove(s)
                self.save_students()
                print("Student Deleted ✅")
                return
        print("Student Not Found ❌")

    # Update student
    def update_student(self):
        name = input("Enter name to update: ")
        for s in self.students:
            if s.name.lower() == name.lower():
                s.m1 = int(input("Enter new marks for Subject 1: "))
                s.m2 = int(input("Enter new marks for Subject 2: "))
                s.m3 = int(input("Enter new marks for Subject 3: "))
                s.calculate_result()
                self.save_students()
                print("Student Updated ✅")
                return
        print("Student Not Found ❌")


# ---------------------- Main Program ----------------------
def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.update_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("Exiting... 👋")
            break
        else:
            print("Invalid Choice ❌")

if __name__ == "__main__":
    main()