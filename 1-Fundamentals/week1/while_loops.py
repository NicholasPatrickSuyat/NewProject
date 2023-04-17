"""
While loop
"""
# While loop
n = 6
while n > 0:
    print(n)
    n = n - 1
print("Blast Off!")
print(n)

# While Break statement
n = 5
while n > 1:
    print(n)
    n = n - 1
    if n == 2:
        break
print(n)

# While Continue statement
# continue statement doesnt include the first variable. It skips to the next
n = 9
while n > 1:
    n = n - 1
    if n == 3:
        continue
    print(n)
