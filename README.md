# Learn basic python
This is a collection of `.py` files to learn python language step by step with some learning materials

---
## Practices
`Notes: (author is using ubuntu 18.04, for windows n mac OS you might have to see outside references for setting the environment)`
### Minimal requirement
- python 3.8 is installed 
### How to run
1. open folder which you put `.py` files in terminal
2. run this command
```
python3.8 <file-name-to-run-with-.py-extensions>

```
---
## Learning materials

### Data Type
In general, python have 2 data types *static* and *dynamic*
1. Static Data Type [(example)](https://github.com/noviirna/learn-python/blob/master/datatype-static.py)
   |Type|Description|Example|
   |----|----|----|
   |`String`|represent text|'hello', '123', 'Hello123!*#', "hello", "123", 'Hello123!*#' |
   |`Integer`|represent integers|-123, -1, 0, 1, 123|
   |`Float`|represent decimals|-1.33, 0.07, 9.54|
   |`Boolean`|represent true / false|True, False|
   |`Complex`|represent imaginary value|1j, 2-6j|
     
   #### Difference between String and Integer  
   You need remember that if you put numeric value in `'` or `"`, it will be stored as String variable. It will be handled differently  in operation. Take a look at the example below
   ```
   # addition of numeric value with data type integer
   print(5 + 5) # output 10

   # addition of numeric value with data type string
   print('5' + '5') # output 55
   ```  
2. Dynamic Data Type [(example)](https://github.com/noviirna/learn-python/blob/master/datatype-dynamic.py)
   |Type|Description|Example|
   |----|----|----|
   |`List`|represent collection of values that is ordered and indexed, the value can have different data type and can have duplicate value|[1, "1", 'Hello', False]|
   |`Tuple`|same as `List`, but immutable|(1, "1", 'Hello', False)|
   |`Set`|represent collection of values that is unordered and unindexed, immutable, the value can have different data type and does not allow duplicate values|{"hello","world"}|
   |`Dictionary`|represent collection of values that is ordered by key (key-value based), changeable, the value can have different data type and does not allow duplicates (for key name)|{"foo":"bar"}|

### Variable 
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

#### How to assign value to variable 
There are several ways to store value into variable :
   |Type|[Example](https://github.com/noviirna/learn-python/blob/master/variable-assignment.py)|
   |----|----|
   |many value to many variable|var1, var2, var3 = "car", "plane", "bike"|
   |one value to many variable|x = y = z = "car"|
   |one value to one variable|str = "Hello World"|
   |unpacking value from collection|see: [(example)](https://github.com/noviirna/learn-python/blob/master/variable-assignment.py)|

#### Rules for naming variable
- variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- variable name cannot start with numeric character (must start with a letter or the underscore character)
- variable name is case sensitive

#### Scope of a variable
There are 2 kinds of variable based on scope, local variable and global variable.
1. Global variable  
   Global variable is a variable that is created outside of a function or a variable that is created inside of a function with `global` keyword before declaring variable name.  
   Global variable can be used by everyone, both inside of functions and outside. Global variable also can be created inside of a function (see: [example]())
2. Local variable
   Local variable is a variable that is created inside of a function, can be used only inside of that function where the variable is declared.