score= float(input("Enter Score: "))
while score<0 or score>100:
        score= float(input("Enter Score: "))
if score>=80:
                grade= 'A'
elif score>=60:
                grade= 'B'
elif score>=50:
                grade= 'C'
else:
                grade= 'F'
print("Grade: ", grade)
