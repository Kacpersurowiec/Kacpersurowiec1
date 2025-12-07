class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library {self.city} {self.street} {self.zip_code} is opened: "
            f"{self.open_hours}, phone: {self.phone}"
        )


class Employee:
    def __init__(self, first_name, last_name, hire_date,
                 birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Employee: {self.first_name} {self.last_name}, "
            f"hired: {self.hire_date}, birth: {self.birth_date}, "
            f"address: {self.city}, {self.street}, {self.zip_code}, "
            f"tel: {self.phone}"
        )


class Book:
    def __init__(self, library, publication_date,
                 author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Book {self.author_name} {self.author_surname}, "
            f"publicated: {self.publication_date} has "
            f"{self.number_of_pages} pages and you can find it "
            f"in {self.library}"
        )


class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return (
            f"Student: {self.first_name} {self.last_name} "
            f"(ID: {self.student_id})"
        )


student_aga = Student("Agnieszka", "Wójcik", "S12345")
student_bartek = Student("Bartosz", "Lis", "S67890")
student_celina = Student("Celina", "Mazur", "S11223")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_titles = [str(book) for book in self.books]
        return (
            f"Order from day {self.order_date}, "
            f"Employee: {self.employee.last_name}, "
            f"Number of books: {len(book_titles)}"
        )


lib_1 = Library(
    city="Warszawa",
    street="Książkowa 10",
    zip_code="00-001",
    open_hours="9:00-18:00",
    phone="111-222-333"
)


lib_2 = Library(
    city="Kraków",
    street="Literacka 5",
    zip_code="30-005",
    open_hours="10:00-19:00",
    phone="444-555-666"
)


emp_anna = Employee(
    "Anna", "Kowalska", "2020-05-15",
    "1990-01-20", "Warszawa",
    "Słoneczna 1", "00-100", "700-100-100"
)
emp_piotr = Employee(
    "Piotr", "Nowak", "2018-09-01", "1985-11-11",
    "Kraków", "Gwiezdna 2", "30-200", "700-200-200"
)
emp_ewelina = Employee(
    "Ewelina", "Zielińska", "2022-01-10", "1995-07-07",
    "Warszawa", "Leśna 3", "00-300", "700-300-300"
)


book1 = Book(lib_2, '21-07-1999', 'Olga', 'Tokarczuk', 321)
book2 = Book(lib_1, "2015-11-20", "Adam", "Mickiewicz", 210)
book3 = Book(lib_1, "1999-05-01", "Maria", "Curie", 420)
book4 = Book(lib_2, "2021-08-05", "Zofia", "Nałkowska", 180)
book5 = Book(lib_2, "1988-02-28", "Henryk", "Sienkiewicz", 600)


order1 = Order(
    employee=emp_anna,
    student=student_aga,
    books=[book1, book2, book3, book4, book5],
    order_date='2025-10-10'
)


order2 = Order(
    employee=emp_piotr,
    student=student_bartek,
    books=[book1, book2, ],
    order_date='2024-11-10'
)


print(order1)
print(order2)
