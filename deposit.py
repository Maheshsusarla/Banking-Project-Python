class Deposit:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self):
        amount=float(input("\nEnter Deposit Amount :"))
        if amount>0:
            self.balance+=amount
            print("Amount Deposited Successfully!")
            print("Updated Balance :",self.balance)
        else:
            print("Invalied Amount")
