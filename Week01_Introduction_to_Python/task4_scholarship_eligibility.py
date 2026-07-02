#This is a simple code to check a students eligibility to get a scholarship asking users full name, age, gpa, state of being domestic or not, and annual family income.
# done by MD Raihan Joy on 25th Feb,2026.
full_name= input('Enter your full name: ')   #string is automatically used by quotations
age= int(input('Enter your age: '))      #integer is used as age must be a whole number not in decimal
domestic_student= str(input('Are You a Domestic Student? (Yes/No): '))  #string is used to specifically take words only( Yes/ No)
gpa= float(input('Enter your GPA: '))    #float is used as gpa can be in decimal
annual_family_income= float(input('Enter your Annual Family Income: '))   #float is used as income can be in decimal
if domestic_student == 'Yes':
    if gpa>= 8.5 and annual_family_income<40000:
        print(f'------------SCHOLARSHIP RESULT-----------')
        print(f'STUDENT:{full_name}')
        print(f'Age: {age}')
        print(f'GPA: {gpa}')
        print(f'Congratulations! You qualify for FULL SCHOLARSHIP.')
        print(f'-----------------------------------------')
else:
    print(f'You are not eligible for SCHOLARSHIP.')