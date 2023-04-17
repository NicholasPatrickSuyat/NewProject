# Modules

# using 'from import' is useful because you do not need to put the module file name infront of the variable
from my_module import greet, flavor
# import is used to bring the other file into this file.
import my_module as my_module

# This code is from function def greet(name): in (my_module). It is calling that function from other file
my_module.greet("Albert Einstein")
print("My favorite ice cream flavor is", my_module.flavor)


# from import


greet("Patrick")
print("I do not like ", flavor)
