#importing function from another file
from name_functions import format_name
name=['Ali','Jack','Simon']
#printing formatted names for number of places in the list
for n in name:
    print(format_name(n))