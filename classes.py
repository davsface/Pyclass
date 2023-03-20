class BankAccount:
    """
    Represents a bank account that the user can deposit money to and    withdraw money from.
    """

    def __init__(self, account_ID, balance):
        """Creates a bank account object with an account ID and balance."""
        self._account_ID = account_ID
        self._balance = balance

    def get_account_ID(self):
        """Returns the account ID."""
        return self._account_ID

    def set_account_ID(self, new_ID):
        """Sets the account ID to a new value."""
        self._account_ID = new_ID

    def get_balance(self):
        """Returns the current balance."""
        return self._balance

    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        self._balance += amount

    def withdraw(self, amount):
        """Withdraws the specified amount from the account."""
        self._balance -= amount

bank1 = BankAccount(1, 1000)

print(bank1.get_balance())
bank1.deposit(1000)
print(bank1.get_balance())

