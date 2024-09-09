# Data Type in Python

# String    
# Integer
# Float 
# Boolean
# List
# Tuple
# Set
# Dictionary


# Operators
#  1 + 1 = 2
#   1 - 1 = 0
#   2 * 2 = 4
#   1 / 1 = 1
#   2 ** 2 = 16
#   4 % 3 = 1
#   4 // 3 = 1
#  7 \\ 2 = 3 --> Provides Floor Value and Round it off the nearest integer


# Boolean Operator

# not
# and
# or

# or return the first truthy value if all are falsy return the last value
    # 0 or 1 return 1
    # False or 'hey' return 'hey'
    # 'hi' or 'hello' return 'hi'
    # [] or False return False ---> Both are falsy last value is returned
    # False or [] return []  ---> Both are falsy last value is returned


# and return the first falsy value if all are true return the last value
    # 0 and 1 return 0
    # False and 'hey' return False
    # 'hi' and 'hello' return 'hello' --> All are True then return the last value
    # [] and False return []
    # False and [] return False


# Bitwise Operators
    # & (and)
    # | (or)
    # ^ (xor)
    # ~ (not)
    # << (left shift)
    # >> (right shift)


# is 
    # It is need to compare two objects and return true if both the objects are the same object
# in
    # It is used to check if a sequence is present in the object

# Tirnary Operator in Python
    # true_value if condition else false_value

def is_adult(age):
    return True if age > 18 else False
print("Tirnary Operator in Python")
print(is_adult(19))
print(is_adult(12))

# String Methods in Python
# All String Methods do not alter the original strings
print("haRRy".lower())  # harry
print("haRRy potter".upper()) # Uppercase the whole string
print("haRRy potter".title()) # Capitalize the first letter of each word
print("haRRy".islower()) # Checks for all the letters to be in lower case
print(len("harry"))
