# Boolean
Boolean is a datatype that represent one of these value: `True` or `False`.
## Variable Assignment
Example on how to assign boolean variable:
```python
x = True
y = False
```

To check datatype of a variable
```python
x = True
y = False
print(type(x))  # output: <class 'bool'>
print(type(y))  # output: <class 'bool'>
```

Some operation in python will returning boolean value, lets see at this example:
```python
x = 2 < 1
print(x)  # output: False
print(type(x))  # output: <class 'bool'>
```
We will discuss more of operation in python later in the next [module]().

## Function bool()

bool() is a function that allows you to evaluate any value, and give you True or False in return. You can use bool() to check whether the value of any data type is empty or not.

### Example  
You can try to run these statements: 

1. These statement(s) will return value True:
```python
print(bool("Hello World"))  # output: True
print(bool(123))  # output: True
print(bool(["car", "bike", "plane"]))  # output: True
  ```

2. These statement(s) will return value False:
```python
print(bool(False)) # output: False
print(bool(None))  # output: False  
print(bool(0))  # output: False
print(bool(""))  # output: False
print(bool(()))  # output: False
print(bool([]))  # output: False
print(bool({}))  # output: False
```
