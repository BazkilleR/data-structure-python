"""Student Class"""

def student():
    students = []

    for _ in range(3):
        student_data = []
        for _ in range(5):
            student_data.append(input())
        students.append(student_data)
    id_select = input()

    for i in range(3):
        if students[i][3] == id_select:
            select_index = i
            pronoun = "Mr" if students[select_index][1] == "Male" else "Miss"
            name = students[select_index][0]
            age = students[select_index][2]
            id = students[select_index][3]
            gpa = students[select_index][4]
            gpa = f"{float(gpa):.2f}"
            result = pronoun + " " + name + " (" + age + ") " + "ID: " + id + " GPA " + gpa
            return result
    return "Student not found"

print(student())
