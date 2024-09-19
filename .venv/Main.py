import Checkings_Account
import Savings_Account
Checking_1 = Checkings_Account.Checkings_Account("Steve",1000,500, 1234, 5678,750)
Checking_2 = Checkings_Account.Checkings_Account("Kevin",1500,250, 2345, 6789,500)
Saving_1 = Savings_Account.Savings_Account("Sarah",1250,750, 3456, 7890,1.01)
Saving_2 = Savings_Account.Savings_Account("Betsy",2500,500, 4567, 8901,1.05)
Checking_1.deposit_check(1000)
Checking_1.withdraw(750)
Checking_1.print_customer_information()
checking_2.deposit_check(100)
Checking_2.withdraw(1000)
Checking_2.print_customer_information()
Saving_1.deposit_check(750)
Saving_1.withdraw(500)
Saving_1.print_customer_information()
Saving_1.withdraw(2001)
Saving_1.print_customer_information()


