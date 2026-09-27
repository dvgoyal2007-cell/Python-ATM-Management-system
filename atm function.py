# ATM Functions


def check_balance(account):
    print("\nYour balance is: ₹", account["balance"])


def deposit_money(account, transactions):
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


def withdraw_money(account, transactions):
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


def change_pin(account):
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
