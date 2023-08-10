class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name, password):
        self.customers[name] = BankAccount(name, password)

    def get_customer(self, name):
        return self.customers.get(name)
    
    def create_account(self, name, password):
        if name in self.customers:
            print("Account already exists for this user.")
        else:
            self.add_customer(name, password)
            print("Account created successfully.")

class BankAccount:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit of {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal of {amount}")
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance

    def transfer(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            self.transactions.append(f"Transfer of {amount} to {other_account.name}")
            other_account.transactions.append(f"Transfer of {amount} from {self.name}")
            print("Transfer successful.")
        else:
            print("Insufficient balance.")

    def view_transactions(self):
        print("Transaction history:")
        for transaction in self.transactions:
            print(transaction)

    def apply_for_loan(self, amount):
        loan_status = "Approved" if amount <= (self.balance * 3) else "Rejected"
        print(f"Loan application for {amount} is {loan_status}")
        if loan_status == "Approved":
            self.balance += amount
            self.transactions.append(f"Loan of {amount} approved")

    def calculate_interest(self, interest_rate):
        interest = interest_rate * self.balance / 100
        self.balance += interest
        self.transactions.append(f"Interest of {interest} added")

    def login(self, password):
        if self.password == password:
            print("Login successful.")
            while True:
                print("1. View balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer")
                print("5. View transactions")
                print("6. Apply for loan")
                print("7. Calculate interest")
                print("8. Logout")
                option = int(input("Enter option: "))
                if option == 1:
                    print(f"Your balance is: {self.get_balance()}")
                elif option == 2:
                    amount = float(input("Enter amount to deposit: "))
                    self.deposit(amount)
                elif option == 3:
                    amount = float(input("Enter amount to withdraw: "))
                    self.withdraw(amount)
                elif option == 4:
                    name = input("Enter recipient name: ")
                    amount = float(input("Enter amount to transfer: "))
                    recipient = bank.get_customer(name)
                    if recipient:
                        self.transfer(recipient, amount)
                    else:
                        print("Recipient not found.")
                elif option == 5:
                    self.view_transactions()
                elif option == 6:
                    amount = float(input("Enter loan amount: "))
                    self.apply_for_loan(amount)
                elif option == 7:
                    interest_rate = float(input("Enter interest rate: "))
                    self.calculate_interest(interest_rate)
                elif option == 8:
                    print("Logout successful.")
                    break
                else:
                    print("Invalid option.")
        else:
            print("Incorrect password.")

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
        password = input("Enter password: ")
        account = bank.get_customer(name)
        if account:
            account.login(password)
        else:
            print("Account not found.")
    elif option == 3:
        print("Exiting.")
        break
    else:
        print("Invalid option.")

