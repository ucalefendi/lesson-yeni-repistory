
#parent class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details")    
        print("")    
        print("Name",self.name)    
        print("Age",self.age)    
        print("gender",self.gender)   

# ucal = User('Ucal',29,'Male')         
# ucal.show_details()

#child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        print("Account has been updated:",f'{self.balance}')
    

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("insufficient funds - Balance avilable:" ,self.balance)
        else : 
            self.balance -= self.amount 
            print("Account balance has been updated :",self.balance)

    def view_balance(self):
        self.show_details() 
        print("Account balance has been updated :",self.balance)       




ucal = Bank('Ucal',29,'Male') 
ucal.withdraw(100)  

