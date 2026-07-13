from account import Account


class CurrentAccount(Account):
    """
    Current Bank Account
    No minimum balance restriction.
    """

    def __init__(self, account_number, customer, balance=0):
        super().__init__(account_number, customer, balance)

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.get_balance():
            raise ValueError("Insufficient balance.")

        self._set_balance(self.get_balance() - amount)

    def account_type(self):
        return "Current"