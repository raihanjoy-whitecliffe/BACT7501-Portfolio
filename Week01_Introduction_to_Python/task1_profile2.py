#This is a simple code to generate a users personal profile by asking their fullname, age, height and favourite programming language
# done by MD Raihan Joy on 25th Feb,2026.
Full_name= (input("Enter your Full Name: ") ) #asking for a users Name as input
Age= int(input("Enter your Age: ") ) #asking for a users current age as input
Height= float(input("Enter your Height(in meters): ")) #asking for users height in meters as input in float
Favourite_programming_Language= str(input("Enter your Favourite Programming Language: ")) # Takes input of the users
# as String
Height2= Height*100 #covertion of height from meters to centimeters for the expected output
Age2= Age+1 #for the users age next year
                                        #printing the profile summary
print("--------- PROFILE SUMMARY ---------")
print(f'You are {Full_name}')
print(f'Next year you will be {Age2} years old')
print(f'Your Height in cm is {Height2} cm')
print(f'You Love Programming in {Favourite_programming_Language}!')
#end