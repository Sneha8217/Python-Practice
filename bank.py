accounts = {}


def create_account():
    print("\n--- Create Account ---")

    account_number = input("Enter account number: ")

    if account_number in accounts:
        print("Account already exists.")
        return

    name = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial balance: "))

    if initial_balance < 0:
        print("Balance cannot be negative.")
        return

    accounts[account_number] = {
        "name": name,
        "balance": initial_balance
    }

    print("Account created successfully!")


def check_balance():
    print("\n--- Check Balance ---")

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found.")
        return

    account = accounts[account_number]

    print("Account Holder:", account["name"])
    print("Balance:", account["balance"])


def deposit():
    print("\n--- Deposit Money ---")

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter deposit amount: "))

    if amount <= 0:
        print("Enter a valid amount.")
        return

    accounts[account_number]["balance"] += amount

    print("Deposit successful.")
    print("New balance:",
          accounts[account_number]["balance"])


def withdraw():
    print("\n--- Withdraw Money ---")

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Enter a valid amount.")
        return

    balance = accounts[account_number]["balance"]

    if amount > balance:
        print("Insufficient balance.")
        return

    accounts[account_number]["balance"] -= amount

    print("Withdrawal successful.")
    print("Remaining balance:",
          accounts[account_number]["balance"])


def display_accounts():
    print("\n--- All Accounts ---")

    if not accounts:
        print("No accounts available.")
        return

    for account_number, account in accounts.items():

        print("\nAccount Number:", account_number)
        print("Name:", account["name"])
        print("Balance:", account["balance"])


def main():

    while True:

        print("\n==============================")
        print("      BANK MANAGEMENT")
        print("==============================")

        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Display Accounts")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            check_balance()

        elif choice == "3":
            deposit()

        elif choice == "4":
            withdraw()

        elif choice == "5":
            display_accounts()

        elif choice == "6":
            print("Thank you for using the bank system.")
            break

        else:
            print("Invalid choice.")


main()