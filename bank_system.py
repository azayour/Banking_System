#import abstract method
from abc import ABC, abstractmethod

#import date time method
from datetime import datetime 

#import
import json

#abstract class
class Account(ABC):
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance
        self.transactions = []
        self.password = None

    #Encapsulation
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    def __add__(self, other):
        if isinstance(other, Account):
            return self.balance + other.balance
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Account):
            return self.balance > other.balance
        return NotImplemented

    @abstractmethod
    def deposit(self, amount):
        pass
    
    
    @abstractmethod
    def withdraw(self, amount):
        pass

    
    @abstractmethod
    def get_account_type(self):
        pass


#sub classes that inherit from abstract class Account:

#Savings Account
class SavingsAccount(Account):

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction("Deposit",amount,"Success"))
            print(f"Deposited ${amount}. New balance is: ${self.balance}")
            return True
        else:
            self.transactions.append(Transaction("Deposit", amount, "Failed"))
            print("Deposit amount must be positive")
            return False
    
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction("Withdraw",amount,"Success"))
            print(f"Withdraw ${amount}. Remaining balance is: ${self.balance}")
            return True
        else:
            self.transactions.append(Transaction("Withdraw", amount, "Failed"))
            print("Invalid amount.")
            return False
        

    
    def get_account_type(self):
        return "Savings Account"
        


#Checking Account
class CheckingAccount(Account):

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction("Deposit", amount, "Success"))
            print(f"Deposited ${amount} into Checking. New balance is: ${self.balance}")
            return True
        else:
            self.transactions.append(Transaction("Deposit", amount, "Failed"))
            print("Invalid amount")
            return False
    
    
    def withdraw(self, amount):
        #withdraw rule for Checking Account.
        fee = 2
        total = amount + fee
        #withdrawing from a checking account will lead to $2 fee
        if amount > 0 and total <= self.balance:
            self.balance -= total
            self.transactions.append(Transaction("Withdrawal", amount, "Success"))
            print(f"Withdraw ${amount} + ${fee} fee. Remaining balance: ${self.balance}.")
            return True
        else:
            self.transactions.append(Transaction("Withdrawal", amount, "Failed"))
            print("Invalid amount")
            return False

    
    def get_account_type(self):
        return "Checking Account"
        

#Business Account
class BusinessAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction("Deposit", amount, "Success"))
            print(f"Deposited ${amount} into Business account. New balance is: ${self.balance}")
            return True
        else:
            self.transactions.append(Transaction("Deposit", amount, "Failed"))
            print("Invalid amount")
            return False
        
    
    
    def withdraw(self, amount):
        #Business Account must have a $500 as a minimum balance
        min_balance = 500
        if amount > 0 and self.balance - amount >=min_balance:
            self.balance -= amount
            self.transactions.append(Transaction("Withdrawal", amount, "Success"))
            print(f"Withdraw ${amount}. Remaining balance: ${self.balance}.")
            return True
        else:
            self.transactions.append(Transaction("Withdrawal", amount, "Failed"))
            print("Invalid amount. Minimum balance should be $500")
            return False
        
    
    def get_account_type(self):
        return "Business Account"
    
#crypto Wallet(doent inherit from Account)
class CryptoWallet:
    def __init__(self, wallet_id, holder_name, balance=0):
        self.account_number = wallet_id          
        self.holder_name = holder_name
        self.__balance = balance                 
        self.transactions = []
        self.password = None
    
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount

    def deposit(self, amount):

        if amount > 0:
            self.balance = self.balance + amount
            self.transactions.append(Transaction("Deposit", amount, "Success"))
            print(f"Deposited {amount} coin(s). New balance is: {self.balance}")
            return True
        else:
            self.transactions.append(Transaction("Deposit", amount, "Failed"))
            print("Invalid amount")
            return False
    
    def withdraw(self, amount):

        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
            self.transactions.append(Transaction("Withdrawal", amount, "Success"))
            print(f"Withdrew {amount} coin(s). Remaining balance is: {self.balance}")
            return True
        else:
            self.transactions.append(Transaction("Withdrawal", amount, "Failed"))
            print("Invalid amount")
            return False
    
    def get_account_type(self):
        return "Crypto Wallet"
        




class Transaction:
    def __init__(self, type, amount, status):
        self.type = type
        self.amount = amount
        self.timestamp = datetime.now()
        self.status = status

    def __str__(self):
        return(f"Transaction:{self.type} | " 
               f"Amount:{self.amount} | "
               f"Status:{self.status} | "
               f"Time:{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    
    
#central controller for all accounts and transactions
class Bank:
    def __init__(self):
        self.accounts = {} 
        self.file = "bank_data.json"
        self.load_data() #load saved data when program starts
    
    def save_data(self):
        data = {} #create dictionary

        for acc_num, acc in self.accounts.items():
            key = str(acc_num)
            data[key]={
                "account_type": acc.get_account_type(),
                "holder_name": acc.holder_name,
                "balance": acc.balance,
                "password": acc.password,
                "transactions": [
                    {
                        "type": t.type,
                        "amount": t.amount,
                        "status": t.status,
                        "timestamp": t.timestamp.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    for t in acc.transactions
                ],
            }
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4) 

    def load_data(self):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
            for acc_num, info in data.items():
                acct_type = info["account_type"].lower()
                holder = info["holder_name"]
                balance = info["balance"]

                if "savings" in acct_type:
                    acc = SavingsAccount(acc_num, holder, balance)
                elif "checking" in acct_type:
                    acc = CheckingAccount(acc_num, holder, balance)
                elif "business" in acct_type:
                    acc = BusinessAccount(acc_num, holder, balance)
                elif "crypto" in acct_type:
                    acc = CryptoWallet(acc_num, holder, balance)
                else:
                    continue

                acc.password = info["password"]
                for t in info.get("transactions", []):
                    acc.transactions.append(Transaction(t["type"], t["amount"], t["status"]))
                self.accounts[int(acc_num)] = acc
        except FileNotFoundError:
            # If no file exists yet, just start empty
            pass
            
            
    
    def create_account(self, account_type, account_number, holder_name, balance = 0):

        #prevent duplicates account number
        if account_number in self.accounts:
            print(f"Account number {account_number} already exists. Please use a different number.")
            return
    
        if account_type.lower() == "business" and balance < 500:
            print("Business accounts require a minimum $500 opening balance.")
            return
        
        if account_type.lower() == "savings":
            account = SavingsAccount(account_number, holder_name, balance)
        elif account_type.lower() == "checking":
            account = CheckingAccount(account_number, holder_name, balance)
        elif account_type.lower() == "business":
            account = BusinessAccount(account_number, holder_name, balance)
        elif account_type.lower() == "crypto": 
            account = CryptoWallet(account_number, holder_name, balance)
        else:
            print("Invalid account type")
            return
        
        password = input("Create a password for this account:")
        confirm = input("Confirm password: ")

        if password != confirm:
            print("Passwords do no match. Account not created")
            return
        
        account.password = password
        self.accounts[account_number] = account

        if balance > 0:
            account.transactions.append(Transaction("OpeningDeposit", balance, "Success"))
        print(f"{account_type.capitalize()} Account created for {holder_name} with balance ${balance}.")
        self.save_data()

    def get_account_secure(self, account_number):
        if account_number not in self.accounts:
            print("Account not found")
            return None
        
        account = self.accounts[account_number]
        password = input("Enter your password: ")
        if password == account.password:
            return account

        else: 
            print("Incorrect password.")
            return None

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found")
            return None
        
    def transfer_funds(self, from_acc_num, to_acc_num, amount):
        
        #Prevent transferring to the same account
        if from_acc_num == to_acc_num:
            print("Cannot transfer to the same acount")
            return
        
        if amount <= 0:
            print("Transfer amount must be greater than 0.")
            return
    
        from_acc = self.get_account(from_acc_num)
        to_acc = self.get_account(to_acc_num)
        
        if not from_acc or not to_acc:
            print("Transfer failed: one or both accounts not found.")
            return

        if from_acc.withdraw(amount):
            if to_acc.deposit(amount):
                from_acc.transactions.append(Transaction("Transfer Out", amount, "Success"))
                to_acc.transactions.append(Transaction("Transfer In", amount, "Success"))
                print(f"Transferred ${amount} from Account {from_acc_num} to Account {to_acc_num}.")
        
            else:
                from_acc.deposit(amount)
                from_acc.transactions.append(Transaction("Transfer Out", amount, "Failed"))
                print("Transfer failed due to insufficient balance or invalid amount.")
        
        else:
            from_acc.transactions.append(Transaction("Transfer Out", amount, "Failed"))
            print("Transfer failed due to insufficient balance or invalid amount.")

        self.save_data()

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts in the system.")
            return
        for acc in self.accounts.values():
            print(f"{acc.get_account_type()} | "
                  f"Account Number: {acc.account_number} | "
                  f"Holder: {acc.holder_name} | "
                  f"Balance: ${acc.balance}")

    def show_account_transactions(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(f"--- Transaction History for {account.holder_name} ---")
            if not account.transactions:
                print("No transactions yet.")
            else:
                for t in account.transactions:
                    print(t)


def show_account_details(account : Account): 
    print(f"{account.get_account_type()} | "
          f"Account Number: {account.account_number} | "
          f"Holder: {account.holder_name} | "
          f"Balance: ${account.balance}")
    
#Main Menu

def MENU():
    bank = Bank()
    print("Welcome to the Banking System")

    while True:
        print("Main Menu:")
        print("1. Create new account (savings/checking/business/crypto)")
        print("2. Deposit funds")
        print("3. Withdraw funds")
        print("4. Transfer funds between accounts")
        print("5. View account details")
        print("6. Display all accounts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            while True:
                acct_type = input("Enter account type (savings/checking/business/crypto): ").strip().lower()

                #Check for valid choice:
                if acct_type in ["savings", "checking", "business", "crypto"]:
                    break
                else:
                    print("Invalid account type. Please enter one of: savings, checking, business, or crypto.")
                
            try:
                #Loop until the user enters a valid input
                while True:
                    acct_num_input = input("Enter account number (numeric): ").strip()

                    if not acct_num_input.isdigit():
                        print("Account number must be numeric.")
                        continue
                    acct_num = int(acct_num_input)
                    
                    #check if account number already exists
                    if acct_num in bank.accounts:
                        print(f"Account number {acct_num} already exists. Please use a different number.")
                        continue
                    break
                holder = input("Enter holder name: ").strip()
                while True:
                    try:
                        opening = float(input("Enter opening balance (>= 0): ").strip())
                        if opening < 0:
                            print("Opening balance cannot be negative.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number")
                        
                bank.create_account(acct_type, acct_num, holder, opening)

                #ask if user wants to continue
                again = input("Do you want to continue? (y/n): ").strip().lower()
                if again != "y":
                    print("Goodbye!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers for account number and balance.")

        elif choice == "2":
            try:
                acct_num = int(input("Account number: ").strip())
                amount = float(input("Deposit amount (> 0): ").strip())
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                acc = bank.get_account_secure(acct_num)
                if acc and acc.deposit(amount):
                    bank.save_data()
                
                again = input("Do you want to continue? (y/n): ").strip().lower()
                if again != "y":
                    print("Goodbye!")
                    break

            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == "3":
            try:
                acct_num = int(input("Account number: ").strip())
                while True:
                    #Loop until a valid input is entered
                    try:
                        amount = float(input("Withdrawal amount (> 0): ").strip())
                        if amount <= 0:
                            print("Amount must be greater than 0.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input")

                    
                acc = bank.get_account(acct_num)
                if acc and acc.withdraw(amount):
                    bank.save_data()

                again = input("Do you want to continue? (y/n): ").strip().lower()
                if again != "y":
                    print("Goodbye!")
                    break

            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == "4":
            try:
                from_num = int(input("From account number: ").strip())
                to_num = int(input("To account number: ").strip())
                while True:
                    try:
                        amount = float(input("Transfer amount (> 0): ").strip())
                        if amount <= 0:
                            print("Amount must be greater than 0.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input.")
                
                bank.transfer_funds(from_num, to_num, amount)

                #ask if user wants to continue
                again = input("Do you want to continue? (y/n): ").strip().lower()
                if again != "y":
                    print("Goodbye!")
                    break

            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == "5":
            try:
                acct_num = int(input("Account number: ").strip())
                acc = bank.get_account(acct_num)
                if acc:
                    print(f"{acc.get_account_type()} | Account Number: {acc.account_number} | Holder: {acc.holder_name} | Balance: ${acc.balance}")
                    print("\nRecent Transactions:")
                    if not acc.transactions:
                        print("No transactions yet.")
                    else:
                        for t in acc.transactions[-10:]:
                            print(t)
                #ask if user wants to continue even if account not found
                again =  input("Do you want to continue? (y/n): ").strip().lower()
                if again != "y":
                    print("Goodbye!")
                    break 

            except ValueError:
                print("Invalid input.")

        elif choice == "6":
            bank.display_all_accounts()
            again = input("Do you want to continue? (y/n): ").strip().lower()
            if again != "y":
                print("Goodbye!")
                break

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-7.")

MENU()