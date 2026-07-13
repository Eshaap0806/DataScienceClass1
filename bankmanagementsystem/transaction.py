from datetime import datetime


class Transaction:
    """
    Represents a bank transaction.
    """

    def __init__(self,account_number,transaction_type,amount,date_time=None):
        if date_time is None:
            self.__date_time = datetime.now()
        else:
            self.__date_time = date_time

        self.__account_number = account_number
        self.__transaction_type = transaction_type
        self.__amount = amount
        

    # ---------- Getters ----------

    def get_account_number(self):
        return self.__account_number

    def get_transaction_type(self):
        return self.__transaction_type

    def get_amount(self):
        return self.__amount

    def get_date_time(self):
        return self.__date_time

    # ---------- Display ----------

    def display(self):

        print("-------------------------------------")
        print("Transaction Details")
        print("-------------------------------------")
        print(f"Account Number : {self.__account_number}")
        print(f"Transaction    : {self.__transaction_type}")
        print(f"Amount         : ₹{self.__amount:.2f}")
        print(f"Date & Time    : {self.__date_time}")