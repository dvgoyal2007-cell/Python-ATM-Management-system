accounts = {
    1001: {"name": "Dhruv", "pin": 3252, "balance": 5000},
    1002: {"name": "Harsh", "pin": 3252, "balance": 7500},
    1003: {"name": "Prakshal", "pin": 3252, "balance": 3000},
    1004: {"name": "Sakshi", "pin": 3252, "balance": 5000},
    1005: {"name": "Bhramari", "pin": 3252, "balance": 7500},
    1006: {"name": "Shreya", "pin": 3252, "balance": 3000},
    1007: {"name": "Shubham", "pin": 3252, "balance": 2000}
}

transactions = []

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

        # ---------------- CHECK BALANCE ----------------

        if choice == 1:

            print("\nYour balance is: ₹", account["balance"])

        # ---------------- DEPOSIT ----------------

        elif choice == 2:

            amount = float(input("Enter amount to deposit: ₹"))

            if amount > 0:

                account["balance"] = account["balance"] + amount

                print("\nAmount deposited successfully")
                print("Your new balance is: ₹", account["balance"])

                transactions.append(
                    f"+ Deposited: ₹{amount:.2f}"
                )

            else:

                print("Invalid amount")

        # ---------------- WITHDRAW ----------------

        elif choice == 3:

            amount = float(input("Enter amount to withdraw: ₹"))

            if amount > 0 and amount <= account["balance"]:

                account["balance"] = account["balance"] - amount

                print("\nPlease collect your cash")
                print("Your remaining balance is: ₹", account["balance"])

                transactions.append(
                    f"- Withdrawn: ₹{amount:.2f}"
                )

            elif amount <= 0:

                print("Invalid amount")

            else:

                print("Insufficient balance")

        # ---------------- CHANGE PIN ----------------

        elif choice == 4:

            old_pin = int(input("Enter your current PIN: "))

            if old_pin == account["pin"]:

                new_pin = int(input("Enter new PIN: "))
                confirm_pin = int(input("Enter new PIN again: "))

                if new_pin == confirm_pin:

                    account["pin"] = new_pin

                    print("\nPIN changed successfully")

                else:

                    print("\nNew PINs do not match")

            else:

                print("\nIncorrect current PIN")

        # ---------------- MINI STATEMENT ----------------

        elif choice == 5:

            print("\n================================")
            print("         MINI STATEMENT")
            print("================================")
            print("Account Holder:", account["name"])
            print("--------------------------------")

            if len(transactions) == 0:

                print("No transactions yet.")

            else:

                for i, transaction in enumerate(
                    transactions,
                    start=1
                ):

                    print(i, ".", transaction)

            print("--------------------------------")
            print(
                "Final Balance: ₹",
                f"{account['balance']:.2f}"
            )
            print("================================")

        # ---------------- LOGOUT ----------------

        elif choice == 6:

            print("\nYou have been logged out successfully.")
            break

        # ---------------- EXIT ----------------

        elif choice == 7:

            print("\nThank you for choosing this ATM.")
            running = False

        # ---------------- INVALID CHOICE ----------------

        else:

            print("\nInvalid choice")
