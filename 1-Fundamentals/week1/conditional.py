"""
Conditional Statement
"""
weather = "cold"

if weather == "cold":
    print("Wear a Jacket")

# Chained Conditional
x = 5
if x < 2:
    print("small")
elif x < 10:
    print("Medium")
else:
    print("Large")

# Nested Condition
# Best if avoided. Use Nested operators instead
if x > 1:
    print("More than one")
    if x < 100:
        print("Less than 100")
print("All done")

# Nested Operator
if x > 1 and x < 100:
    print("More than one")
    print("Less than 100")
print("All Done")
