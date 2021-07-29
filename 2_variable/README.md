# Variable 
- variable is some kind of storage to store data value
- to store any value to variable is to use *assignment* operator (**=**)
- a variable that already had data value, can be assigned with new value, but the old value will be replaced with latest assigned value
- a variable that already had data value, can be assigned with new value with different data type
- assignment of variable can be done while doing mathematic operation
   |Operator Assignment|Example|Description|
   |---|---|---|
   |+=|x+=2| x = x + 2|
   |-=|x-=2| x = x - 2|
   |*=|x*=2| x = x * 2|
   |/=|x/=2| x = x / 2|
   |%=|x%=2| x = x % 2|
   |**=|x**=2| x = x ** 2|
   |//=|x//=2| x = x // 2|


## How to assign value to variable 
There are several ways to store value into variable :
   |Type|[Example](https://github.com/noviirna/learn-python/blob/master/2_variable/variable-assignment.py)|
   |----|----|
   |many value to many variable|var1, var2, var3 = "car", "plane", "bike"|
   |one value to many variable|x = y = z = "car"|
   |one value to one variable|str = "Hello World"|
   |unpacking value from collection|see: [(example)](https://github.com/noviirna/learn-python/blob/master/2_variable/variable-assignment.py)|

## Rules for naming variable
- variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- variable name cannot start with numeric character (must start with a letter or the underscore character)
- variable name is case sensitive

## Scope of a variable
There are 2 kinds of variable based on scope, local variable and global variable.
1. Global variable  
   Global variable is a variable that is created outside of a function or a variable that is created inside of a function with `global` keyword before declaring variable name.  
   Global variable can be used by everyone, both inside of functions and outside. Global variable also can be created inside of a function (see: [example]())
2. Local variable  
   Local variable is a variable that is created inside of a function, can be used only inside of that function where the variable is declared.