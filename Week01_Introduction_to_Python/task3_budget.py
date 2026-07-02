#This is a simple code to calculate a users total expense and remaining balance by asking their monthly income, rent, transport, food and entertainment cost.
# done by MD Raihan Joy on 25th Feb,2026.
monthly_income= float(input("Enter your Monthly Income: "))                  #Float is used as a data type because, the expense might be in decimal places and it would be easier for the program to understand and the user to stay problem free
rent=float(input("Enter your Rent: "))                                       #Float is used as a data type because, the expense might be in decimal places and it would be easier for the program to understand and the user to stay problem free
transport_cost= float(input("Enter your Transport Cost: "))                  #Float is used as a data type because, the expense might be in decimal places and it would be easier for the program to understand and the user to stay problem free
food_cost= float(input("Enter your Food Cost: "))                            #Float is used as a data type because, the expense might be in decimal places and it would be easier for the program to understand and the user to stay problem free
entertainment_cost= float(input("Enter your Entertainment Cost: "))          #Float is used as a data type because, the expense might be in decimal places and it would be easier for the program to understand and the user to stay problem free
total_expense= rent + transport_cost + food_cost + entertainment_cost
remaining_balance=  monthly_income - total_expense
print(f'---------------- Monthly Budget Calculator ----------------')
print(f'Total Expenses: ${total_expense}')
print(f'Remaining Balance: $ {remaining_balance}')
print(f'-----------------------------------------------------------')
