balance = 0

def main():
    global balance
    while True:
        print("Current balance:", balance)
        action = input("Enter 'deposit', 'withdraw', or 'exit': ").strip().lower()
        
        if action == 'deposit':
            amount = float(input("Enter amount to deposit: "))
            deposit(amount)
        
        elif action == 'withdraw':
            amount = float(input("Enter amount to withdraw: "))
            withdraw(amount)
        
        elif action == 'exit':
            print("Exiting the program.")
            break

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited {amount}. New balance: {balance}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew {amount}. New balance: {balance}")
    else:
        print("Insufficient funds.")

if __name__ == "__main__":
    main()