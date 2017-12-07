from typing import Dict, Tuple, List
from math import ceil, sqrt
# input = 347991
input = 24

input_root = ceil(sqrt(input))
starting_coordinate = input_root + 1 if input_root % 2 == 0 else input_root
starting_x = int((starting_coordinate - 1) / 2)
starting_y = int((starting_coordinate - 1) / 2)

current_value = starting_coordinate * starting_coordinate
x = starting_x
y = starting_y
for i in range(starting_x, -1 * (starting_x + 1), -1):
    print(current_value)
    if current_value == input:
        break
    x -= 1
    current_value -= 1

print("[" + str(x) + ", " + str(y) + "]")
