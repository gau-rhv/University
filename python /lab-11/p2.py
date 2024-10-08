class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display_attributes(self):
        print(f"ID: {self.student_id}, Name: {self.student_name}, Class: {self.student_class}")

student1_id = input("Enter ID for student 1: ")
student1_name = input("Enter name for student 1: ")
student1_class = input("Enter class for student 1: ")

student2_id = input("Enter ID for student 2: ")
student2_name = input("Enter name for student 2: ")
student2_class = input("Enter class for student 2: ")

student1 = Student(student1_id, student1_name, student1_class)
student2 = Student(student2_id, student2_name, student2_class)

student1.display_attributes()
student2.display_attributes()