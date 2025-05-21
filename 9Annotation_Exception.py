print("---------------------------Annotation-----------------------------")
# Used to check for type Errors

def increment(n : int) -> int:
	return n

increment("ssd1")

print("---------------------------Exception-----------------------------")
try:
	print("Inside Try")
	raise Exception("D")
except Exception as error:
	print("Error", error)	
except:
	print("Erro")
finally:
	print("Finally")

