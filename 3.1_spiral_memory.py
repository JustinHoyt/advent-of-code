from typing import Dict, Tuple, List
from math import ceil, sqrt
# input = 347991
input = 17

input_root = ceil(sqrt(input))
starting_coordinate = input_root + 1 if input_root % 2 == 0 else input_root
starting_x = int((starting_coordinate - 1) / 2)
starting_y = int((starting_coordinate - 1) / 2)

current_value = starting_coordinate * starting_coordinate
x = starting_x
y = starting_y
isFound = False

# move left
for i in range(x, -x, -1):
    print(current_value)
    if current_value == input:
        isFound = True
        break
    x -= 1
    current_value -= 1

# move up
if isFound == False:
    for i in range(y, -y, -1):
        print(current_value)
        if current_value == input:
            isFound = True
            break
        y -= 1
        current_value -= 1

# move right
# move down
print("[" + str(x) + ", " + str(y) + "]")
