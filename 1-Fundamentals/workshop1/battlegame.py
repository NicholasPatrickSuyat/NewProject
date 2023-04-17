# Nicholas Patrick Suyat

# Character
wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"

# HitPoints
wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 80
dragon_hp = 300

# Damages
wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 150
dragon_damage = 50

print("****************************************************************")
name = input("Hello Adventurer! What is your name: ")
print("Welcome ", name, " To the world of Azerath")
ready = input("Are you ready to start this amazing adventure? ").lower()
if ready == "yes":
    print("Here we go!")
else:
    print("Let me know when you are ready!")
    exit()

while True:
    print("1)  Wizard ")
    print("2)  Elf ")
    print("3)  Human ")
    print("4)  Orc")
    character = input("Choose your character: ")
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("You have chosen the character: ", character)
        print("Health: ", my_hp)
        print("Damage: ", my_damage)
        break
    elif character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print("You have chosen the character: ", character)
        print("Health: ", my_hp)
        print("Damage: ", my_damage)
        break
    elif character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print("You have chosen the character: ", character)
        print("Health: ", my_hp)
        print("Damage: ", my_damage)
        break
    elif character == "4":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        print("You have chosen the character: ", character)
        print("Health: ", my_hp)
        print("Damage: ", my_damage)
        break
    else:
        print("Unknown character")
print("Let's Battle with the Dragon!", "\n")
print("****************************************************************")
while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now: ", dragon_hp, "\n")
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

    my_hp = my_hp - dragon_damage
    print("The Dragon Strikes back at ", character)
    print("The", character + "'s hitpoint are now: ", my_hp, "\n")
    if my_hp <= 0:
        print("You have lost the battle!", "\n")
        break
again = input("Would you like to continue? ").lower()
if again == "yes":
    print("The God's have given you one more health!")

else:
    print("I can't believe you admitted defeat!")
    exit()
