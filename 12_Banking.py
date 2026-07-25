# THIS IS A SIMPLE BEGINER FRIENDLY PYTHON BANK
def show_balance(balance):
    print(f"\nCurrent Balance: ₹{balance:.2f}\n")


def deposit(balance):
    amount = float(input("Enter amount to be deposited: ₹"))

    if amount <= 0:
        print("Amount must be greater than 0.")
        return 0

    print(f"₹{amount:.2f} deposited successfully.")
    return amount


def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: ₹"))

    if amount > balance:
        print("Insufficient funds.")
        return 0

    if amount <= 0:
        print("Amount must be greater than 0.")
        return 0

    print(f"₹{amount:.2f} withdrawn successfully.")
    return amount


def main():
    balance = 0
    is_running = True

    print("=" * 45)
    print("        Welcome to Python Bank")
    print("=" * 45)

    while is_running:

        print("""
------------------ MENU ------------------
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
------------------------------------------
""")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance += deposit(balance)

        elif choice == '3':
            balance -= withdraw(balance)

        elif choice == '4':
            print("\nThank you for using Python Bank!")
            print("Have a great day!")
            is_running = False

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()