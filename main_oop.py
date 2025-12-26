from oop.student import Student


def run_example():
    student_passed = Student("Karolina Skorulska", [60, 70, 80])
    student_failed = Student("Alicja Skorulska", [30, 40, 50])

    print(f"{student_passed.name} zdała: {student_passed.is_passed()}")
    print(f"{student_failed.name} zdała: {student_failed.is_passed()}")


if __name__ == "__main__":
    run_example()
