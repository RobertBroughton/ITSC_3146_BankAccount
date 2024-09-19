import Bank
class Checkings_Account(Bank.Bank):
    def __init__(self,name, bal, minBal,acc_num,route_num,trans_limit):
        super.__init__(name, bal, minBal,acc_num,route_num)
        self.transfer_limit = trans_limit
