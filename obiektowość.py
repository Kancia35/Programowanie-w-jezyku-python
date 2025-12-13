class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50


student1 = Student("Karolina", [60, 70, 80])   # średnia > 50
student2 = Student("Ala", [30, 40, 50])  # średnia <= 50

print(student1.is_passed())  # True
print(student2.is_passed())  # False
