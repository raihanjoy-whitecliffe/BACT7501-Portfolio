snum=7
print("-------------------------------")
num= int(input("Guess the number: "))
while num!=snum:
    if num>snum:
        print("Too high")
        num= int(input("Guess the number: "))
    elif num<snum:
        print("Too low")
        num= int(input("Guess the number: "))
print("Correct!")
print("-------------------------------")