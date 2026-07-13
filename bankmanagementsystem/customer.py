class Customer:
    """
    Represents a bank customer.
    """

    def __init__(self, customer_id, name, phone, address):
        self.__customer_id = customer_id
        self.__name = name
        self.__phone = phone
        self.__address = address

    # ---------- Getters ----------

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address

    # ---------- Setters ----------

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_address(self, address):
        self.__address = address

    # ---------- Display ----------

    def display(self):
        print("\nCustomer Details")
        print("---------------------------")
        print(f"Customer ID : {self.__customer_id}")
        print(f"Name        : {self.__name}")
        print(f"Phone       : {self.__phone}")
        print(f"Address     : {self.__address}")