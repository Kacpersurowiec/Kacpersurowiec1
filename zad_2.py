from Klasy.Library import Library
from Klasy.Employee import Employee
from Klasy.Book import Book
from Klasy.Student import Student
from Klasy.Order import Order

student_aga = Student("Agnieszka", "Wójcik", "S12345")
student_bartek = Student("Bartosz", "Lis", "S67890")
student_celina = Student("Celina", "Mazur", "S11223")


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
