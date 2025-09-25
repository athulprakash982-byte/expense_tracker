from datetime import date
class Expense:
    def __init__(self,amount,category,description="",expense_date=None):
        self.amount=float(amount)
        self.category=category
        self.description=description
        self.date=expense_date if expense_date else date.today().isoformat()
    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount} | {self.description}"
        