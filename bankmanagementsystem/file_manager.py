import csv
import os

from customer import Customer
from savings_account import SavingsAccount
from current_account import CurrentAccount
from transaction import Transaction


class FileManager:
    """
    Handles saving and loading accounts and transactions.
    """

    ACCOUNTS_FILE = "data/accounts.csv"
    TRANSACTIONS_FILE = "data/transactions.csv"

    # ==========================================================
    # Save All Accounts
    # ==========================================================

    @staticmethod
    def save_all_accounts(accounts):

        with open(FileManager.ACCOUNTS_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            # Header
            writer.writerow([
                "Account Number",
                "Customer ID",
                "Customer Name",
                "Phone",
                "Address",
                "Account Type",
                "Balance"
            ])

            for account in accounts:

                customer = account.get_customer()

                writer.writerow([
                    account.get_account_number(),
                    customer.get_customer_id(),
                    customer.get_name(),
                    customer.get_phone(),
                    customer.get_address(),
                    account.account_type(),
                    account.get_balance()
                ])

    # ==========================================================
    # Load Accounts
    # ==========================================================

    @staticmethod
    def load_accounts():

        accounts = []

        if not os.path.exists(FileManager.ACCOUNTS_FILE):
            return accounts

        with open(FileManager.ACCOUNTS_FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                customer = Customer(
                    row["Customer ID"],
                    row["Customer Name"],
                    row["Phone"],
                    row["Address"]
                )

                if row["Account Type"] == "Savings":

                    account = SavingsAccount(
                        int(row["Account Number"]),
                        customer,
                        float(row["Balance"])
                    )

                else:

                    account = CurrentAccount(
                        int(row["Account Number"]),
                        customer,
                        float(row["Balance"])
                    )

                accounts.append(account)

        return accounts

    # ==========================================================
    # Save Transaction
    # ==========================================================

    @staticmethod
    def save_transaction(transaction):

        file_exists = os.path.isfile(FileManager.TRANSACTIONS_FILE)

        with open(FileManager.TRANSACTIONS_FILE, "a", newline="") as file:

            writer = csv.writer(file)

            if not file_exists:

                writer.writerow([
                    "Account Number",
                    "Transaction Type",
                    "Amount",
                    "Date & Time"
                ])

            writer.writerow([
                transaction.get_account_number(),
                transaction.get_transaction_type(),
                transaction.get_amount(),
                transaction.get_date_time()
            ])

    # ==========================================================
    # Load Transactions
    # ==========================================================

    @staticmethod
    def load_transactions():

        transactions = []

        if not os.path.exists(FileManager.TRANSACTIONS_FILE):
            return transactions

        with open(FileManager.TRANSACTIONS_FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                transaction = Transaction(
                    int(row["Account Number"]),
                    row["Transaction Type"],
                    float(row["Amount"])
                )

                transactions.append(transaction)

        return transactions