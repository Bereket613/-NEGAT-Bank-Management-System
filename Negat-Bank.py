class Account:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def display(self):
        print(f"Account Number: {self.account_number}, Holder Name: {self.account_holder_name}, Balance: {self.balance}")

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.account_list = []

    def create_account(self, account):
        self.account_list.append(account)
        print(f"Account created for {account.account_holder_name} with account number {account.account_number}")

    def display_accounts(self):
        print("Displaying all accounts:")
        for account in self.account_list:
            account.display()

    def search_account(self, search_number):
        for account in self.account_list:
            if account.account_number == search_number:
                print(f"Account found: Account Number: {account.account_number}, Holder Name: {account.account_holder_name}, Balance: {account.balance}")
                return
        print("The account is not found.")

    def remove_account(self, remove_number):
        for account in self.account_list:
            if account.account_number == remove_number:
                self.account_list.remove(account)
                print(f"The account with account number '{account.account_number}' has been successfully removed.")
                return
        print("The account is not found in the bank.")

    def deposit(self, account_number, amount):
        for account in self.account_list:
            if account.account_number == account_number:
                account.balance += amount
                print(f"Deposited {amount} into account {account_number}. New balance: {account.balance}")
                return
        print("The account is not found.")

    def withdraw(self, account_number, amount):
        for account in self.account_list:
            if account.account_number == account_number:
                if account.balance >= amount:
                    account.balance -= amount
                    print(f"Withdrew {amount} from account {account_number}. New balance: {account.balance}")
                else:
                    print("Insufficient balance.")
                return
        print("The account is not found.")

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = None
        to_account = None
        for account in self.account_list:
            if account.account_number == from_account_number:
                from_account = account
            elif account.account_number == to_account_number:
                to_account = account
        if from_account and to_account:
            if from_account.balance >= amount:
                from_account.balance -= amount
                to_account.balance += amount
                print(f"Transferred {amount} from account {from_account_number} to account {to_account_number}.")
            else:
                print("Insufficient balance.")
        else:
            print("One or both accounts not found.")

def display_welcome_message(bank_name):
    border = '*' * (len(bank_name) + 8)
    print(border)
    print(f"*  {bank_name}  *")
    print(border)

# Main program
bank = Bank("Negat Bank")
while True:
    display_welcome_message(bank.bank_name)
    print("1. Create a new account")
    print("2. Display all accounts")
    print("3. Search for an account")
    print("4. Deposit into an account")
    print("5. Withdraw from an account")
    print("6. Transfer between accounts")
    print("7. Close an account")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        account_number = input("Enter the account number: ")
        holder_name = input("Enter the account holder's name: ")
        balance = float(input("Enter the initial balance: "))
        new_account = Account(account_number, holder_name, balance)
        bank.create_account(new_account)

    elif choice == '2':
        bank.display_accounts()

    elif choice == '3':
        search_number = input("Enter the account number to search: ")
        bank.search_account(search_number)

    elif choice == '4':
        account_number = input("Enter the account number to deposit into: ")
        amount = float(input("Enter the amount to deposit: "))
        bank.deposit(account_number, amount)

    elif choice == '5':
        account_number = input("Enter the account number to withdraw from: ")
        amount = float(input("Enter the amount to withdraw: "))
        bank.withdraw(account_number, amount)

    elif choice == '6':
        from_account_number = input("Enter the account number to transfer from: ")
        to_account_number = input("Enter the account number to transfer to: ")
        amount = float(input("Enter the amount to transfer: "))
        bank.transfer(from_account_number, to_account_number, amount)

    elif choice == '7':
        remove_number = input("Enter the account number to close: ")
        bank.remove_account(remove_number)

    elif choice == '8':
        print(f"Thank you for using {bank.bank_name}. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
