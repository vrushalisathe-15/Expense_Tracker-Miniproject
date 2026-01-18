import sqlite3
from datetime import datetime  
def create_table():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT
        )
    ''' )
    conn.commit()
    conn.close()

            
def add_expense():
    expense_date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not expense_date:
        expense_date = datetime.now().strftime('%Y-%m-%d')
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    conn=sqlite3.connect('expenses.db')
    cursor=conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
    ''', (expense_date, category, amount, description))
    conn.commit()
    conn.close()
    print("Expense added successfully.")
def view_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    print("Expenses:")
    for row in rows:
        print(f"ID: {row[0]}, Date: {row[1]}, Category: {row[2]}, Amount: ${row[3]:.2f}, Description: {row[4]}")
    conn.close()
def total_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(amount) FROM expenses')
    total = cursor.fetchone()[0]
    total = total if total is not None else 0.0
    print(f"Total Expenses: ${total:.2f}")
    conn.close()
def category_summary():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    rows = cursor.fetchall()
    print("Category Summary:")
    for row in rows:
        print(f"Category: {row[0]}, Total Amount: ${row[1]:.2f}")
    conn.close()
def delete_expense():
    expense_id = input("Enter Expense ID to delete: ")

    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
    row = cursor.fetchone()

    if row is None:
        print("❌ No expense found with that ID.")
    else:
        print(f"You are about to delete: ID:{row[0]}, Date:{row[1]}, Category:{row[2]}, Amount:${row[3]:.2f}, Description:{row[4]}")
        confirm = input("Are you sure? (Y/N): ").strip().lower()
        if confirm == 'y':
            cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            conn.commit()
            print("✅ Expense deleted successfully.")
        else:
            print("❌ Deletion cancelled.")

    conn.close()


create_table()
while True:
    print("Expense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Delete Expense")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expenses()
    elif choice == '4':
        category_summary()
    elif choice == '5':
        delete_expense()
    elif choice == '6':
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
