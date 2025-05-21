# Sets
# Sets are like tuples though they are mutable and are unordered
# Sets are used to store unique values

print("------------------------- Sets -------------------------------")

names1 = {"Anup", "YXA", "Shub"} # Creating a set
names2 = {"Anup", "SDDEW", "Shub"}
names3 = {"Anup", "Shub"}

instersect = names1 & names2 # Provide the common values between two sets
print(instersect) # {'Shub', 'Anup'}

union = names1 | names2 # Provide the union of two sets
print(union) # {'YXA', 'SDDEW', 'Shub', 'Anup'}

difference = names1 - names2 # Remove the common value between two sets from the first set and returns remaining values
print(difference) # {'YXA'}

symmetric_difference = names1 ^ names2 # Provide the symmetric difference between two sets
print(symmetric_difference) # {'YXA', 'SDDEW'}

super_set = names1 > names3 # Check if the first set has all the values available in second set
print(super_set) # True

set_to_list = list(names1) # Convert the set to list
print(set_to_list) # ['YXA', 'Shub', 'Anup']

names1.add("Aniket") # Add the value to the set
print(names1)

names1.remove("Aniket") # Remove the value from the set
print(names1)


print("------------------------- Function -------------------------------")

def hello():
	print("Hello")
hello()

def hello(name = "my friend"): # Function with default parameter
	print("Hello " + name) 
hello("Anup")

 
print("------------------------- Objects -------------------------------")

# Everything in python is an object
# All the datatypes in python are objects
# Everything has property that can be access using dot operator is Object

age = 30
print(age.real)
print(age.imag)