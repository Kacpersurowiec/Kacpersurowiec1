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