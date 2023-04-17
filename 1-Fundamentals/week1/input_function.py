"""
Input Function
"""
# Input function let's you ask the user to enter an input. It always end as a string
name = input("What is your name? ")
print("Hello " + name + "!")
print(type(name))

# Input While
while True:
    print("1. Number One")
    print("2. Number Two")
    print("3. Break out of infinite loop")
    option = input("Pick an option: ")
    if option == "1":
        print("You chose 1")
    elif option == "2":
        print("You chose 2")
    elif option == "3":
        print("Leaving the Loop!")
        break
    else:
        print("Invalid Command")
print("You have left the loop.")
