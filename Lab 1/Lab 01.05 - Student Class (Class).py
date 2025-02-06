"""Student Class (Class)"""

class Student:
    def __init__(self, name, gender, age, id, gpa):
        self.name = name
        self.gender = gender
        self.age = age
        self.id = id
        self.gpa = gpa

student_list = []
for _ in range(3):
    student_list.append(Student(input(), input(), input(), input(), input()))
id_selected = input()

def show_student():
    for i in range(3):
        if student_list[i].id == id_selected:
            data = student_list[i]
            pronoun = "Mr" if data.gender == "Male" else "Miss"
            result = f"{pronoun} {data.name} ({data.age}) ID: {data.id} GPA {float(data.gpa):.2f}"
            return result
    return "Student not found"

print(show_student())
