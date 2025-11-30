import datetime

class ExpenseTracker:

    def __init__(self):

        # Predefined expenses dictionary with dates as keys

        self.expenses = {

            "2022-01-01": [
                {"category": "Food", "amount": 200, "description": "Breakfast"},
                {"category": "Transport", "amount": 30, "description": "Bus fare"}
            ],
            "2022-01-02": [
                {"category": "Rent", "amount": 5000.00, "description": "Monthly rent"},
                {"category": "Food", "amount": 200.00, "description": "Dinner"}
            ],
            "2022-01-03": [
                {"category": "Entertainment", "amount": 500.00, "description": "Movie ticket"},
                {"category": "Transport", "amount": 100.00, "description": "Taxi fare"}
            ]
        }

    def add_expense(self, amount, category, description=""):

        """Add an expense to today's date."""

        date = datetime.date.today().strftime("%Y-%m-%d")  # Get today's date

        if date not in self.expenses:

            self.expenses[date] = []  # Initialize a new date entry if not present
        
        self.expenses[date].append({
            "category": category,
            "amount": amount,
            "description": description
        })

        print("\nExpense added successfully.")





    def view_summary(self):

        """Display total expenses and breakdown by category."""

        if not self.expenses:

            print("\nNo expenses recorded yet.")

            return

        total_expense = 0
        category_summary = {}


        for date in self.expenses:

            for expense in self.expenses[date]:

                total_expense += expense["amount"]
                category = expense["category"]
                category_summary[category] = category_summary.get(category, 0) + expense["amount"]

        print("\nExpense Summary:")
        print(f"Total Expenses: ₹{total_expense:.2f}")
        print("\nBy Category:")

        for category in category_summary:
            print(f"  - {category}: ₹{category_summary[category]:.2f}")



    def list_expenses(self):

        """Display all recorded expenses by date."""

        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return

        print("\nAll Expenses:")

        for date in sorted(self.expenses):
            print(f"\nDate: {date}")

            index = 1  # Manual index tracking

            for expense in self.expenses[date]:
                print(
                    f"  {index}. Amount: ₹{expense['amount']:.2f}, "
                    f"Category: {expense['category']}, Description: {expense['description']}"
                )
                index += 1  # Increment index manually





def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expense Summary")
        print("3. List All Expenses")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":

            try:
                amount = float(input("Enter the amount: ₹"))
                category = input("Enter the category (e.g., Food, Transport, Rent, etc.): ")
                description = input("Enter a description (optional): ")
                tracker.add_expense(amount, category, description)

            except ValueError:
                print("Invalid amount! Please enter a valid number.")

        elif choice == "2":
            tracker.view_summary()

        elif choice == "3":
            tracker.list_expenses()

        elif choice == "4":
            print("Goodbye! Have a great day.")
            break

        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
