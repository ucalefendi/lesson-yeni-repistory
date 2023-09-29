class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initamount,accName):
        self.balance = initamount
        self.name = accName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")


    def getBalance(self):
        print(f"\nAccount '{self.name}' balance $ {self.balance:.2f}")    

    def deposit(self,amount):
        self.balance += amount
        print(f" '{self.balance}'  \nDeposit complete.\nAccount '{self.name}' balance $ {self.balance:.2f}") 

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"sorry,account '{self.name}' only has a balance of $'{self.balance:.2f}'")
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')   


    def transfer(self,amount,account):
        try:
            print('Beginning transfer operation')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('Transfer complete')
        except BalanceException as error:
            print(f'Transfer interrupted.{error}')    

class InterestRewards(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print('\nDeposit complete.')
        self.getBalance()

class SavingAccount(InterestRewards):
    def __init__(self, initamount, accName):
        super().__init__(initamount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee) 
            print("\nWithdraw is completed")         
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")       
            
        
