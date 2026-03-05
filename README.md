# Banking System

This project is a command-line banking system built in Python that demonstrates core object-oriented programming concepts such as abstraction, inheritance, encapsulation, and polymorphism.

The system simulates a small banking environment where users can create different types of accounts, perform transactions, transfer funds, and store account data persistently using JSON. The project focuses on building a clean object-oriented design while implementing realistic banking rules and transaction tracking.

---

## Project Highlights

• Object-Oriented design using abstract base classes  
• Multiple account types with different business rules  
• Secure account access using password authentication  
• Persistent data storage using JSON  
• Transaction logging with timestamps  
• Command-line interface for user interaction  

---

## Features

This banking system allows users to:

Create different types of accounts  
- Savings Account  
- Checking Account  
- Business Account  
- Crypto Wallet  

Perform banking operations  
- Deposit money  
- Withdraw money  
- Transfer funds between accounts  
- View account details  
- View transaction history  

Security and data handling  
- Password-protected accounts  
- Persistent storage using a JSON file  
- Transaction history with timestamps  

Account rules implemented in the system  
- Checking accounts include a withdrawal fee  
- Business accounts require a minimum balance  
- Crypto wallets allow coin deposits and withdrawals  

---

## Technologies Used

Python  
Object-Oriented Programming (OOP)  
JSON for data persistence  
Datetime for transaction tracking

---

## Object-Oriented Concepts Demonstrated

### Abstraction
An abstract `Account` class defines the core functionality that all account types must implement, including deposit, withdraw, and account type identification.

### Inheritance
Specialized account types extend the base `Account` class:

- SavingsAccount
- CheckingAccount
- BusinessAccount

Each subclass implements its own deposit and withdrawal behavior.

### Encapsulation
Account balances are protected using private attributes with controlled access through property getters and setters.

### Polymorphism
Each account type overrides deposit and withdrawal logic based on its rules.

### Operator Overloading
Accounts support comparison and balance operations through custom operator methods.

---

## System Architecture

The system is organized into several main components:

### Account (Abstract Base Class)
Defines shared attributes and methods for all account types including balance handling and transaction tracking.

### SavingsAccount
Standard account with simple deposit and withdrawal operations.

### CheckingAccount
Withdrawals include a small transaction fee.

### BusinessAccount
Maintains a required minimum balance of $500.

### CryptoWallet
Represents a digital wallet for managing cryptocurrency balances.

### Transaction
Tracks every account activity including deposits, withdrawals, transfers, status, and timestamps.

### Bank
Central controller responsible for:

• Creating accounts  
• Managing transactions  
• Handling fund transfers  
• Loading and saving account data  

### Command Line Menu
Provides an interactive interface for users to perform banking operations.

---

## How to Run the Program

1. Make sure Python 3 is installed.

2. Clone the repository

```
git clone https://github.com/yourusername/Banking_System.git
```

3. Navigate to the project directory

```
cd Banking_System
```

4. Run the program

```
python bank_system.py
```

---

## Main Menu Options

When the system starts, users can choose from the following actions:

1. Create a new account  
2. Deposit funds  
3. Withdraw funds  
4. Transfer funds between accounts  
5. View account details  
6. Display all accounts  
7. Exit the program  

---

## Data Storage

All account data and transaction history are stored in a JSON file:

```
bank_data.json
```

This allows the system to load previous accounts and transactions whenever the application starts.

---

## Example Transaction Log

Each transaction records the following information:

• Transaction type  
• Amount  
• Status  
• Timestamp  

Example output:

```
Transaction: Deposit | Amount: 200 | Status: Success | Time: 2026-03-04 14:25:33
```

---

## Future Improvements

Possible enhancements for future versions of the system include:

• Graphical user interface (GUI)  
• Database integration (SQLite or PostgreSQL)  
• Account authentication encryption  
• REST API support for banking operations  
• Web-based dashboard for account management  

---

## Author

Ahmad Zayour  
Software Developer
