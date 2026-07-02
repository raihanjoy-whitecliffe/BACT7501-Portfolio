def print_results(student):
    #student_name = student{}
    #student_marks = student{}
    for k,v in student.items():
        if v >= 60:
            status = 'Pass'
            print(k,v,status)
        else:
            status = 'Fail'
            print (k,v,status)
student = {
    "John": 65,
    "Mary": 82,
    "Ali": 55,
    "Sina": 90
}
print_results(student)

