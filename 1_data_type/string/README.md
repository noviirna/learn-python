# String
String is a datatype that represent text.

## Variable Assignment
To assign single line string, value have to be  surrounded by either one character of single quotation marks (`'`) or double quotation marks `(")`.
```python
x = "Hello World"
y = "123"
a = '1'
b = 'Hello World'
```

To assign multiple line string, value have to be surrounded by either three character of single quotation marks (`'`) or double quotation marks `(")`.
```python
word = """Lorem ipsum dolor sit amet,
 consectetur adipiscing elit,
  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

word2 = '''Lorem ipsum dolor sit amet,
 consectetur adipiscing elit,
  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'''
```

To check datatype of a variable
```python
x = "Hello World"
word = """Lorem ipsum dolor sit amet,
 consectetur adipiscing elit,
  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

print(type(x))  # output: <class 'str'>
print(type(word))  # output: <class 'str'>
```

We will discuss more of string manipulation in python later in the next [module](https://github.com/noviirna/learn-python/tree/master/4_string_operation).
