class BankAccount:
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = 0

    def get_balance(self):
        return self.balance
    
    def get_owner(self):
        return self.owner
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("new balance is ",self.balance)
    
    def withdraw(self,amount):
        self.balance=self.balance-amount
        print("new balance is ",self.balance)
        if amount > self.balance:
            print("erreur")
    def transfer(self,amount,account):
        self.withdraw(amount)
        account.deposit(amount)
        print("new balance is ",self.balance)
        print("new balance is ",account.balance)

a1 = BankAccount("Alice",100)
a2 = BankAccount("Bob",500)
print(a1.get_balance())
print(a1.get_owner())
a1.deposit(100)
print(a1.get_balance()) 
a1.withdraw(50)
print(a1.get_balance()) 
a1.transfer(25, a2)
print(a1.get_balance())
print(a2.get_balance())