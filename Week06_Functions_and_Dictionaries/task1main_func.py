
#defining Function
def check_result(mark):
    grade= ''
    #checking mark for pass or fail
    if mark>= 60:
        grade= 'Pass'
    elif mark<60:
        grade= 'Fail'
    #returning what the output will be when I call function
    return grade
#list of marks
mark=[55, 70, 62, 40, 90]
#for number of slots in list, printing the marks stored and their state
for m in mark:
    print(m, check_result(m))