#Loop
print("------------------------ Loop -------------------------------")
items = [1,2,3,4]
for item in items:
	print(item) # 1 2 3 4

for item in range(15):
	print(item) # 1 2 3 4 5 6 7 8 9 10 11 12 13 14

# To get the index and item
for index, item in enumerate(items):
	print(index, item) 

names = ["Anup", "YXA", "Shub", "An"]
for index, name in enumerate(names):
	print(index, name)


# Significance of break and continue keywork
# continue :-- Skips the loop and keep running for the next iteration
# break :-- Breaks the loop

for items in range(10):
	if items == 5 or items == 6:
		continue 
	print(items) # 1 2 3 4 7 8 9 10 Skipped 5 and 6

for item in range(10):
	if item == 5:
		break
	print(item) # 1 2 3 4


print("------------------------ Class -------------------------------")
# Class is used to instanciate an Object
# While defining a method inside the class "self" is the fist parameter that should be used as a parameter. SELF refer to the instance of the class

# constructor in class is defined using "__init__" 
	# constructor is used to initialize the instance of the class

class Animal:
	def walk(self):
		print("Walking....")

class Dog(Animal): # Inheritance of the Animal inside Dog --> Dog class has access to all the methods that are defined inside Animal Class
	#constructor 
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def bark(self):
			print("woof!")

	def details(self):
		print(f"Dog name is {self.name} and it is {self.age} years old")



roger = Dog("Roger", 5)
roger.bark()
roger.details()
roger.walk() # Through Inheritance of Animal class

print(type(roger))