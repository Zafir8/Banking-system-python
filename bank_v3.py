class Bank:
    def __init__(self):
        self.customers = []

    def create_account(self, name, password):
        customer = Customer(name, password)
        self.customers.append(customer)
        print("Account created successfully.")

    def get_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None

class Customer:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        print("Deposit successful.")
        print(f"Your current balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            print("Withdrawal successful.")
            print(f"Your current balance is {self.balance}.")
        else:
            print("Insufficient balance.")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Transferred {amount} to {recipient.name}")
            recipient.transactions.append(f"Received {amount} from {self.name}")
            print("Transfer successful.")
            print(f"Your current balance is {self.balance}.")
        else:
            print("Insufficient balance.")

    def view_transactions(self):
        print("Transactions:")
        for transaction in self.transactions:
            print(transaction)

    def apply_for_loan(self, amount):
        self.balance += amount
        self.transactions.append(f"Applied for loan of {amount}")
        print("Loan application successful.")
        print(f"Your current balance is {self.balance}.")

    def calculate_interest(self, interest_rate):
        interest = self.balance * interest_rate / 100
        self.balance += interest
        self.transactions.append(f"Calculated interest of {interest}")
        print("Interest calculation successful.")
        print(f"Your current balance is {self.balance}.")

    def login(self, password):
        if self.password == password:
            print("Login successful.")
            while True:
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Transfer")
                print("4. View transactions")
                print("5. Apply for loan")
                print("6. Calculate interest")
                print("7. Logout")
                option = int(input("Enter option: "))
                if option == 1:
                    amount = float(input("Enter amount to deposit: "))
                    self.deposit(amount)
                elif option == 2:
                    amount = float(input("Enter amount to withdraw: "))
                    self.withdraw(amount)
                elif option == 3:
                    recipient_name = input("Enter recipient name: ")
                    recipient = bank.get_customer(recipient_name)
                    if recipient:
                        amount = float(input("Enter amount to transfer: "))
                        self.transfer(recipient, amount)
                    else:
                        print("Recipient not found.")
                elif option == 4:
                    self.view_transactions()
                elif option == 5:
                    amount = float(input("Enter loan amount: "))
                    self.apply_for_loan(amount)
                elif option == 6:
                    interest_rate = float(input("Enter interest rate: "))
                    self.calculate_interest(interest_rate)
                elif option == 7:
                    print("Logout successful.")
                    break
                else:
                    print("Invalid option.")
        else:
            print("Login failed.")

bank = Bank()
while True:
    print("1. Create account")
    print("2. Login")
    print("3. Exit")
    option = int(input("Enter option: "))
    if option == 1:
        name = input("Enter name: ")
        password = input("Enter password: ")
        bank.create_account(name, password)
    elif option == 2:
        name = input("Enter name: ")
        customer = bank.get_customer(name)
        if customer:
            password = input("Enter password: ")
            customer.login(password)
        else:
            print("Customer not found.")
    elif option == 3:
        print("Bye!")
        break
    else:
        print("Invalid option.")

