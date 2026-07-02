from os import remove

shopping_list=[]
item_name= ''
while item_name!= 'done':
    item_name= input("Enter Item: ")
    if item_name != 'done':
        shopping_list.append(item_name)
print('shopping list', shopping_list)
#print('First two item:', shopping_list[0:3])
print('Last item: ', shopping_list[-1])
del shopping_list[len(shopping_list)-1]
print('Shopping list', shopping_list)