class Library:
    def __init__(self, city:str, street:str, zipcode:str, open_hours:str, phone:str):
        self.city = city
        self.street = street
        self.zipcode = zipcode
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library({self.city}, {self.street}, {self.zipcode}, {self.open_hours}, {self.phone})"


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
        return f"Employee({self.first_name} {self.last_name}, phone: {self.phone})"


class Student:
    def __init__(self, first_name, last_name, index_number):
        self.first_name = first_name
        self.last_name = last_name
        self.index_number = index_number

    def __str__(self):
        return f"Student({self.first_name} {self.last_name})"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book({self.author_name}, {self.author_surname}, {self.number_of_pages})"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_titles = ", ".join([f"{b.author_name} {b.author_surname}" for b in self.books])

        return (f"Zamówienie(({self.order_date}),\n"
                f"employee={self.employee},\n"
                f"student={self.student},\n"
                f"books=[{books_titles}])")


library1 = Library("Katowice", "Plac Rady Europy 1", "40-021", "08:00-20:00", "32 208 37 40")
library2 = Library("Gliwice", "Kościuszki 17", "44-100", "08:00-20:00", "32 238 25 10")

employee1 = Employee("Tomek", "Halman", "1999-12-15", "1980-04-09", "Katowice", "Polna 69", "40-021", "726765437")
employee2 = Employee("Anna", "Jelenska", "2022-02-15", "1989-04-23", "Katowice", "Szafirowa 12", "40-021", "726744437")
employee3 = Employee("Patrycja", "Kotlorz", "2020-01-40", "1988-02-10", "Gliwice", "Zielona 22", "44-109", "888280989")

student1 = Student("Klara", "Kowalski", "14455")
student2 = Student("Michał", "Nowak", "92939")
student3 = Student("Karolina", "Picheta", "92123")


book1 = Book(library1, "2022", "Daniel", "Kahneman", 672)
book2 = Book(library1, "2019", "James", "Clear", 286)
book3 = Book(library2, "2017", "Ichiro", "", 264)
book4 = Book(library2, "2018", "Mel", "Robbins", 256)
book5 = Book(library1, "2023", "Brianna", "Wiest", 600)

order1 = Order(employee1, student1, [book3, book4], "2025-12-20")
order2 = Order(employee2, student3, [book1, book2, book5], "2025-12-21")

print(order1)
print(order2)
