import json
import os


class Student:
    def __init__(self, name, age, parents):
        self.name = name
        self.age = age
        self.parents = parents if parents else []

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        if self.parents:
            print("Parents: " + ", ".join(self.parents))
        else:
            print("The student doesn't have any parent.")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "parents": self.parents
        }

    @staticmethod
    def from_dict(data):
        return Student(data["name"], data["age"], data["parents"])

def load_students(filename="students.json"):
    """Load students from a JSON file."""
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as file:
        data = json.load(file)
        return {name: Student.from_dict(info) for name, info in data.items()}


def save_students(students, filename="students.json"):
    with open(filename, "w") as file:
        data = {name: student.to_dict() for name, student in students.items()}
        json.dump(data, file, indent=4)
        print("\n--- Student data saved to file! ---")


def add_student():
    while True:
        name = input("Enter the student's name: ")
        if name:
            break
        print("Invalid input. Name cannot be empty. Please try again.")

    while True:
        try:
            age = int(input("Enter the student's age: "))
            if age > 0:
                break
            else:
                print("Age must be a positive number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        print("\nChoose from the options provided below:")
        print("1. Both parents are alive")
        print("2. At least one parent is alive")
        print("3. No parents are alive")
        
        parental_choice = input("Enter the number corresponding to your answer (1/2/3): ")
        
        if parental_choice == "1":
            father_name = input("Father's name: ")
            mother_name = input("Mother's name: ")
            
            if father_name and mother_name:
                parents = [father_name, mother_name]
                break
            else:
                print("Both parents' names are required. Please try again.")
        elif parental_choice == "2":
            alive_parent = input("Enterthe parent's name: ")
        
            if alive_parent:
                parents = [alive_parent]
                break
            else:
                print("Parent name is required. Please try again.")
        elif parental_choice == "3":
            parents = []
            print("The student doesn't have any parent.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    return Student(name, age, parents)


def main():
    filename = "students.json"
    students = load_students(filename)  
    
    while True:
        print("\n--- Add a New Student ---")
        student = add_student()
        students[student.name] = student
        print("\n--- Student Added Successfully! ---")
        student.display_info()

        while True:
            another = input("\nWould you like to add another student? (yes/no): ")
            if another in ["yes", "no"]:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        if another == "no":
            break

    save_students(students, filename)  

    while True:
        print("\n--- Access Student Records ---")
        access_name = input("Enter the name of the student you want to access (or 'none' to exit): ")
        if access_name.lower() == "none":
            print("Exiting the program.")
            break
        elif access_name in students:
            print("\n--- Student Information ---")
            students[access_name].display_info()
        else:
            print(f"Student with name '{access_name}' not found. Please try again.")


if __name__ == "__main__":
    main()
