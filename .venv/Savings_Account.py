import Bank
class Savings_Account(Bank.Bank):
    def __init__(self,name, bal, minBal,Acc_num,route_num):
        super.__init__(name, bal, minBal)
        self._account_number = Acc_num
        self.__routing_number = route_num