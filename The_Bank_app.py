import time
running = True
class account():
    def __init__(self, account_holder , balance):
        self.account_holder = account_holder

        self.balance = int(balance)

    def changeName(self):
        name = input("Name: ")
        self.account_holder = name
        print(self.account_holder)

    def deposit(self):
        deposit = int(input("Deposit: "))
        self.balance = self.balance + deposit
        print('Your balance is: R',self.balance,'\n')

    def withDraw(self):
        Amount = int(input("Amount: "))
        if Amount > self.balance:
            print("Account cannot have a negative balance!")

        else:
            self.balance = self.balance - Amount
            print('Your balance is: R',self.balance,'\n')


    def getBalance(self):
        print(self.balance,'\n')

    def getName(self):
        print(self.account_holder,'\n')

print("88*------ THE BANK ------*88\n")
clients = []
name = input("Name: ")

balance = int(input("Balance: "))
acc = account(name,  balance)
clients.append(acc)

time.sleep(1)
print(f'\nHello {name}, welcome to *The Bank*\n')

time.sleep(1)
print("1. Deposit\n2. Withdrawal \n3. Account holder \n4. Exit\nChoose 1,2,3 or 4")

try:
    insert = int(input(":"))
except ValueError as e:
    print(e)
    print("Please choose between 1 and 2 Genius!!")

if insert == 1:
    acc.deposit()

if insert == 2:
    acc.withDraw()

if insert == 3:
    acc.getName()

if insert == 4:
    print("Goodbye")
    print(e)

while running:
    transact_again = input('You you like to perform another transaction?\nPress "y"  for yes or "n" for no: ')
    time.sleep(1)
    if transact_again.lower() == 'y':

        time.sleep(1)
        print("1. Deposit\n2. Withdrawal \n3. Account holder \n4. Exit\nChoose 1,2,3 or 4\n")

        try:
            insert = int(input(":"))
        except ValueError as e:
            print(e)
            print("Please choose between 1 and 4 Genius!!")


        if insert == 1:
            acc.deposit()

        if insert == 2:
            acc.withDraw()

        if insert == 3:
            acc.getName()

        if insert == 4:
            print("Goodbye")
            print(e)

    elif transact_again.lower() == 'n':
        print('\nThank you, Goodbye!')
        exit(0)

