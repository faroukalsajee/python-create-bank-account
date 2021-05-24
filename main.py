import BankAccount

while True:
    print("creating a bank account")
    print("enter the account holder name: ",end="")
    name=input() # getting name as an input
    print("enter the balance: ",end="")
    balance=input() # getting initial balance as an input
    try:
        account = BankAccount.BankAccount(name,balance) 
        account.displayDetails() # displaying details
        break
    except ValueError as e:
        print(" ",e)
        print("try again")
        continue
while True: # second loop to get transactions
    print("1 - deposit")
    print("2 - withdraw")
    print("enter your choice: ",end="")
    choice=input()
    if choice=="1":
        print(" your choice is  1")
        print("enter the amount to deposit: ",end="")
        deposit=float(input())
        try:
            account.deposit(deposit)
        except ValueError as e:
            print(" ",e)
    elif choice=="2":
        print(" your choice is  2")
        print("enter the amount to withdraw: ",end="")
        withdraw=float(input())
        try:
            account.withdraw(withdraw)
        except ValueError as e:
            print(" ",e)
    print("do you want to make another transaction?yes/no: ",end="")
    answer = input()
    if answer.lower() =="yes":
        continue
    else:
        break
