# class BankLogin:
#     def __init__(self,name,acc_num,pin,balance):
#         self.name=name
#         self.acc_num=acc_num
#         self.pin=pin
#         self.balance=balance
    
#     def login(self):
#         name=input("Enter your Name : ")
#         acc_num=input("Enter 12 Digit Account Number : ")
#         pin=input("Enter a 6 digit PIN : ")

#     #name check
#         if name!=self.name:
#             print("Wrong Name ")
#             return False
#         #acc number
#         if acc_num!=self.acc_num:
#             print("Worng Account Number")
#             return False
#         # pin 
#         if pin!=self.pin:
#             print("Worng PIN")
#             return False
#         print("Login Successful!")
#         return True
    
class BankLogin:

    def __init__(self, name, acc_num, pin, balance):

        self.name = name
        self.acc_num = acc_num
        self.pin = pin
        self.balance = balance

    def login(self):

        name = input("Enter Your Name : ")
        acc_num = input("Enter 12 Digit Account Number : ")
        pin = input("Enter 6 Digit PIN : ")

        # Name Check
        if name != self.name:
            print("Wrong Name")
            return False

        # Account Number Validation
        if len(acc_num) != 12 or not acc_num.isdigit():
            print("Account Number Must Be 12 Digits")
            return False

        # Account Number Check
        if acc_num != self.acc_num:
            print("Wrong Account Number")
            return False

        # PIN Validation
        if len(pin) != 6 or not pin.isdigit():
            print("PIN Must Be 6 Digits")
            return False

        # PIN Check
        if pin != self.pin:
            print("Wrong PIN")
            return False

        print("\nLogin Successful!")

        return True