from datetime import date

# ----- Klasy -----

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Biblioteka: {self.city}, {self.street}, {self.zip_code}, "
                f"Godziny otwarcia: {self.open_hours}, Tel: {self.phone}")


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Pracownik: {self.first_name} {self.last_name}, "
                f"Zatrudniony: {self.hire_date}, Tel: {self.phone}")


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50

    def __str__(self):
        return f"Student: {self.name}, Zaliczenie: {self.is_passed()}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Książka: {self.author_name} {self.author_surname}, "
                f"Rok wydania: {self.publication_date}, "
                f"Liczba stron: {self.number_of_pages}\n"
                f"  {self.library}")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n".join([str(book) for book in self.books])
        return (f"Zamówienie z dnia: {self.order_date}\n"
                f"{self.employee}\n"
                f"{self.student}\n"
                f"Książki:\n{books_str}\n")


# ----- Tworzenie obiektów -----

# Biblioteki
library1 = Library("Warszawa", "Marszałkowska 1", "00-001", "8-18", "123456789")
library2 = Library("Kraków", "Długa 5", "30-001", "9-17", "987654321")

# Książki
book1 = Book(library1, 2010, "Adam", "Mickiewicz", 350)
book2 = Book(library1, 2015, "Henryk", "Sienkiewicz", 420)
book3 = Book(library2, 2005, "Bolesław", "Prus", 300)
book4 = Book(library2, 2020, "Olga", "Tokarczuk", 280)
book5 = Book(library1, 2018, "Stanisław", "Lem", 500)

# Pracownicy
employee1 = Employee("Jan", "Kowalski", date(2020, 1, 1), date(1985, 5, 10),
                     "Warszawa", "Krótka 2", "00-002", "111111111")
employee2 = Employee("Anna", "Nowak", date(2019, 3, 15), date(1990, 7, 20),
                     "Kraków", "Długa 10", "30-002", "222222222")
employee3 = Employee("Piotr", "Wiśniewski", date(2021, 6, 1), date(1995, 2, 5),
                     "Warszawa", "Prosta 7", "00-003", "333333333")

# Studenci
student1 = Student("Tomasz", [60, 70, 80])
student2 = Student("Kasia", [40, 45, 50])
student3 = Student("Marek", [90, 85, 88])

# Zamówienia
order1 = Order(employee1, student1, [book1, book2, book5], date(2024, 1, 10))
order2 = Order(employee2, student2, [book3, book4], date(2024, 2, 5))

# ----- Wyświetlanie zamówień -----

print(order1)
print(order2)

