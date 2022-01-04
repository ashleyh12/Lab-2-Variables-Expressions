# In the part, you will calculate your monthly savings by calculating your monthly income and total monthly expenses. For simplicity, we will use only one personal montly income, and the following expenses. For this problem, we assume that you share your apartment with 2 other flatmates and shared bills for rent, grocery, and internet bill. We also assume that you have two other personal expenses, cell phone bill and personal subscriptions (such as Netflix, Amazon prime, etc). Since these variables (monthly income, rent, grocery, ...) are subject to change, we want to write a program where it prompts its users to enter their monthly income and these expenses. 

# The program should prompt for monthly income, rent, grocery expense, cell phone bill, internet bill and personal subscriptions. Here rent, grocery expense and internet bill are shared expenses with 2 other people, therefore, you need to calculate rent per head, grocery expense per head, and internet bill per head. Eventually, you can add them together with your personal expenses (cell phone bill and personal subscriptions) to calculate your total personal monthly expenses. 

# Your program's output should be your total personal monthly saving, in 2 decimal places. 




#prompt to enter monthly income
monthly_income = float(input("Enter your monthly income: "))

#prompt to enter rent
rent = float(input("Enter your rent: "))

#prompt to enter grocery expense
groceries = float(input("Enter your grocery expense: "))

#prompt to enter internet bill
internet_bill = float(input("Enter your internet bill: "))

#prompt to enter cell phone bill 
cell_phone_bill = float(input("Enter your cell phone bill: "))

#prompt to enter the cost for personal subscriptions such as Netflix, Amazon, 
subscriptions = float(input("Enter your subscriptions bill: "))

#calculate per head expenses with shared bills 
per_head = (rent + groceries + internet_bill) / 3

#calculate total expenses 
total_expenses = (monthly_income - cell_phone_bill - subscriptions - per_head)

#calculate monthly saving and print it 2 decimal places.
monthly_savings = print(round(total_expenses,2)) 
