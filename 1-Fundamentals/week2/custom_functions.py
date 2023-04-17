# Creating your Own Functions Parameter
def myFn():     # Calling a function without a parameter
    print("You have called my function")


def add(x, y):
    z = x + y
    print(z)


myFn()      # Function to call. Empty argumentlist because the function has no Parameter
add(2, 3)   # Function to call. It has two parameters(x, y) so declare a parameter to call
add(3, 4)   # Function to call. same as above but new functions to call.

a = 4
b = 5
add(a, b)   # Functions to call. Can also work with variables

# def Function using input function
def func(name):
    print("hello", name)


x = (input("What is your name"))

func(x)



# Lambda Function


g = lambda num1, num2: num1 * num2

x = g(2, 5)
print(x)


# Lambda with def function

def math_function(x,y):
   return lambda a,b,c: (b/c*x) + a*x + y

m = math_function(5,1) # the (5,1) comes from the def math_function(x)

print(m(5,2,6)) # The (5,2,6) comes from lambda a,b,c 