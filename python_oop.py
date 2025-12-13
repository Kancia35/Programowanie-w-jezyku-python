class Student(object):
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        average = sum(self.marks) / len(self.marks)
        return average > 50


student_passed = Student("Karolina Skorulska", [60, 70, 80])
student_failed = Student("Alicja Skorulska", [30, 40, 50])

print(f"{student_passed.name} zdał: {student_passed.is_passed()}")
print(f"{student_failed.name} zdał: {student_failed.is_passed()}")




