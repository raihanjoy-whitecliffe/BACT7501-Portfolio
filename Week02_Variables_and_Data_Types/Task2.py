total_items= int(input('How Many Items? '))
runningtotal=0
subtotal1=0
for i in range(total_items):
    Item_Name= input(f'Item {i+1} Name:   ')
    Price=float(input('Price:   '))
    Quantity=int(input('Quantity:   '))
    subtotal= Price*Quantity
    subtotal1= subtotal1 + subtotal
    runningtotal= runningtotal + subtotal1

gst15percent= subtotal1 *.15
alltotal= runningtotal + gst15percent
print(f'---------Billing---------')
print(f'How Many Items? : {total_items}')
for j in range(total_items):
    print(f'Item {j+1} Name: {Item_Name}')
    print(f'Price: {Price}')
    print(f'Quantity: {Quantity}')
    print(f'Subtotal: {subtotal}')
    print(f'                ')
    print(f'                ')
    print(f'                ')
print(f'Gst (15%) : {gst15percent}')
print(f'Total: ${alltotal}')
print(f'---------------------------')
