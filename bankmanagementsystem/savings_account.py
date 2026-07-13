from account import Account


class SavingsAccount(Account):
    """
    Savings Bank Account
    Minimum balance = ₹500
    """

    MINIMUM_BALANCE = 500

    def __init__(self, account_number, customer, balance=0):
        super().__init__(account_number, customer, balance)

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if self.get_balance() - amount < SavingsAccount.MINIMUM_BALANCE:
            raise ValueError(
                f"Minimum balance of ₹{SavingsAccount.MINIMUM_BALANCE} must be maintained."
            )

        self._set_balance(self.get_balance() - amount)

    def account_type(self):
        return "Savings"