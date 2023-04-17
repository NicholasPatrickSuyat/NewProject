# For range loop
for x in range(0, 10, 1):        # start(0), stop(10), step increment/decrement(1)
    print(x)
print("For loop has Finished")

# For loop without range, using string
for x in "string":
    print(x)

# For loop using break in string, it stops when it reach "i"
for x in "string":
    if x == "i":
        break
    print(x)

# For loop using continue in string, it skips the letter "i"
for x in "string":
    if x == "i":
        continue
    print(x)
