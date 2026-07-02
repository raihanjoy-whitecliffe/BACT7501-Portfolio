def score(num1):
    #storing grade
    grade=''
    #checking scores for grades
    if num1 >= 80:
        grade = 'A'
    elif num1 >=60:
        grade = 'B'
    elif num1 >= 50:
        grade = 'C'
    elif num1 < 50:
        grade = 'F'
    return grade