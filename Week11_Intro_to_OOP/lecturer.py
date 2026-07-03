#making a class called lecturer
class Lecturer:
#passing lecturer details from the object
    def __init__(self, lecturer_name, department, course, years_experience):
        self.lecturer_name = lecturer_name
        self.department = department
        self.course = course
        self.years_experience = years_experience
#printing lecturer name, department, course, and experience
    def display_info(self ):
        print("Lecturer Name: ", self.lecturer_name)
        print("Department: ", self.department)
        print("Course: ", self.course)
        print("Years Experience: ", self.years_experience)
    def check_experience(self):
        if self.years_experience >= 5:
            print("Experienced Lecturer")
        else:
            print("Junior Lecturer")
#object having information about a lecturer which is passed in the __init__ method
lecturer= Lecturer("Sarah Ahmed", "Information Technology", "Python Programming", 5)
#executes line 7 to 11, and prints the details of the lecturer
lecturer.display_info()
#executes line 12 to 16, and prints whether the lecturer is experienced or a junior lecturer
lecturer.check_experience()