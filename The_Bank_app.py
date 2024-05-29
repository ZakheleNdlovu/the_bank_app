import time
import mysql.connector
balance = 0
name = input("Name: ")


def updatePassword(password):
    while True:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='clients'
        )
        new_password = input("Enter your new Password: ")
        confirm_password = input("Confirm your new Password: ")
        if new_password == confirm_password:
            c = conn.cursor()
            q = f'update accounts set password="{new_password}"where password="{password}"'
            c.execute(q)
            conn.commit()
            c.close()
            conn.close()
            print("password successfully changed")
            break
        else:
            print("passwords don't match")


def updateEmail(email):
    while True:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='clients'
        )
        new_email = input("Enter your new Password: ")
        confirm_email = input("Confirm your new Password: ")
        if new_email == confirm_email:
            c = conn.cursor()
            q = f'update accounts set email="{new_email}"where email="{email}"'
            c.execute(q)
            conn.commit()
            c.close()
            conn.close()
            print("E-mail successfully changed")
            break
        else:
            print("E-mails don't match")


def getbalance():
    global name
    global balance
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
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
        password='',
        database='clients'
    )
    c = conn.cursor()
    q = f'update accounts set balance="{balance}"where name="{name}"'
    c.execute(q)
    conn.commit()
    c.close()
    conn.close()


def register():
    while True:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='clients'
        )
        print("let's create an account for you")
        time.sleep(1)
        name = input("Name: ")
        time.sleep(1)
        surname = input('Surname: ')
        time.sleep(1)
        email = input("E-mail: ")
        time.sleep(1)
        date_of_birth = input('Date of birth(YYYY-MM-DD): ')
        time.sleep(1)
        balance = int(input('Deposit: '))
        time.sleep(1)
        password = input("Password: ")
        time.sleep(1)
        c = conn.cursor()
        q = 'insert into accounts(name,surname,email,date_of_birth,password,balance) values(%s,%s,%s,%s,%s,%s)'
        v = (name, surname, email, date_of_birth, password, balance)
        c.execute(q, v)
        conn.commit()
        c.close()
        conn.close()
        print("Account successfully created :)")
        break


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
        transaction = int(input("1. Deposit\n2. Withdrawal\n3. Buy prepaid\n4. Check Balance\n5. Update Account\n6. Exit\n: "))

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
                update = int(input("What would you like to update?\n1. E-mail\n2. Password\n: "))
                if update == 1:
                    email = input("Enter your old E-mail: ")
                    updateEmail(email)
                elif update == 2:
                    password = input("your old password: ")
                    updatePassword(password)
                else:
                    print('invalid choice!')

            case 6:
                exit("Goodbye")


def login():
    global balance
    while True:
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
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
                if name_.lower() == name.lower() and password_ == password:
                    print("log in successful")
                    break
                else:
                    print("incorrect log in details")
            except:
                print('Account not in database')

        except:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            c = conn.cursor()
            q = f'create database clients'
            c.execute(q)
            conn.commit()
            c.close()
            register()



print(f"Hello {name}")
account = input("Do you have an account?\nPress y for yes or n for no: ")
if account.lower() == 'y':
    login()
    transact()

elif account == 'n':
    register()

while True:
    login()
    transact()

