#PersonalBudgetTracker.py

import csv # imported csv 
import os # imported os to manipulate csv file opeations

# function which add transaction to csv file for both income and expense
def add_transaction(transaction_type,amount):
    with open('personal_savings_tracker.csv',mode='a', newline='') as file:
        csv_writer_file=csv.writer(file)
        csv_writer_file.writerow([transaction_type,amount])


# function to print savings after income and expenses are added and subtracted 
def savings_calculation():
    # initialised total income and expense variable to store , for performing operations 
    total_income=0
    total_expense=0
    
    with open('personal_savings_tracker.csv',mode='r')as file:
        # checking if file exists or not 
        if not os.path.exists('personal_savings_tracker.csv'):
            print("no such file directory")
            return 0
            # iterating through through row while checking the row is income or expense and performing add method
        else:
            readable_csv_file=csv.reader(file)
            for row in readable_csv_file:
                if row[0]=='Income':
                    total_income+=int(row[1])
                elif row[0]=='Expense':
                    total_expense+=int(row[1])
    savings=total_income-total_expense
    return savings

# added another function to clear file if user wants to start a new savings account
def clearfile():
    if os.path.exists('personal_savings_tracker.csv'):
        with open('personal_savings_tracker.csv',mode='w'):
            pass
            print("File cleared successfully\n")
    else:
        print("no such file exists")

while True:
    try:
        print("*****Welcome to  personal Expense tracker*********\n\n")
        print("select below operations to perform operations\n")
        print("choose  1 : ADD Income")
        print("choose  2 : ADD Expense")
        print("choose  3 : Savings")
        print("choose  4 : to clear file  ")
        print("choose  5 : to EXIT ")
        choice=int(input("Choose the operation to be performed: "))
        if choice==1:
            Income=int(input("enter income amount : "))
            add_transaction('Income',Income)
            print("income added successfully\n")
        elif choice==2:
            Expense=int(input("Enter Expense amount : "))
            add_transaction('Expense',Expense) # type: ignore
            print("Expense added successfully\n")
        elif  choice==3:
            savings=savings_calculation() # type: ignore
            print(f"savings amount = {savings}")
        elif choice==5:
            print("Opertion ended")
            break
        elif choice==4:
            clearfile()   
        else:
            
            print("enter a valid input")
    except Exception as e:
        print("invalid input please try with valid input")
        print(e)



