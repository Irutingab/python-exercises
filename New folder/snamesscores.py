# Create, Read, update and delete
students = {"Raissa": 80, "Cristal": 90, "Tessy": 78}

def readstudent(name):
    return students.get(name, "Student not found.")

def updatescore(name, score):
    if name in students:
        students[name] = score
        return f"{name}'s score updated to {score}."
    else:
        return "Student not found."

def deletestudent(name):
    return students.pop(name, "Student not found.")

#example
print(readstudent("Raissa"))
print(updatescore("Raissa", 98))
print(students)
