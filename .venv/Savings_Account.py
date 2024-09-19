import Bank
class Savings_Account(Bank.Bank):
    def __init__(self,name, bal, minBal,acc_num,route_num, interest):
        super.__init__(name, bal, minBal,acc_num,route_num)
        self.interest = interest