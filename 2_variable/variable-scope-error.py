"""
if you call a local variable from outside of it scope,
on runtime it will return error like this

NameError: name '${your variable name}' is not defined

lets try to run this .py files to prove it
"""


def my_function2():
  a = "\"inside\""
  print("Output from local variable, called inside the scope: " + z)

print("Output from local variable, called outside the scope: " + a)
