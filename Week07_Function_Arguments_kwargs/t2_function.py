#defining function adding kwargs which is similar to a dict
def fruit_price(**kwargs):
    #initializing sum
    sum=0
    #running for-loop for all values passed in the keyword argument
    for i in kwargs.keys():
        #sum of the values for keys in kwargs
        print(i)