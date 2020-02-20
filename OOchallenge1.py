class Account:
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
        
    def deposit(self, amount):
        self.balance + int(amount)
        print('Deposit Accepted')
        
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance - int(amount)
            print('Withdrawal Accepted')
        else:
            print('Insufficient Funds!')    
    
    
acct1 = Account('Alec', 100)