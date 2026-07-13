from bank import Bank


def display_menu():
    """
    Display the main menu.
    """
    print("\n")
    print("=" * 50)
    print("        BANK MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Search Account")
    print("6. Display All Accounts")
    print("7. Delete Account")
    print("8. Transaction History")
    print("9. Exit")
    print("=" * 50)


def main():

    bank = Bank()

    while True:

        display_menu()

        try:

            choice = int(input("Enter your choice : "))

            # --------------------------------------------------
            # Create Savings Account
            # --------------------------------------------------

            if choice == 1:

                print("\nCreate Savings Account")

                account_number = int(input("Account Number : "))
                customer_id = input("Customer ID : ")
                name = input("Customer Name : ")
                phone = input("Phone Number : ")
                address = input("Address : ")
                balance = float(input("Initial Balance : "))

                bank.create_savings_account(
                    account_number,
                    customer_id,
                    name,
                    phone,
                    address,
                    balance
                )

            # --------------------------------------------------
            # Create Current Account
            # --------------------------------------------------

            elif choice == 2:

                print("\nCreate Current Account")

                account_number = int(input("Account Number : "))
                customer_id = input("Customer ID : ")
                name = input("Customer Name : ")
                phone = input("Phone Number : ")
                address = input("Address : ")
                balance = float(input("Initial Balance : "))

                bank.create_current_account(
                    account_number,
                    customer_id,
                    name,
                    phone,
                    address,
                    balance
                )

            # --------------------------------------------------
            # Deposit
            # --------------------------------------------------

            elif choice == 3:

                account_number = int(input("Account Number : "))
                amount = float(input("Deposit Amount : "))

                bank.deposit_money(
                    account_number,
                    amount
                )

            # --------------------------------------------------
            # Withdraw
            # --------------------------------------------------

            elif choice == 4:

                account_number = int(input("Account Number : "))
                amount = float(input("Withdrawal Amount : "))

                bank.withdraw_money(
                    account_number,
                    amount
                )

            # --------------------------------------------------
            # Search Account
            # --------------------------------------------------

            elif choice == 5:

                account_number = int(input("Account Number : "))

                bank.display_account(account_number)

            # --------------------------------------------------
            # Display All Accounts
            # --------------------------------------------------

            elif choice == 6:

                bank.display_all_accounts()

            # --------------------------------------------------
            # Delete Account
            # --------------------------------------------------

            elif choice == 7:

                account_number = int(input("Account Number : "))

                bank.delete_account(account_number)

            # --------------------------------------------------
            # Transaction History
            # --------------------------------------------------

            elif choice == 8:

                account_number = int(input("Account Number : "))

                bank.show_transaction_history(account_number)

            # --------------------------------------------------
            # Exit
            # --------------------------------------------------

            elif choice == 9:

                print("\nThank you for using Bank Management System.")
                print("Goodbye!")

                break

            # --------------------------------------------------
            # Invalid Choice
            # --------------------------------------------------

            else:

                print("\nInvalid choice. Please try again.")

        except ValueError:

            print("\nInvalid input. Please enter the correct data type.")

        except Exception as error:

            print("\nUnexpected Error:", error)


if __name__ == "__main__":
    main()