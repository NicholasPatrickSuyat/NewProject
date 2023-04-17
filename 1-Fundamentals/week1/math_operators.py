"""
 Math Operators! In this lesson, it will teach us the basics of Math Operators
"""

# Addition
x = 1
y = 2
z = 3
xyz = x + y + z
x = x + 10  # New value of x because it is newer
y = y + 7  # New value of y because it is newer
z = z + 9  # New value of z because it is newer

# Subtraction
a = 1
b = 2
c = a - b

# Division
d = 1
e = 2
f = e / d  # This will answer in float value which is 1.0(Decimal)

# Floor Division
g = 1
h = 2
i = h // g  # This will answer in whole number

# Exponentiation
j = 3
k = 2
l = j ** k  # This will be 3^2

# Modulo
m = 23
n = 5
o = m % y  # This will answer the remainder of the division

"""
Operator Precedence Rules! In this lesson, it will teach us the order of Math operators when combined
"""
# Operators Precedence are not left and right!
# Parentheses > Exponentiation > Modulo Multiply Division > Addition Sub
# Also called PEMDAS

# Exponent first which is the 5^6 then Multi and Division then Add then Subtract
p = 1 + 2 * 3 - 4 / 5**6
print(p)
