import markingcr as mr
score= float(input("Enter Score: "))
while score<0 or score>100:
        score= float(input("Enter Score: "))
grade= mr.score(score)
print("Grade: ", grade)