class assessment:
    def __init__(self,student_name, assessment_name, marks):
        self.student_name = student_name
        self.assessment_name = assessment_name
        self.marks = marks
    def display_results(self):
        print("Student: ", self.student_name)
        print("Assessment: ", self.assessment_name)
        print("Marks: ", self.marks)
    def check_pass(self):
        if self.marks >=50:
            print("Result: Pass")
        else:
            print("Result: Fail")
student1 = assessment("Ali", "Python Lab", 72)
student1.display_results()
student1.check_pass()