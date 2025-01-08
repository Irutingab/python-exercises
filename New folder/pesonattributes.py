class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Example 
person1 = Person("Raissa", 19) 
person1.display()             

person2 = Person("Tessy", 21)   
person2.display()              
