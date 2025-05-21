print("---------------------------List Compression-----------------------------")

numbers = [1, 2, 3, 4]

numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)

print("---------------------------Polymorphism-----------------------------")
# Polymorphism is the ability of an object to take on many forms

class Animal:	
	def walk(self):
		print("Walking....")

class Dog(Animal):
	def walk(self):
		print("Dog is Walking....")

class Cat(Animal):
	def walk(self):
		print("Cat is Walking....")

dog = Dog()
cat = Cat()

dog.walk()
cat.walk()


print("---------------------------Operator-----------------------------")
