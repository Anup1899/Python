list_data = ["Roger", 1, True, 2.5]

print("Roger" in list_data) # True
print("x" in list_data) # False

print(list_data[0]) # Roger 
print(list_data[-1]) # 2.5

list_data[2] = "Anup" # Change the value of the list
print(list_data) # ['Roger', 1, 'Anup', 2.5]

print(list_data[0:2]) # Slicing:-- ["Roger", 1]
print(list_data[:3]) # Slicing:-- ["Roger", 1, True]

print(len(list_data)) # 4

list_data.append(True) # Add the value at the end of the list
print(list_data) # ['Roger', 1, 'Anup', 2.5, True]

# Combining two lists together
list_data.extend([1,2,3]) # Add the values at the end of the list
list_data += ["YXA", 34, False] # Add the values at the end of the list
print(list_data) # ['Roger', 1, 'Anup', 2.5, True, 1, 2, 3, 'YXA', 34, False]

list_data.remove(1) #IMPORTANT:-- Remove the fist occurrence of the value from the list
print(list_data) # ['Roger', 'Anup', 2.5, True, 1, 2, 3, 'YXA', 34, False]

list_data.pop() # False:-- Remove and Returnthe last value from the list
print(list_data) # ['Roger', 'Anup', 2.5, True, 1, 2, 3, 'YXA', 34]

list_data.insert(0, "Test") #Important:-- Insert the value at the specified index --> And Moves other items by one index
print(list_data) # ['Test', 'Roger', 'Anup', 2.5, True, 1, 2, 3, 'YXA', 34]

print("------------------------------------------------------------------------")

items = ["phone", "laptop", "tablet", "Bulb", "motor", "Engin", "bike", "ZX10R"]
print(items)

# Sort method changes the original list
# To copy the list in order variable in order to preserve the original list
items2 = items[:]

# Sorting changes the original list
# items.sort() # Sort the list in alphabetical order
# IMPORTANT:-- String Starting with upper case letter with get sort first in alphabetical order. Then the string with lower case will sort in alphabetical order.
items.sort() 
# ['Bulb', 'Engin', 'ZX10R', 'bike', 'laptop', 'motor', 'phone', 'tablet']

# Sort the list in alphabetical order irrespective of upper or lower case
# items.sort(key=str.lower)
print(items)

# List is prserved
print(items2)

# IMPORTANT:-- There is a way where list can be sorted without changing the original list
items3 = sorted(items, key=str.lower)
# items3 = sorted(items)
print(items3)
print(items2)



print("----------------------------------------- Tuplessssss -------------------------------")   

# Tuples imputable groups of values
# Tuples are immutable
# Tuples are faster than lists
# Tuples are used to store multiple values in a single variable

tuple_data = ("Anup", 1, 2.5, True)
print(tuple_data)
print(tuple_data[0])

print(tuple_data.index(True)) # Returns the index of the value --> 2
# The above should return index as 3
# But it return 1, bacause True is treated as 1 in python and first occurrence of 1 is at index 1

print("Anup" in tuple_data)

new_tuple = tuple_data + ("YXA", 34, False)
print(new_tuple)


print("----------------------------------------- Dictionaries -------------------------------")
# Dict is Key Value Pairs

dict_data = {
	"name": "Anup",
	"age": 25,
	"is_adult": True
}
print(dict_data)
print(dict_data["name"]) # Anup
dict_data["age"] = 13
print(dict_data)
print(dict_data.get("age"), dict_data["age"])
dict_data.pop("age") # Remove the key value pair
# print(dict_data.popitem()) # Remove the last key value pair
print(dict_data)
print("name" in dict_data)
print(dict_data.keys()) # Returns the keys of the dictionary
print(dict_data.values()) # Returns the keys of the dictionary
print(dict_data.items()) # Returns the Items of key and value as list of List

dict_data["state"] = "Maharashtra"
print(dict_data)


del dict_data["is_adult"]
print(dict_data)

#Create a new dictionary using copy()
dict_data2 = dict_data.copy()
dict_data2["name"] = "YXA"
print(dict_data,dict_data2)


# Nested funciton and Closure

def count():
	count = 0

	def increment():
		nonlocal count # This is used to access the variable from outer scope in inner scope
		count = count + 1
		print(count)

	return increment

increment = count()
increment() # 1
increment()	# 2
increment()	# 3
