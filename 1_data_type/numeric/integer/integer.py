x = 0 # whole number, zero
y = 1 # whole number, positive
z = -1 # whole number negative

b = 0b00001010 # binary of value 10
o = 0o12 # octal binary of value 100
h = 0x4B # hexadecimal of value 75


"""
lets see, are above variables really an integer?
you can try it by changing myVar value to one of variable name above
"""
myVar = o

print(myVar)
print(type(myVar))  # output: <class 'int'>



"""
integers operation have priority by its operator, lets see practical example of this
If you check whether ops_1 equals ops_2 it will return value True
"""
ops_1 = 2 ** 3 * 3 - 12 / 2 + 4
ops_2 = ( (2 ** 3) * 3) - ( 12/2 ) + 4


print(ops_1 == ops_2) # output: True
