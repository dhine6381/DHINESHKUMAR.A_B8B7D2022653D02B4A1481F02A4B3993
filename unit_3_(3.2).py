
def sort_students(students):
    students.sort(key=lambda x: x.cgpa, reverse=True)
    return students

class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa
        
students = [
    Student("Dhineshkumar A", "2K22CS044", 3.5),
    Student("Gopinath N", "2K22CS055", 3.2),
    Student("Dhananchezhiyan S", "2K22CS039", 3.8),
    Student("Harikaran P", "2K22CS017", 3.6)
]

sorted_students = sort_students(students)
for student in sorted_students:
    print(student.name, student.roll_number,student.cgpa)