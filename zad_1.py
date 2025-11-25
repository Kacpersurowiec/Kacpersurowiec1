
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        srednia = sum(self.marks) / len(self.marks)
        return srednia > 50


student1 = Student("Kamil", [100, 50, 20])
student2 = Student("Kamila", [90, 20, 10])

print(student1.is_passed())
print(student2.is_passed())