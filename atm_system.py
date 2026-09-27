from accounts import accounts
from transactions import transactions
from atm_functions import (
    check_balance,
    deposit_money,
    withdraw_money,
    change_pin
)
from transactions import show_transactions


# Account Number
account_number = int(input("Enter your account number: "))

if account_number in accounts:
    account = accounts[account_number]
else:
    print("Invalid account number")
    exit()


# PIN Verification
attempts = 0

while attempts < 3:

    user_pin = int(input("Enter your PIN: "))

    if user_pin == account["pin"]:

        print("\nWelcome", account["name"], "!")
        print("PIN is correct")
        break

    else:

        attempts = attempts + 1
        print("PIN is incorrect")


# Account blocked
if attempts == 3:

    print("Too many attempts. Your account is blocked")

else:

    # ATM starts
    running = True

    while running:

        print("\n======================================")
        print("              ATM SYSTEM")
        print("======================================")
        print("Account Holder:", account["name"])
        print("======================================")

        print("              MAIN MENU")
        print("--------------------------------------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Mini Statement")
        print("6. Logout")
        print("7. EXIT")
        print("--------------------------------------")

        choice = int(input("Enter your choice: "))

        # CHECK BALANCE
        if choice == 1:

            check_balance(account)

        # DEPOSIT
        elif choice == 2:

            deposit_money(account, transactions)

        # WITHDRAW
        elif choice == 3:

            withdraw_money(account, transactions)

        # CHANGE PIN
        elif choice == 4:

            change_pin(account)

        # MINI STATEMENT
        elif choice == 5:

            show_transactions(account)

        # LOGOUT
        elif choice == 6:

            print("\nYou have been logged out successfully.")
            break

        # EXIT
        elif choice == 7:

            print("\nThank you for choosing this ATM.")
            running = False

        # INVALID CHOICE
        else:

            print("\nInvalid choice")
