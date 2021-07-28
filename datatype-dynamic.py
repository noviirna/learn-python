# This is an example on how to assign variable with example value of related datatype
def print_newline():
  print("")

## 1. List
print("1. List")
exampleList = ["car", "bike", "plane"]

# 1.1. if printed, will be printed in order
print("1.1. ", exampleList)
# output: ["car", "bike", "plane"]

# 1.2. first item has index 0, exampleList have "car" as first data at index 0
print("1.2. ",exampleList[0]) 
# output: "car"

# 1.3. mutable, can perform operation add, delete, remove, update to items in list
exampleList.append("motorcycle");
print("1.3. ",exampleList) 
# output: ["car", "bike", "plane", "motorcycle"]


print_newline()


## 2. Tuple
print("2. Tuple")
exampleTuple = ("bike", "plane", "car")

# 2.1. if printed, will be printed in order
print("2.1. ", exampleTuple) # output: ("bike", "plane", "car")

# 2.2. first item has index 0
print("2.2 ", exampleTuple[0]) # output: "bike"

# 2.3. immutable
# if tried to change item inside tuple the console will show error:
# TypeError: 'tuple' object does not support item assignment

print_newline()

## 3. Set
print("3. Set")
exampleSet = {"car", "plane", "bike"}

# 3.1. if printed, will be printed in unordered manner
print("3.1. ", exampleSet)

# 3.2. do not have index because it is unordered, if tried to get index, the console will show error:
# TypeError: 'set' object is not subscriptable

# 3.3. immutable 
# # if tried to change item inside set the console will show error:
# TypeError: 'set' object does not support item assignment

print_newline()


## 4. Dictionary
print("4. Dictionary")
exampleDictionary = {
  "transportation" : "car",
  "fuel": "gas"
}

# 4.1. if printed, will be printed in ordered manner
print("4.1. ", exampleDictionary)
# output: {'transportation': 'car', 'fuel': 'gas'}

# 4.2. to access value, you will need to call the key
print("4.2.1 ", exampleDictionary.get("fuel"))
# output: "gas"
print("4.2.2 ", exampleDictionary["fuel"])
# output: "gas"

# 3.3. mutable 
exampleDictionary.update({"fuel": "electricity"})
print("4.3.1. ", exampleDictionary)
# output: {'transportation': 'car', 'fuel': 'electricity'}

exampleDictionary["transportation"] = "hybrid car"
print("4.3.2. ", exampleDictionary)
# output: {'transportation': 'hybrid car', 'fuel': 'electricity'}
