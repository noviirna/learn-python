# Integer
Integer is a datatype that represent whole numbers (can be zero, positive or negative) without a fractional part and having unlimited precision.  
If value of a variable have fractional part, then the data type will be [Float]() instead of Integer.  
Integer also can be represented by other number system, which includes: binary, octal, and hexadecimal values.

## Other numeral system with type Integer
- **Binary** numbers represented by any value that begin with `0b` or `0B` then followed with eight digits in the combination of 0 and 1
- **Octal** numbers can be represented by adding `0o` or `0O` as prefix before the octal value
- **Hexadecimal** numbers represented by adding `0x` or `0X` as prefix before the hexadecimal value

## Variable Assignment
Example on how to assign boolean variable:
```python
x = 0 # whole number, zero
y = 1 # whole number, positive
z = -1 # whole number negative

b = 0b00001010 # binary of value 10
o = 0o12 # octal binary of value 100
h = 0x4B # hexadecimal of value 75
```

When checked the data type, any variable with type integer will return `<class 'int'>`
```python
print(type(x))  # output: <class 'int'>
```

## Operation
|Symbol|Operator|Description|Example|Result|Priority|
|---|---|---|---|---|---|
|`+`|Addition|Adds operands on either side of the operator|`1+1`|2|3|
|`-`|Substraction|Subtracts the right-hand operand from the left-hand operand|`1-1`|0|3|
|`*`|Multiplication|Multiplies values on either side of the operator|`8*9`|72|2|
|`/`|Division|Divides the left-hand operand by the right-hand operand|`21/7`|3|2|
|`//`|Floor Division|The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity)|`10//4`|2|2|
|`%`|Modulus|Returns the remainder of the division of the left-hand operand by right-hand operand.|`20%6`|2|2|
|`**`|Exponent|Calculates the value of the left-operand raised to the right-operand.|`3**2`|9|1|

**NOTES**  
Operator that have lowest value in column *Priority* will be prioritized to be executed first in mathematical expression.  
On column *Priority* `1` represent highest priority, `3` represent lowest priority.  If given expression below :  
```python
2 ** 3 * 3 - 12 / 2 + 4
```
will be executed like this :
```python
( (2 ** 3) * 3) - ( 12/2 ) + 4
```

