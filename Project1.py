# bank account class with two attribues;
#   owner
#   balance
#
#   two methods
    # deposit
    # withdrawl
#   withdrawls may not exceed balance
#


class Account():
    
    def __init__(self,acc_holder,balance):
        self.acc_holder = acc_holder
        self.balance = balance
    
    def __repr__(self):
        return f"Owner: {self.acc_holder}\nAccount Balance: {self.balance}"

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit was accepted.")

    def withdrawl(self,amount):
        if (self.balance - amount < 0):
            print ("Insufficient funds for that withdrawl")
        else:
            self.balance = self.balance - amount
            print("Withdrawl processed!")

        


# 1 instanciate the class
acct1 = Account("Jose", 100)

# 2 print the object
print("Initial account details")
print(acct1)

# 3 show owner
print("Account holder:")
print(acct1.acc_holder)

# 4 show balance
print("Account Balance")
print(acct1.balance)

# 5 make a series of deposits and withdrawls
print("Making deposit of $500")
acct1.deposit(500)
print("New balance:")
print(acct1.balance)

print("Attempting to make withdrawl of $4000")
acct1.withdrawl(4000)
print("New Account Balance:")
print(acct1.balance)
# 6 make withdrawl that exceeds balance.

