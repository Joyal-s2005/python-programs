class BankAccount:
    def __init__(self):
        self.balance=0
        print("Welcome to the Bank")
    def deposit(self):
        amount=float(input("Enter amount to be deposited: "))
        self.balance +=amount
        print("Amount deposited:",amount)
    def withdraw(self):
        amount=float(input("Enter amount to be withdrawn:"))
        if self.balance >=amount:
            self.balance -=amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Net available balance=",self.balance)
    

account1=BankAccount()
account1.deposit()
account1.withdraw()
account1.display()