total_items= int(input('How Many Items? '))
runningtotal=0
#subtotal1=0
for i in range(total_items):
    Item_Name= input(f'Item {i+1} Name:   ')
    Price=float(input('Price:   '))
    Quantity=int(input('Quantity:   '))
    #subtotal1= subtotal1 + subtotal
    subtotal = Price * Quantity
    runningtotal= runningtotal + subtotal
    print(f'Subtotal: {subtotal}')

gst15percent= runningtotal *.15
alltotal= runningtotal + gst15percent
print(f'---------Billing---------')
print(f'How Many Items? : {total_items}')
print(f'Subtotal: {runningtotal}')
print(f'Gst (15%) : {gst15percent}')
print(f'Total: ${alltotal}')
print(f'---------------------------')
