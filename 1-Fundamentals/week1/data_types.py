# Primitive Variables
name = "Patrick"  # String
age = 23  # Integer
cash = 350.46  # Float
retired = False  # Boolean

# How to know the Data type of a variable
# Invoking the Function type(<Variable Name>)
print("Data type of the variable 'name' is", type(name))
print("Data type of the variable 'age' is", type(age))
print("Data type of the variable 'cash' is", type(cash))
print("Data type of the variable 'retired' is", type(retired))

# Composite Data types
my_locations = ["Colorado", "Philippines", "Japan"]  # Storing a LIST
Patrick_Info = {"name": "Patrick", "age": 23,
                "cash": 350.46, "retired": False}  # Storing a DICTIONARY
my_tuple = ("apple", "banana", "cherry")  # Storing a TUPLE
my_set = {"cats", "dogs", "birds"}  # Storing a SET

print("Data type of the variable 'my_locations' is", type(my_locations))
print("Data type of the variable 'Patrick_Info' is", type(Patrick_Info))
print("Data type of the variable 'my_tuple' is", type(my_tuple))
print("Data type of the variable 'my_set' is", type(my_set))
