# Import Random Lessons
import random
# Randint()
print(random.randint(1, 100))

# Choice()
pets = ['cat', 'dog', 'bird', 'dinosaur']
print(random.choice(pets))

# Shuffle()
country = ["Philippines", "Japan", "USA"]
random.shuffle(country)
print(country)


# Can also use this on a def function

def rand_int(x, y):
    return random.randint(x, y)


print(rand_int(0, 10))


# Import Random Exercise

pips = random.randint(1, 6)
print("You roll the die... it lands with", pips, "pips showing.")

prizes = ["a car", "$10000", "a pony", "$500000"]
prize_won = random.choice(prizes)
print("You turn the wheel of fortune... It lands on a prize of", prize_won + "!!")

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(cards)
print(cards)
