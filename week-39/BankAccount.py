class BankAccount:
    __account_holder = ""
    __balance = 0.0
    
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount
    
    def display_balance(self):
        return f'<< Name: {self.__account_holder} \
            ** Balance: {self.__balance}$ >>'
    
    
def test():
    myAccount = BankAccount("Junaid", 2500.00)
    myAccount.deposit(5000)
    print(myAccount.display_balance())
    
    myAccount.withdraw(2000)
    print(myAccount.display_balance())
    
    
if __name__ == "__main__":
    test()
    