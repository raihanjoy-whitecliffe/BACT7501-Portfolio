course1= float(input("Enter Course1 Final Mark(out of 100): "))
course2= float(input("Enter Course2 Final Mark(out of 100):"))
course3= float(input("Enter Course3 Final Mark(out of 100):"))
course4= float(input("Enter Course4 Final Mark(out of 100):"))
total= course1+course2+course3+course4
avg= (total/400)*100
if avg>=85 :
        grade= 'A'
        remarks='Excellent'
elif avg>=75 and avg<=84:
        grade= 'B'
        remarks='Very Good'
elif avg>=65 and avg<=74:
        grade= 'C'
        remarks='Good'
elif avg>=50 and avg<=64:
        grade= 'D'
        remarks='Pass'
else :
        grade= 'F'
        remarks='Fail'
print(f'-------STUDENT RESULT-------')
print(f'Course1: {course1}')
print(f'Course2: {course2}')
print(f'Course3: {course3}')
print(f'Course4: {course4}')
print(f'Final Grade: {avg: .2f}%')
print(f'Grade: {grade}')
print(f'Remark:  {remarks}')
print(f'-----------------------------')