# Transaction handling

transactions = []


def add_transaction(transaction):
    transactions.append(transaction)


def show_transactions(account):
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
