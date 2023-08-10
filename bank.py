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

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance

    def login(self, password):
        if self.password == password:
            return True
        else:
            return False

bank = Bank()

while True:
    print("Enter 1 to create an account")
    print("Enter 2 to log into an account")
    print("Enter 3 to exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter your name: ")
        password = input("Enter a password: ")
        bank.create_account(name, password)
    elif choice == 2:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        customer = bank.get_customer(name)
        if customer:
            if customer.login(password):
                while True:
                    print("Enter 1 to deposit")
                    print("Enter 2 to withdraw")
                    print("Enter 3 to check balance")
                    print("Enter 4 to logout")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        amount = float(input("Enter the amount to deposit: "))
                        customer.deposit(amount)
                    elif choice == 2:
                        amount = float(input("Enter the amount to withdraw: "))
                        customer.withdraw(amount)
                    elif choice == 3:
                        print("Your balance is:", customer.get_balance())
                    elif choice == 4:
                        print("Logout successful.")
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Incorrect password.")
        else:
            print("Customer not found.")
    elif choice == 3:
        print("Exiting.")
        break
    else:
        print("Invalid choice.")
