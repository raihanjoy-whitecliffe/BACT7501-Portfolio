class Student:
    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

    def display_info(self):
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)


student1 = Student("Ali", "Cybersecurity", 68)
student2= Student("Bob", "Software and Web", 90)
student3= Student("David", "Art and Design", 88)
print(student1.name)
student1.display_info()
student2.display_info()
student3.display_info()