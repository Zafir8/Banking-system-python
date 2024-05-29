import os

def load_customers():
    customers = {}
    if os.path.exists("customers.txt"):
        with open("customers.txt", "r") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) == 3:
                    name, password, account_number = parts
                    customers[name] = {"name": name, "password": password, "account_number": account_number, "balance": 0, "transactions": []}
                    load_customer_details(customers[name])
    return customers

def load_customer_details(customer):
    if os.path.exists(f"{customer['account_number']}.txt"):
        with open(f"{customer['account_number']}.txt", "r") as f:
            lines = f.readlines()
            if lines:
                customer["balance"] = float(lines[0].strip())
                customer["transactions"] = [line.strip() for line in lines[1:]]

def save_customer_details(customer):
    with open(f"{customer['account_number']}.txt", "w") as f:
        f.write(f"{customer['balance']}\n")
        for transaction in customer["transactions"]:
            f.write(f"{transaction}\n")

def create_account(customers, name, password):
    account_number = str(len(customers) + 1).zfill(6)  # 6-digit account number
    customer = {"name": name, "password": password, "account_number": account_number, "balance": 0, "transactions": []}
    customers[name] = customer
    with open("customers.txt", "a") as f:
        f.write(f"{name}:{password}:{account_number}\n")
    save_customer_details(customer)
    print("Account created.")

def get_customer_by_name(customers, name):
    return customers.get(name)

def login(customer):
    while True:
        print("1. View balance")
        print("2. Deposit")
        print("3. Transfer")
        print("4. View transactions")
        print("5. Apply for loan")
        print("6. Calculate interest")
        print("7. Logout")
        option = int(input("Enter option: "))
        match option:
            case 1:
                view_balance(customer)
            case 2:
                amount = float(input("Enter amount: "))
                deposit(customer, amount)
            case 3:
                recipient_account = input("Enter recipient account number: ")
                recipient = get_customer_by_account_number(customers, recipient_account)
                if recipient:
                    amount = float(input("Enter amount to transfer: "))
                    transfer(customer, recipient, amount)
                else:
                    print("Recipient not found.")
            case 4:
                view_transactions(customer)
            case 5:
                amount = float(input("Enter loan amount: "))
                apply_for_loan(customer, amount)
            case 6:
                interest_rate = float(input("Enter interest rate: "))
                calculate_interest(customer, interest_rate)
            case 7:
                print("Logout successful.")
                save_customer_details(customer)
                break
            case _:
                print("Invalid option.")

def view_balance(customer):
    print(f"Balance: {customer['balance']}")

def deposit(customer, amount):
    customer['balance'] += amount
    customer['transactions'].append(f"Deposited {amount}")
    save_customer_details(customer)

def withdraw(customer, amount):
    if customer['balance'] >= amount:
        customer['balance'] -= amount
        customer['transactions'].append(f"Withdrew {amount}")
        save_customer_details(customer)
    else:
        print("Insufficient balance.")

def transfer(sender, recipient, amount):
    if sender['balance'] >= amount:
        withdraw(sender, amount)
        deposit(recipient, amount)
        sender['transactions'].append(f"Transferred {amount} to {recipient['account_number']}")
        save_customer_details(sender)
    else:
        print("Insufficient balance.")

def view_transactions(customer):
    print("Transactions:")
    for transaction in customer['transactions']:
        print(transaction)

def apply_for_loan(customer, amount):
    customer['balance'] += amount
    customer['transactions'].append(f"Took loan of {amount}")
    save_customer_details(customer)

def calculate_interest(customer, interest_rate):
    interest = customer['balance'] * (interest_rate / 100)
    customer['balance'] += interest
    customer['transactions'].append(f"Calculated interest of {interest}")
    save_customer_details(customer)

def get_customer_by_account_number(customers, account_number):
    for customer in customers.values():
        if customer["account_number"] == account_number:
            return customer
    return None

# Main code
customers = load_customers()

while True:
    print("1. Login")
    print("2. Sign up")
    print("3. Exit")
    option = int(input("Enter option: "))
    match option:
        case 1:
            name = input("Enter name: ")
            password = input("Enter password: ")
            customer = get_customer_by_name(customers, name)
            if customer and customer["password"] == password:
                login(customer)
            else:
                print("Customer not found or incorrect password.")
        case 2:
            name = input("Enter name: ")
            password = input("Enter password: ")
            if name in customers:
                print("Username already taken.")
            else:
                create_account(customers, name, password)
        case 3:
            print("Exiting...")
            break
        case _:
            print("Invalid option.")
