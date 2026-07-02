account_balance= 1000
pin=1234
print(f'---------ATM----------')
input("Insert Atm Card:")
pin1= int(input('Enter Your Pin: '))
if pin!=pin1:
    print("Invalid Pin")
elif pin==pin1:
    amount= float(input("Enter Withdrawal Amount:  "))
    if amount > account_balance:
        print('Insufficient funds')
    elif amount<=account_balance:
        print(f'Dispensing Cash........')
        print(f'Printing Receipt........')
        print(f'Please Take Your Card')



print(f'------------------------------------------------------------------')