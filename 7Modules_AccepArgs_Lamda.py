# import test
from test import hello # Allows specific functions from the file
from lib.test import name

import math

# test.hello("Anup")
hello("Anup")
name()

print(math.pi)
print(math.sqrt(16))

print("------------------------ Accepting Arguments -------------------------------")
# import sys
# import argparse

# parser = argparse.ArgumentParser(
# 	description="This is used for testing"
# )

# # parser.add_argument("-c", "--color", metavar='color', required=True, help="the color to search")
# parser.add_argument("-c", "--color", metavar='color', required=True, choices={'red', 'yellow'},help="the color to search")  # Argument with choices

# args = parser.parse_args()

# print(args.color)

# Run the code by -------------> python 7Modules.py -c red


print("------------------------Lamda Funciton-------------------------")
# Anonymous function
# It has to return a expression not the statement
multiply_by_2 = lambda num: num *2
print(multiply_by_2(5))


# Map, Filter and Reduce
list_data = [1,2,3,4,5]

res_map = map(lambda num: num *2, list_data)
print(list(res_map))

res_filter = filter(lambda num: num % 2 == 0, list_data)
print(list(res_filter))

from functools import reduce
res_reduce = reduce(lambda acc, num: acc + num, list_data)
print(res_reduce)