# Data Type
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