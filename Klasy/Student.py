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
