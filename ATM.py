from datetime import datetime

currentDate = datetime.now()

customersList = ["Kuzayet", "Pam", "Ovie", "Akpan", "Idibia"]
customersPassword = ["K1234", "P1234", "O1234", "A1234", "I1234"]
customersBalance = [1000, 2000, 3000, 500, 2000]


name = input("What is your name? \n")

while name in customersList:
    password = input("What is your password? \n")
    userId = customersList.index(name)

    if password == customersPassword[userId]:
        print("Welcome %s" % name)

        print("Time: %s" % currentDate)

        print("1. Withdraw")
        print("These are the available options:")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Complaint")

        selectedOption = int(input("please select an option: "))

        if selectedOption == 1:
            withdraw = int(
                input("How much would you like to withdraw? \n"))
            userBalance = customersList.index(name)

            if customersBalance[userBalance] > withdraw:
                customersBalance[userBalance] = customersBalance[userBalance] - withdraw

                print("Take your cash")

            else:
                print("Insufficient Balance")

        elif selectedOption == 2:
            deposit = int(input("How much would you like to deposit? \n"))
            userBalance = customersList.index(name)

            customersBalance[userBalance] = customersBalance[userBalance] + deposit
            print("Deposit successful")

        elif selectedOption == 3:
            userBalance = customersList.index(name)
            print("Your balance is %s" % customersBalance[userBalance])

        elif selectedOption == 4:
            input("What issue will you like to report? \n")

            print("Thank you for contacting us")

        else:
            print("Option selected is invalid, please try again")

    else:
        print("Password is incorrect, please try again")
        break

    print("Do you want to perform another transaction?")
    print("1. Yes")
    print("2. No")

    anotherTranscation = int(input("Please select an option: \n"))

    if anotherTranscation == 1:
        continue

    else:
        break


else:
    print("Name not found, please try again")
