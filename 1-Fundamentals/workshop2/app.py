from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
while True:
    name = input("Enter name to register: ")
    if len(name) > 10:
        print("The maximum name length is 10 characters.")
        continue
    pin = input("Enter Pin: ")
    if len(pin) < 4 or len(pin) > 4:
        print("PIN must contain 4 numbers! Please Try again!")
        continue
    balance = 0
    print(name, " has been registered with a starting balance of $" + str(balance))

    print("          === Automated Teller Machine ===          ")

    while True:
        print("LOGIN")
        name_to_validate = (input("Enter name: "))
        pin_to_validate = (input("Enter PIN: "))
        if name_to_validate == name and pin_to_validate == pin:
            print("Login successful!")
            break
        else:
            print("Invalid credentials")
    while True:
        atm_menu(name)
        option = input("Choose an Option: ")
        if option == "1":
            # the base balance is $0 but after updating the balance inside the while loop using deposit/withdraw, the new balance will be updated
            print("Current Balance: $" + str(balance))
        elif option == "2":
            balance = account.deposit(balance)
            print("Current Balance: $" + str(balance))
        elif option == "3":
            balance = account.withdraw(balance)
            print("Current Balance: $" + str(balance))
        elif option == "4":
            account.logout(name)
            quit()
        else:
            print("Pick only 1-4")
