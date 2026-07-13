from customer import Customer
from savings_account import SavingsAccount
from current_account import CurrentAccount
from transaction import Transaction
from file_manager import FileManager


class Bank:
    """
    Represents the bank and manages all accounts and transactions.
    """

    def __init__(self):
        """
        Load previously saved accounts and transactions.
        """

        self.__accounts = FileManager.load_accounts()
        self.__transactions = FileManager.load_transactions()

    # ==========================================================
    # Create Savings Account
    # ==========================================================

    def create_savings_account(
            self,
            account_number,
            customer_id,
            name,
            phone,
            address,
            balance):

        # Check whether account already exists
        if self.search_account(account_number) is not None:
            print("\nAccount Number already exists.")
            return

        customer = Customer(
            customer_id,
            name,
            phone,
            address
        )

        account = SavingsAccount(
            account_number,
            customer,
            balance
        )

        self.__accounts.append(account)

        FileManager.save_all_accounts(self.__accounts)

        print("\nSavings Account Created Successfully!")

    # ==========================================================
    # Create Current Account
    # ==========================================================

    def create_current_account(
            self,
            account_number,
            customer_id,
            name,
            phone,
            address,
            balance):

        # Check whether account already exists
        if self.search_account(account_number) is not None:
            print("\nAccount Number already exists.")
            return

        customer = Customer(
            customer_id,
            name,
            phone,
            address
        )

        account = CurrentAccount(
            account_number,
            customer,
            balance
        )

        self.__accounts.append(account)

        FileManager.save_all_accounts(self.__accounts)

        print("\nCurrent Account Created Successfully!")

    # ==========================================================
    # Search Account
    # ==========================================================

    def search_account(self, account_number):
        """
        Returns the account object if found,
        otherwise returns None.
        """

        for account in self.__accounts:

            if account.get_account_number() == account_number:
                return account

        return None
            # ==========================================================
    # Deposit Money
    # ==========================================================

    def deposit_money(self, account_number, amount):
        """
        Deposit money into an account.
        """

        account = self.search_account(account_number)

        if account is None:
            print("\nAccount not found.")
            return

        try:

            account.deposit(amount)

            transaction = Transaction(
                account_number,
                "Deposit",
                amount
            )

            self.__transactions.append(transaction)

            FileManager.save_all_accounts(self.__accounts)
            FileManager.save_transaction(transaction)

            print("\nDeposit Successful!")
            print(f"Updated Balance : ₹{account.get_balance():.2f}")

        except ValueError as error:
            print(error)

    # ==========================================================
    # Withdraw Money
    # ==========================================================

    def withdraw_money(self, account_number, amount):
        """
        Withdraw money from an account.
        """

        account = self.search_account(account_number)

        if account is None:
            print("\nAccount not found.")
            return

        try:

            account.withdraw(amount)

            transaction = Transaction(
                account_number,
                "Withdraw",
                amount
            )

            self.__transactions.append(transaction)

            FileManager.save_all_accounts(self.__accounts)
            FileManager.save_transaction(transaction)

            print("\nWithdrawal Successful!")
            print(f"Updated Balance : ₹{account.get_balance():.2f}")

        except ValueError as error:
            print(error)

    # ==========================================================
    # Display All Accounts
    # ==========================================================

    def display_all_accounts(self):
        """
        Display all bank accounts.
        """

        if len(self.__accounts) == 0:
            print("\nNo accounts available.")
            return

        print("\n========== ACCOUNT LIST ==========")

        for account in self.__accounts:
            account.display()

    # ==========================================================
    # Delete Account
    # ==========================================================

    def delete_account(self, account_number):
        """
        Delete an account.
        """

        account = self.search_account(account_number)

        if account is None:
            print("\nAccount not found.")
            return

        self.__accounts.remove(account)

        FileManager.save_all_accounts(self.__accounts)

        print("\nAccount deleted successfully!")
            # ==========================================================
    # Show Transaction History
    # ==========================================================

    def show_transaction_history(self, account_number):
        """
        Display all transactions of a particular account.
        """

        found = False

        print("\n========== TRANSACTION HISTORY ==========")

        for transaction in self.__transactions:

            if transaction.get_account_number() == account_number:

                transaction.display()
                found = True

        if not found:
            print("No transactions found.")

    # ==========================================================
    # Display Single Account
    # ==========================================================

    def display_account(self, account_number):
        """
        Display a particular account.
        """

        account = self.search_account(account_number)

        if account is None:
            print("\nAccount not found.")
            return

        account.display()

    # ==========================================================
    # Total Number of Accounts
    # ==========================================================

    def total_accounts(self):
        """
        Returns the total number of bank accounts.
        """

        return len(self.__accounts)
            # ==========================================================
    # Check whether account exists
    # ==========================================================

    def account_exists(self, account_number):

        return self.search_account(account_number) is not None

    # ==========================================================
    # Get Account
    # ==========================================================

    def get_account(self, account_number):

        return self.search_account(account_number)