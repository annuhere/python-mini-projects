#mini project: Expense Tracker

#Question/problem statement: create a console-based expense tracker program in python that allows the user to record daily expenses abd view summaries like total spending. use only the concepts learned till chapter6(loop,copnditions,lists,dictionaries,basic input/output).

#project details/ description:
#you are requied to build a simple personal finance management tool.

#the program should allow the user to:
#1.add an expense with details like date,category,description,and amount.
#2.view all recorded expenses.
#3.calculate total spending so far.
#4.exit the program gracefully when the user chooses to.

#all tasks must be implemented using loops,if-else,lists,and dictuonaries on;ly.no user-defined function or file handling should be used.

expenses=[ ] #list of expenses in form of dictionaries
print("Welcome to the Expense Tracker!")
while True:
    print("=====MENU=====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice=int(input("Enter your choice(1-4): "))

#Add Expense
    if(choice==1):
        date=input("Enter the date(yyyy-mm-dd):")
        category=input("Enter the category(food,transportation,utilities,etc):")
        description=input("Enter a brief description of the expense:")
        amount=float(input("Enter the amount spent:"))
        expense={
            "Date":date,
            "Category":category,
            "Description":description,
            "Amount":amount
        }
        expenses.append(expense)
        print("Expense added successfully!")

#View All Expenses
    elif(choice==2):
        if len(expenses)==0:
            print("No expenses recorded yet.")
        else:
            print("Recorded Expenses:")
            count=1
            for expense in expenses:
                print(f"Expense {count} -> Date: {expense['Date']}, Category: {expense['Category']}, Description: {expense['Description']}, Amount: ${expense['Amount']}")
                count += 1

#View Total Spending
    elif(choice==3):
        total_spending=0
        for expense in expenses:
            total_spending += expense['Amount']
        print(f"Total Spending so far: ${total_spending}")

#Exit
    elif(choice==4):
        print("Exiting the Expense Tracker. Goodbye!")
        break

#if user enters invalid choice
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

