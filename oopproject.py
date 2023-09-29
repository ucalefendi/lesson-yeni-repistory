from  bank1 import *

Dave = BankAccount(1000,'Dave')
# Sara = BankAccount(150,'Sara')

# Dave.getBalance()
# Sara.getBalance()


Dave.deposit(500)
Dave.withdraw(100)
Dave.deposit(1000)
Dave.withdraw(200.0000)
Dave.transfer(10000000,Dave)

Elcin=InterestRewards(20,'Elcin')
Elcin.deposit(10)
Elcin.transfer(120,Dave)
Blaze = SavingAccount(100,'Blaze')
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(20,Elcin)


