# This is an example on how to assign variable with example value of related datatype

## Integer, represent integers
integerVar = 2021
integerVar2 = -2021

## Float, represent decimals
floatVar = 1.21
floatVar2 = -1.21

## String, represent text
stringVar = '2021'
stringVar2 = 'Python123'

## Boolean, represent true / false
booleanVar = True
booleanVar2 = False

## Complex, represent imaginary value
complexVar = 1 + 1j
complexVar2 = 1j


# === not a learning materials, variables only for description in terminal ===

prefix='variable '
newLine = '\n'
aggregator1 = " with value "
aggregator2 = " have datatype "

print('Static Data Type Example', newLine, "= " * 30)
print(prefix, f'{floatVar=}'.split('=')[0],aggregator1, f'{floatVar=}'.split('=')[1], aggregator2, type(floatVar))
print(prefix, f'{floatVar2=}'.split('=')[0],aggregator1, f'{floatVar2=}'.split('=')[1], aggregator2, type(floatVar2), newLine)
print(prefix, f'{integerVar=}'.split('=')[0],aggregator1, f'{integerVar=}'.split('=')[1], aggregator2, type(integerVar))
print(prefix, f'{integerVar2=}'.split('=')[0],aggregator1, f'{integerVar2=}'.split('=')[1], aggregator2, type(integerVar2), newLine)
print(prefix, f'{stringVar=}'.split('=')[0],aggregator1, f'{stringVar=}'.split('=')[1], aggregator2, type(stringVar))
print(prefix, f'{stringVar2=}'.split('=')[0],aggregator1, f'{stringVar2=}'.split('=')[1], aggregator2, type(stringVar2), newLine)
print(prefix, f'{booleanVar=}'.split('=')[0],aggregator1, f'{booleanVar=}'.split('=')[1], aggregator2, type(booleanVar))
print(prefix, f'{booleanVar2=}'.split('=')[0],aggregator1, f'{booleanVar2=}'.split('=')[1], aggregator2, type(booleanVar2), newLine)
print(prefix, f'{complexVar=}'.split('=')[0],aggregator1, f'{complexVar=}'.split('=')[1], aggregator2, type(complexVar))
print(prefix, f'{complexVar2=}'.split('=')[0],aggregator1, f'{complexVar2=}'.split('=')[1], aggregator2, type(complexVar2), newLine)
