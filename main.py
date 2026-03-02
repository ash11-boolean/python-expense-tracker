import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


# -----------------------------
# Load Data
# -----------------------------
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


# -----------------------------
# Save Data
# -----------------------------
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# -----------------------------
# Add Transaction
# -----------------------------
def add_transaction(data, transaction_type):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        transaction = {
            "type": transaction_type,
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        data.append(transaction)
        save_data(data)

        print("✅ Transaction added successfully!\n")

    except ValueError:
        print("❌ Invalid amount. Please enter a number.\n")


# -----------------------------
# View Transactions
# -----------------------------
def view_transactions(data):
    if not data:
        print("No transactions found.\n")
        return

    for i, transaction in enumerate(data, start=1):
        print(f"{i}. [{transaction['type']}] ${transaction['amount']} - "
              f"{transaction['category']} - {transaction['description']} "
              f"({transaction['date']})")

    print()


# -----------------------------
# Calculate Balance
# -----------------------------
def calculate_balance(data):
    income = sum(t["amount"] for t in data if t["type"] == "Income")
    expense = sum(t["amount"] for t in data if t["type"] == "Expense")
    balance = income - expense

    print(f"\nTotal Income: ${income}")
    print(f"Total Expenses: ${expense}")
    print(f"Current Balance: ${balance}\n")


# -----------------------------
# Main Menu
# -----------------------------
def main():
    data = load_data()

    while True:
        print("====== EXPENSE TRACKER ======")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Balance")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_transaction(data, "Income")
        elif choice == "2":
            add_transaction(data, "Expense")
        elif choice == "3":
            view_transactions(data)
        elif choice == "4":
            calculate_balance(data)
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()