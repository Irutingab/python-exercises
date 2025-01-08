class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)  
        self.student_id = student_id
        self.major = major

    def display(self):
        """
        Display the details of the student.
        """
        super().display()  
        print(f"Student ID: {self.student_id}, Major: {self.major}")


class Teacher(Person):
    def __init__(self, name, age, teacher_id, subject):
        super().__init__(name, age)  
        self.teacher_id = teacher_id
        self.subject = subject

    def display(self):
        super().display() 
        print(f"Teacher ID: {self.teacher_id}, Subject: {self.subject}")


# Example 
student = Student("Raissa", 19, "S12345", "Software Engineering")
teacher = Teacher("Tessy", 21, "T98765", "Business Administration")

print("Student Details:")
student.display()

print("\nTeacher Details:")
teacher.display()
