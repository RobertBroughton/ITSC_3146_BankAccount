class Bank:
    title_of_bank = "Title of Bank"
    def __init__(self,name, bal, minBal,acc_num,route_num):
        self.customer_name = name
        self.current_balance = bal
        self.minimum_balance = minBal
        self._account_number = acc_num
        self.__routing_number = route_num
    def deposit(self, amount):
        self.current_balance += amount
    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("Error: Insufficient funds")
        else:
            self.current_balance -= amount
    def print_customer_information(self):
        print("Bank Title: ",self.title_of_bank,"\nCustomer Name: ",self.customer_name,"\nCurrent Balance: ",self.current_balance, "\nMinimum Balance: ",self.minimum_balance, "\n")
