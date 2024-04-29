import time
import mysql.connector

balance = 0
name = input("Name: ")


def getbalance():
    global name
    global balance
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='superunlock',
        database='clients'
    )
    time.sleep(1)
    c = conn.cursor()
    q = f'select * from accounts where name="{name}"'
    c.execute(q)
    r = c.fetchone()
    balance = r[6]
    conn.commit()
    c.close()
    conn.close()


def updateBalance(balance):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='superunlock',
        database='clients'
    )
    c = conn.cursor()
    q = f'update accounts set balance="{balance}"where name="{name}"'
    c.execute(q)
    conn.commit()
    c.close()
    conn.close()


def register():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='superunlock',
        database='clients'
    )
    print("let's create an account for you")
    time.sleep(1)
    name1 = input("Name: ")
    time.sleep(1)
    surname = input('Surname: ')
    time.sleep(1)
    email = input("E-mail: ")
    time.sleep(1)
    date_of_birth = input('Date of birth(YYYY-MM-DD): ')
    time.sleep(1)
    password = input("Password: ")
    time.sleep(1)
    c = conn.cursor()
    q = 'insert into accounts(name1,surname,email,date_of_birth,password) values(%s,%s,%s,%s,%s)'
    v = (name, surname, email, date_of_birth, password)
    c.execute(q, v)
    conn.commit()
    c.close()
    conn.close()


def transact():
    global balance
    getbalance()

    def buyPrepaid():
        global balance
        getbalance()
        while True:
            print("1. Buy Airtime\n2. Buy Data")
            reply = int(input(": "))
            match reply:
                case 1:
                    amount = int(input("R: "))
                    if amount > balance:
                        print("insufficient balance")
                        time.sleep(1)
                        print(f"Your balance is R{balance}")
                        break
                    if amount < balance:
                        balance = balance - amount
                        updateBalance(balance)
                        print(f"Your purchase is successful. You will receive an sms shortly")
                        print(f"Your balance is R{balance}")
                        time.sleep(1)
                        break
                case 2:
                    amount = int(input("R: "))
                    if amount > balance:
                        print("insufficient balance")
                        time.sleep(1)
                        print(f"Your balance is R{balance}")
                        break
                    if amount < balance:
                        balance = balance - amount
                        updateBalance(balance)
                        print(f"Your purchase is successful. You will receive an sms shortly")
                        print(f"Your balance is R{balance}")
                        time.sleep(1)
                        break

    while True:
        getbalance()
        print("Welcome to the Bank\n")
        time.sleep(1)
        transaction = int(input("1. Deposit\n2. Withdrawal\n3. Buy prepaid\n4. Check Balance\n5.Exit\n: "))

        match transaction:
            case 1:
                amount = int(input("Deposit amount: "))
                balance = balance + amount
                updateBalance(balance)
                print(f"Your new balance is R{balance}")


            case 2:
                amount = int(input("Amount: "))
                if amount > balance:
                    print("Amount cannot be more than the available balance")
                else:
                    balance = balance - amount
                    updateBalance(balance)
                    print(f"Your new balance is R{balance}")


            case 3:
                buyPrepaid()

            case 4:
                print(f"Your balance is R{balance}")

            case 5:
                exit("Goodbye")


def login():
    global balance
    while True:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='superunlock',
            database='clients'
        )
        name = input("Name: ")
        password = input("Password: ")
        c = conn.cursor()
        q = f'select * from accounts where name="{name}"'
        try:
            c.execute(q)
            r = c.fetchone()
            name_ = r[1]
            password_ = r[5]
            if name_ == name and password_ == password:
                print("log in successful")
                break
            else:
                print("incorrect log in details")
        except:
            print('Account not in database')


print("Hello")
account = input("Do you have an account?\nPress y for yes or n for no: ")

while True:
    if account.lower() == 'y':
        login()
        transact()

    elif account == 'n':
        register()
