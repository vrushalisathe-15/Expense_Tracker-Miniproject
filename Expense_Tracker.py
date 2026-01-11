import csv
from datetime import date
EXPENSES_FILE = 'expenses.csv'
try:
    with open(EXPENSES_FILE, 'x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
except FileExistsError:
    pass
def add_expense():
    expense_date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not expense_date:
        expense_date = str(date.today())
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    with open(EXPENSES_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([expense_date, category, amount, description])
    print("Expense added successfully.")
def view_expenses():
    print("Date\t\tCategory\tAmount\tDescription")
    print("-" * 50)
    try:
        with open(EXPENSES_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
    except FileNotFoundError:
        print("No expenses recorded yet.")
def total_expenses():
    total = 0.0
    try:
        with open(EXPENSES_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
        print(f"Total Expenses: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet.")
def category_summary():
    summary = {}
    try:
        with open(EXPENSES_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[2])
                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount
        print("Category Summary:")
        for category, amount in summary.items():
            print(f"{category}: ${amount:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

    
while True:
    print("Expense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expenses()
    elif choice == '4':
        category_summary()
    elif choice == '5':
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
