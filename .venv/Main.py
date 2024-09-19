import Checkings_Account
import Savings_Account
Checking_1 = Checkings_Account.Checkings_Account("Steve",1000,500, 1234, 5678,750)
Checking_2 = Checkings_Account.Checkings_Account("Kevin",1500,250, 2345, 6789,500)
Saving_1 = Savings_Account.Savings_Account("Sarah",1250,750, 3456, 7890,1.01)
Saving_2 = Savings_Account.Savings_Account("Betsy",2500,500, 4567, 8901,1.05)
Checking_1.deposit(1000)
Checking_1.withdraw(750)
Checking_1.print_customer_information()
print(Checking_1.transfer_limit)
Checking_2.deposit(100)
Checking_2.withdraw(250)
Checking_2.print_customer_information()
print(Checking_2.transfer_limit)
Saving_1.deposit(750)
Saving_1.withdraw(500)
Saving_1.print_customer_information()
print(Saving_1.interest_rate)
Saving_2.withdraw(2001)
Saving_2.print_customer_information()
print(Saving_2.interest_rate)


