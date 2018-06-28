# Creating a Bank Account Object

# Class
class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# Object Instance
account = Account("bank_account_example\\balance.txt")

#Inheritance(Subclass)
class Checking(Account):
    #Doc Strings
    """This class generates checking account objects"""

    #Class Variable
    type = 'checking'

    #Contructor
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    #Class Method
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

#Instantiation
checking = Checking("bank_account_example\\balance.txt", 1)
checking.transfer(100)
print(checking.balance)
print(checking.type)
print(checking.__doc__)
checking.commit()