class Bank:
    title_of_bank = "Title of Bank"
    def __init__(self,name, bal, minBal):
        self.customer_name = name
        self.current_balance = bal
        self.minimum_balance = minBal
    def deposit(self, amount):
        self.current_balance += amount
    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("Error: Insufficient funds")
        else:
            self.current_balance -= amount
    def print_customer_information(self):
        print("Bank Title: ",self.title_of_bank,"\nCustomer Name: ",self.customer_name,"\nCurrent Balance: ",self.current_balance, "\nMinimum Balance: ",self.minimum_balance, "\n")
