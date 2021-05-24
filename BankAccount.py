import re
class BankAccount:
    """Creating A bank account with name and balance and validating the inputs.\n
    Function: displayDetails() , displays name and balance\n
    \tdeposit(amount) Depositing Amount in the balance\n
    \twithdraw(amount Withdrawing Amount from the balance"""
    def __init__(self,name,balance):
        '''making the constructor and validating the parameters in it.'''
        self.name = name # initializing the name
        self.balance = balance # initializing the balance
        if self.name =="":
            raise ValueError("name cannot be empty") # if name is empty then raise ValueError
        if self.balance =="":
            raise ValueError("balance cannot be empty") # if balance is empty then raise ValueError
        self.balance = float(balance) # converting str to float
        if re.search('[\d\$\.\@\#\?]',self.name): # checking that the name doesn't have digits or symbols
            raise ValueError("name cannot include numbers or symbols")
        if re.match('[A-Za-z_\-]{11,}',self.name.replace(" ","")): # checking for more than 10 characters long name excluding the spaces
            raise ValueError("name is more than 10 characters long")
        if self.balance < 0: # checking for negative balance
            raise ValueError("balance cannot be negative")
        self.name = re.split(" ",self.name) # formating the name, splitting it into first middle (if it was in the input) last name
        self.name = [x.lower().capitalize() for x in self.name] # lowering all chars and then captializing the first letter of the word
        self.name= " ".join(self.name) # joining the list into one string
    def displayDetails(self):
        '''Displaying the name and the balance of the account'''
        print("name is: {}".format(self.name))
        print("balance is: {}".format(self.balance))

    def deposit(self,amount):
        '''Depositing Amount in the balance'''
        if amount <= 0: # if amount is negative , raise value error
            raise ValueError("amount cannot be zero or less")
        self.balance +=amount # adding the amount to the balance
    def withdraw(self,amount):
        '''Withdrawing Amount from the balance'''
        if amount <= 0:# if amount is negative , raise value error
            raise ValueError("amount cannot be zero or less than zero")
        if amount > self.balance:# if amount is greater than the balance , raise value error
            raise ValueError("Insufficient funds")
        self.balance -=amount #subtracting the amount from the balance


'''b = BankAccount("joHn dBlack",10)
b.displayDetails()
b.deposit(10)
b.displayDetails()
b.withdraw(21)
b.displayDetails()'''
