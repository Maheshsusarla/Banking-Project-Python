from login import BankLogin
from deposit import Deposit
from withdraw import Withdraw
from balance import Balance


class Bank(BankLogin,Deposit,Withdraw,Balance):
    # Constructor
    def __init__(self, name, acc_num, pin, balance):
        BankLogin.__init__(self,name,acc_num,pin,balance)


# Object Creation
user = Bank("Mahesh","1234","123456",5000)


print("\n====== WELCOME TO PYTHON BANK ======")

# Login
if user.login():

    # User Details
    user.check_balance()

    while True:
        print("\n------ BANK MENU ------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter Your Choice : ")

        # Deposit
        if choice == "1":
            user.deposit()

        # Withdraw
        elif choice == "2":
            user.withdraw()

        # Balance
        elif choice == "3":
            user.check_balance()

        # Exit
        elif choice == "4":
            print("\nThank You For Using Python Bank")
            break

        else:
            print("Invalid Choice")