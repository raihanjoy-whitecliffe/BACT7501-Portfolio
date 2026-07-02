def validate_student(name, age, email)
    name = input()
    age = int(input())
    email=input()
    if name.strip() == "":
        print("Invaid")
    elif age.isdigit():
        if int(age) > 18 or int(age) < 60:


