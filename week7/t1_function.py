#defining function
def marks(*args):
    #initializing Sum
    sum = 0
    #calcualtion using for loop for all numbers in args
    for i in args:
        #get total
        sum += i
        #calculating average
    avg = sum / len(args)
    #printing average
    print('Average Mark=',avg)
    #checking pass or fail
    if avg>=50:
        print('Pass')
    else:
        print('Fail')