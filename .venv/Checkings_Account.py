import Bank
class Checkings_Account(Bank.Bank):
    def __init__(self,name, bal, minBal,acc_num,route_num,trans_limit):
        super().__init__(name, bal, minBal,acc_num,route_num)
        self.transfer_limit = trans_limit
    #overloaded Method
    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance & amount > self.transfer_limit:
            print("Error: Insufficient Funds Available")
        else:
            self.current_balance -= amount
