print("------------------------ Recursion -------------------------------")

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)

print(factorial(5))


print("------------------------ Decorator -------------------------------")
# Function that takes function as an argument and return another function 
# When ever the function is called the decorator is attached to it

def logtime(func):
	print("Decorator Before")
	def wrapper():
		print("Inside Wrapper")
	func()
	return wrapper

@logtime
def hello():
	print("Hello World")

hello()

print("------------------------ Docstrings -------------------------------")
def	increment(n):
	"""Doc String
		Multiple line
	"""
	"""Increment"""
	return n+1

print(help(increment(2)))