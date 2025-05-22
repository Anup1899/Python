# Data types
# Number, String, Boolean, None, Float


# Reserved words -- These words can not be used as variable name
# Python is Case-Sensetive

# Logical Operator --> not, and, or

# Type Conversion
    # Conversion -- Automatic conversion
    # Casting Conversion -- Manual conversion

a = 2
b = 4.24
print(a+b) # Automatic conversion -- Intger a is converted to float automatically

c = "2"
d = 23
# print(c + d) ---> ERROR 
# String concatination is only possible with string data type (not int)

# Type casting -- Casting Conversion
print(int(c) + d) 


# Taking Inputs in Python
# input() --> Takes inputs from the users
            # Always returs a string
                # We always need to type cast the value to get the proper data type


# String : Start ------------------------------------------------------------------------------------------
str1 = "This is a string. \n I need to add this statement to the new line" 
print(str1)
print(len(str1))
print(str1[8]) # Indexing :- Item assignment is allowed in indexing str[8] = "r" --> Not Allowed

# Slicing
print(str1[1:4]) 
# print(str1[:4]) 
# print(str1[56:]) 
print(str1[-5 : -1])
print(str1.endswith("line"))
print(str1.replace("add", "move"), "\n",str1)  # Does not change the original string
# find() --> Returns the first index of the occurrence
# count() --> Returns the count of word/letter in the string

# String : End ------------------------------------------------------------------------------------------


# Conditional Statements : Start ------------------------------------------------------------------------
age = 1
if(age > 18 ):
    print("You can vote")
elif(age < 0):
    print("Invalid age")
else:
    print("You can vote")
# Conditional Statements : End   ------------------------------------------------------------------------


# List : Start   ------------------------------------------------------------------------
# List are similar to string
    # List are mutable while string are not mutable
print("---------------------------------------List---------------------------------------")
myList = [1,2,3,4,5]
myList.append(6)
myList.sort(reverse= True) # Sort return None. Just overwrites the original List
myList.reverse()
myList.insert(3, "Three")
print(myList)
print(len(myList))
myList.remove("Three")
myList.pop() # Removes the last index
myList.pop(4) # Remove the element with index
print(myList)
# All the above methods return None. Overwrite the original list
# All the above methods return None. Overwrite the original list

# List : End   ------------------------------------------------------------------------

# Tuple : Start   ------------------------------------------------------------------------
# Immutable 
print("---------------------------------------Tuple---------------------------------------")
tup = (1,2,3,4,5,4)
print(tup.count(4))
print(tup[0])
tupp = () # Empty Tupple
tupple = (1,) # IMPORTANT ---> To define a single item in a tuple, it is important to define it with comma ",". Otherwise python will compute it a simple number 
# tupple = ("hello",) 
# tupple = () 
print(type(tupple))
tupple = (1) 
print(type(tupple))
# Tuple : End   ------------------------------------------------------------------------

# Dictonary : Start   ------------------------------------------------------------------------
print("---------------------------------------Dictionary---------------------------------------")
myDict ={
    "fname" : "Anup",
    "lname" : "Alone"
}
print(myDict.keys(), type(myDict.keys()), list(myDict.keys())) # Type Casting
print(myDict.values(), list(myDict.values()))
print(myDict.items(), list(myDict.items())) # Returns the list of Tuples
myDict.update({"gender":  "Male"})

# print(myDict["age"]) # Returns Error
print(myDict.get("age")) # Returns None 
print(myDict)
# Dictonary : End   ------------------------------------------------------------------------

# Sets : Start   ------------------------------------------------------------------------
print("---------------------------------------Set---------------------------------------")
# Immutable Elements, Stores Unique Value
# Set store the HashValue for an element --> Like number or string are converted into HashValue which is constant. But list can't because it is mutable for every change in the list the hash value will be changing
# But tuple can be a part of the set because it is immutable, it can have constant has value  
collection = {1,2,3, "world", "hello", "world", 2, 2, 2}
collection.add(5)
collection.remove(1)
collection.pop() # Removes the last element

second_collection = {'hi', "Anup", 34, 3,4 ,2}

unionSet =  collection.union(second_collection)
intersectSet = collection.intersection(second_collection)
# collection.remove(7) # Error

print(collection, f"length :- {len(collection)}")
print("Union", unionSet)
print("InterSect", intersectSet)

mySet = set({int(9), float(9.0)})
mySet = set({int(9), float(9.0)})
mySet.add(("int", 9))
mySet.add(("float", 9.0))
print(mySet)
# Sets : End   ------------------------------------------------------------------------


# Loop : Start   ------------------------------------------------------------------------
print("---------------------------------------Loop---------------------------------------")
print("---While Loop----")
count = 0
while(count <= 5):
    print(count)
    count += 1

squareList = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i=0
while(i<len(squareList)):
    print(squareList[i])
    i += 1

squareTuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
j= len(squareTuple) - 1
# print(len(squareTuple), squareTuple[1])
while(j >= 0):
    print(squareTuple[j])
    j -= 1

print("---For Loop----")
for square in squareTuple :
    print(square)

print("---Range----")
for ele in range(5):
    print(ele)

print("Range with starting point")
for ele in range(1,5):
    print(ele)

print("Range with step size")
for ele in range(1, 10, 2):
    print(ele)
# Loop : End   ------------------------------------------------------------------------


# Function : Start   ------------------------------------------------------------------------
print("---------------------------------------Function---------------------------------------")
# First non default values then default values



# File Input/Output : Start   ------------------------------------------------------------------------
print("---------------------------------------File Input/Output---------------------------------------")
# Text File :- .txt, .docx, .log, etc,
# Binary File :- .mp4, .mov, .png, .jpeg, etc,
# IMPORTANT :- 
    # Concept of Stream/ Curor
    # Everytime the file is read the cursor is pointed at the beginning end remains at the end of the end.
    # While appending to the file the stream/cursor is appened at the end of the file 
print("Reading a file")
file =  open("demo.txt", "r")
data = file.read()
print(data)
file.close()

print("Writing a file") # Truncate the data of the file
file = open("demo.txt", "w")
data = file.write("This is overwite the data in the file.")
file.close()

print("Append the data")
file = open("demo.txt", "a")
data = file.write("\nThis statement has appended")
file.close()

# r+ -> read and overwrite the data in the file. Stream starts where it was already before
# w+ -> read and overwrite the data in the file. Truncate the data of the file
# a+ -> read and append the data in the file. Stream starts from the end of the file

print("--------------------------------With Statement File Input/Output---------------------------------------")
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
    # No need to close the file while using with statement


# For deleting the file  
# import os 
# os.remove("demo.txt")

# File Input/Output : End   ------------------------------------------------------------------------








