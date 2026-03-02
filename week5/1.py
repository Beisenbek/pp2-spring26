class Account:
    def __init__(self, number):
        self.number = number 
        self.__value = 0
    
    def print(self):
        print(f"Account number: {self.number}, Value: {self.__value}")
    
    def transfer(self, amount):
        self.__value += amount

    def top_up(self, amount):
        self.__value += amount




account = Account(123)
account.print()
account.top_up(2000)
account.print()
account.transfer(500)
account.print()
#account.__value += 1000000
#account.print()

