from student import Student


class StudentManagementSystem:

    def __init__(self):
        self.students = []

    def add_student(self):

        n = int(input("How many students do you want to add? : "))

        for i in range(n):

            print(f"\nEnter Details of Student {i+1}")

            while True:
                student_id = int(input("Enter Student ID : "))

                is_duplicate = False

                for student in self.students:
                    if student.student_id == student_id:
                        is_duplicate = True
                        break

                if is_duplicate:
                    print("Student ID already exists!")
                else:
                    break

            name = input("Enter Student Name : ")
            age = int(input("Enter Age : "))
            marks = float(input("Enter Marks : "))

            student = Student(student_id, name, age, marks)

            self.students.append(student)

        print(f"\n{n} Students Added Successfully!")

    def view_students(self):

        if len(self.students) == 0:
            print("No Students Found!")

        else:
            print("\n----- Student Details -----")

            for student in self.students:
                student.display()

    def search_student(self):

        student_id = int(input("Enter Student ID to Search : "))

        for student in self.students:

            if student.student_id == student_id:

                print("\nStudent Found!")
                student.display()
                return

        print("Student Not Found!")

    def update_marks(self):

        student_id = int(input("Enter Student ID : "))

        for student in self.students:

            if student.student_id == student_id:

                new_marks = float(input("Enter New Marks : "))
                student.marks = new_marks

                print("Marks Updated Successfully!")
                return

        print("Student Not Found!")

    def delete_student(self):

        student_id = int(input("Enter Student ID : "))

        for student in self.students:

            if student.student_id == student_id:

                self.students.remove(student)

                print("Student Deleted Successfully!")
                return

        print("Student Not Found!")

    def display_topper(self):

        if len(self.students) == 0:
            print("No Students Available!")

        else:

            topper = self.students[0]

            for student in self.students:

                if student.marks > topper.marks:
                    topper = student

            print("\n----- Topper Details -----")
            topper.display()