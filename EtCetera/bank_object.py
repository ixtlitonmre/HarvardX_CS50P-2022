#Using classes is better way to encapsulate the functionality and is referred than use global variables
class Account:
    def __init__(self):
        #self.account_number = account_number
        #self.account_holder = account_holder
        self._balance = 0 #Is a best practice to use "_" to idicate is a private property, should not be used externally.

    @property
    def balance(self):
        return self._balance
    """
    @property
    def account_number(self):
        return self.account_number
    @property
    def account_holder(self):
        return self.account_holder
    """
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self._balance -= amount
            return True
        return False
"""
    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Account({self.account_number}, {self.account_holder}, Balance: {self.balance})"
"""
def main():
    account = Account ()
    print("Balance: ", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance: ", account.balance)

if __name__ == "__main__":
    main()