"""
Now we will see how global and local variable in python is declared & accessed
"""
x = "[this is a global variable, declared outside of function]"

# Example method
def my_function():
  print("Global variable can be accessed while inside of a function: " + x)
  global y
  y = "[this is a global variable, declared inside of function]"

# To prove that y is global variable, lets just run these 2 lines of code
my_function()
print("Variable y is a global variable despite it is declared inside a function with 'global' syntax : " + y)


"""
If you create a variable with the same name inside a function, and do not declare it with 'global' syntax before variable name
the variable will be local, and can only be used inside the function
And the global variable with the same name will remain as it was, global and with the original value.
take a look of this example
"""

z = "\"blue\""

def my_function2():
  z = "\"red\""
  print("Output from local variable: " + z)

# To prove that z is global variable, lets just see the output of these 2 lines of code
my_function2()
print("Output from global variable: " + z)