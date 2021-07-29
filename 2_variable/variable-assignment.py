# This is an example on how to assign variable


# 1. many value to many variable
var1, var2, var3 = "car", "plane", "bike"

print("Example 1: ", var1, var2, var3) # output: car plane bike

"""
var1 will have value "car"
var2 will have value "plane"
and var3 will have value "bike"
""" 


# 2. one value to many variable
x = y = z = "motorcycle"

print("Example 2: ", x,y,z) # output: motorcycle motorcycle motorcycle

"""
x, y, and z all will have value "motorcycle"
"""


# 3. one value to one variable
str = "Hello World"

print("Example 3: ", str) # output: hello world


# 4. unpacking value from a collection
transportation = ["bike", "ship", "bus"]
x, y, z = transportation

print("Example 4.1: ", transportation) # output: ['bike', 'ship', 'bus']
print("Example 4.2: ", x,y,z) # output: bike, ship, bus

"""
x will have value "bike"
y will have value "ship"
z will have value "bus"
"""