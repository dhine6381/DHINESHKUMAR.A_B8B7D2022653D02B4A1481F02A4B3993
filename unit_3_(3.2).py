
def sort_students(students):
    students.sort(key=lambda x: x.cgpa, reverse=True)
    return students

class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa
        
students = [
    Student("John", "1001", 3.5),
    Student("Jane", "1002", 3.2),
    Student("David", "1003", 3.8),
    Student("Sarah", "1004", 3.6)
]

sorted_students = sort_students(students)
for student in sorted_students:
    print(student.name, student.roll_number,student.cgpa)