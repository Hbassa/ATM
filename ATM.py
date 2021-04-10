from datetime import datetime
import random

currentDate = datetime.now()

database = {}

def init():

        print("Welcome To Bank Py")

        haveAccount = int(
            input("Do you have and account with us? 1. (Yes) 2. (No) \n"))

        if haveAccount == 1:
            login()
        elif haveAccount == 2:
            register()
        else:
            print("You have selected an invalid option")
            init()

def login():
        print("*****login*****")

        accountNumberFromUser = int(input("What is your account number? \n"))
        password = input("what is your password? \n")

        for accountNumber,userDetails in database.items():
            if accountNumber == accountNumberFromUser:
                if userDetails[3] == password:
                    bankOperation(userDetails)
            else:
                print("invalid account number")
        login()

def register():

        print("*****Register*****")
        email = input("what is your email address? \n")
        first_name = input("what is your first name? \n")
        last_name = input("what is your last name? \n")
        password = input("generate a password for yourself \n")
        balance = int(input("how much do you want to deposit into your new account? \n"))
        accountNumber = generatingAccountNumber()

        database[accountNumber] = [email, first_name, last_name, password, balance]

        print("your account has been generated")
        print("================================")
        print("your account number is %d:" % accountNumber)
        print("================================")
        print("keep it safe")

        login()

def bankOperation(user):

        print("welcome %s %s" % (user[0], user[1]))
        print("Time: %s" % currentDate)

        selectedOption = int(input("what would you like to do? 1. (deposit) 2. (withdraw) 3. (check balance) 4. (complaint) 5. (logout) 6. (exit) \n"))

        if selectedOption == 1:
            depositOperation(user)

        elif selectedOption == 2:
            withdrawOperation(user)

        elif selectedOption == 3:
            balanceOperation(user)

        elif selectedOption == 4:
            complaint()

        elif selectedOption == 5:
            logout()     

        elif selectedOption == 6:
            exit()

        else:
            print("invalid option selected")
            bankOperation(user)

def depositOperation(user):
        print("*****deposit*****")
        deposit = int(input("How much do you want to deposit? \n"))
        user[4] = user[4] + deposit

        print("Deposit Successful")

def withdrawOperation(user):
        print("*****withdraw****")
        withdraw = int(input("How much would you like to withdraw? \n"))
        
        if user[4] > withdraw:
            user[4] = user[4] - withdraw
            print("Take your cash")

        else:
            print("Insufficient Balance")

def balanceOperation(user):
        print("****balance****")

        print("your balance is %d" % user[4])

def complaint():
        input("What issue will you like to report? \n")

        print("Thank you for contacting us")

def logout():
        login()


def generatingAccountNumber():
        return random.randrange(1111111111, 9999999999)


init()
