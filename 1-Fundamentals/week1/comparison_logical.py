"""
Comparison Operators and Boolean Expressions
"""
X = 100
Y = 200

print(X != Y)       # X is not equal to Y
print(X > Y)        # X is greater than Y
print(X < Y)        # X is less than Y
print(X >= Y)       # X is greater than or equal to Y
print(X <= Y)       # X is less than or equal to Y

"""
Logical operators
"""
# "and" must be both true to become true
# "or" need atleast one true to become true
# "not" not true is false and not false is true
x = 100
y = 200
z = 100

print(x < y and y > z)
print(x > y or y > z)
print(not (x > y or y > z))
