from abc import ABC, abstractmethod


class Account(ABC):
    """
    Abstract Base Class for all bank accounts.
    """

    from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, account_number, customer, balance=0):

        self.__account_number = account_number
        self.__customer = customer
        self.__balance = balance

    # ---------- Getters ----------

    def get_account_number(self):
        return self.__account_number

    def get_customer(self):
        return self.__customer

    def get_balance(self):
        return self.__balance

    # ---------- Deposit ----------

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.__balance += amount

    # ---------- Balance Update ----------

    def _set_balance(self, balance):
        self.__balance = balance

    # ---------- Abstract Methods ----------

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def account_type(self):
        pass

    # ---------- Display ----------

    def display(self):

        print("\n==============================")
        print("ACCOUNT DETAILS")
        print("==============================")

        print(f"Account Number : {self.__account_number}")
        print(f"Customer Name  : {self.__customer.get_name()}")
        print(f"Phone          : {self.__customer.get_phone()}")
        print(f"Account Type   : {self.account_type()}")
        print(f"Balance        : ₹{self.__balance:.2f}")