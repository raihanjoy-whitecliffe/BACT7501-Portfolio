#This is a simple code of a Mini billing system to calculate a users bill by asking the item name, item price, quantity purchased.
# done by MD Raihan Joy on 25th Feb,2026.
item_name= input("Enter the Name of the Item: ")         #automatically a string ""
item_price= float(input("Enter the Item Price: "))       #float used for prices in decimal
quantity_purchased= int(input("Enter the Quantity Purchased: ")) #integer used as quantity must be in whole numbers
total_cost= item_price * quantity_purchased               #summing up the cost without gst
gst_15percent= total_cost * 0.15                          #Total gst for the purchase
final_price_including_gst= total_cost + gst_15percent     #total price with gst of 15%
print(f'------ RECEIPT ------')                           #printing the heading of the receipt as per expected output
print(f'Item: {item_name}')                               #printing the item name as per expected output
print(f'Price per item: ${item_price}')                   #printing the price of each item as per expected output
print(f'Quantity: {quantity_purchased}')                  #printing the quantity of items purchased as per expected output
print(f'Subtotal: ${total_cost}')                         #printing the total cost without gst as per expected output
print(f'GST(15%): ${gst_15percent : .2f}')                     #printing the total gst added as per expected output
print(f'Total: ${final_price_including_gst : .2f}')             #printing the final price with gst as per expected output
