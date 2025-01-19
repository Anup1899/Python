# Complex Number in Python
#Complex number is a number that can be expressed in the form a + bj, where a and b are real numbers and j is the imaginary number i.

num = 2 + 4j
print(num.real, num.imag)

num2 = complex(2,3)
print(num2.real, num2.imag)

print(abs(-5.5))
print(round(5.33, 1))

# enum are generally used to create constant in python
from enum import Enum

print("ENUMS in Python")
class Status(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(Status(0))
print(Status.INACTIVE.value)
print(list(Status))