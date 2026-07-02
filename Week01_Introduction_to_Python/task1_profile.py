#This is a simple code to generate a users personal profile by asking their fullname, age, height
# and favourite programming language
Full_name= (input("Enter your Full Name: ") )
Age= int(input("Enter your Age: ") )
Height= float(input("Enter your Height(in meters): ")) #Takes input of the users Height as Float
Favourite_programming_Language= str(input("Enter your Favourite Programming Language: ")) # Takes input of the users
# as String
Height2= Height*100
print("--------- PROFILE SUMMARY ---------")
print("Name:",Full_name)
print("Next year you will be",Age,"years old")
print("Your Height in cm is",Height2, "cm")
print("You Love Programming in",Favourite_programming_Language,"!")