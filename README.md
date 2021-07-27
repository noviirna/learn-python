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
1. Static Data Type
   |Type|Description|Example|
   |----|----|----|
   |`String`|represent text|'hello', '123', 'Hello123!*#', "hello", "123", 'Hello123!*#' |
   |`Integer`|represent integers|-123, -1, 0, 1, 123|
   |`Float`|represent decimals|-1.33, 0.07, 9.54|
   |`Boolean`|represent true / false|True, False|
   |`Complex`|represent imaginary value|1j, 2-6j|
     
   #### Difference between String and Integer  
   You need remember that if you put numeric value in `'`, it will be stored as String variable. It will be handled differently  in mathematical operation. Take a look at the example below
   ```
   # addition of numeric value with data type integer
   print(5 + 5) # output 10

   # addition of numeric value with data type string
   print('5' + '5') # output 55
   ```  
