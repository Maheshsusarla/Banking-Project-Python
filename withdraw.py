class Withdraw:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self):
        amount=float(input("\nEnter Withdraw Amount : "))
        if amount>self.balance:
            print("Insufficient Balance")
        elif amount<=0:
            print("Invalid Amount")
        else:
            self.balance-=amount
            print("Withdraw Successful!")
            print("Remaining Balance :",self.balance)
