from datetime import date
class Expense:
    def __init__(self,amount,category,description="",expense_date=None):
        self.amount=float(amount)
        self.category=category
        self.description=description
        self.date=expense_date if expense_date else date.today().isoformat()
    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount} | {self.description}"
    
expenses=[]

def add_expense():
    amount=input("Enter the amount: ")
    category=input("Enter the category: ")
    description=input("Enter the description: ")
    try:
        expense=Expense(amount,category,description)
        expenses.append(expense)
        print("Expense added")
    except ValueError:
        print("Invalid amount. Please enter a number.\n")

def view_expense():
    if not expenses:
        return f"No expenses recorded"
    else:
        print("\nAll expenses")
        for exp in expenses:
            print(exp)
def total_by_category():
    if not expenses:
        print("No expenses recorded")
        return
    category=input("Enter category to calculate total: ")
    total=sum(exp.sum for exp in expenses if exp.category.lower()==category.lower())
    print("\nSum of the category: {total}\n")


while True:
    print("=============================")
    print("      Expense Tracker       ")
    print("=============================")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. View total by category")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        total_by_category()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-4.\n")
