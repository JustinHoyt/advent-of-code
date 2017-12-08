from typing import Dict, Tuple, List
from math import ceil, sqrt
# input = 347991
input = 59

def sum_surrounding_cells(x, y, my_map):
    sum = 0
    for offset_x in range(-1, 2):
        for offset_y in range(-1, 2):
            if (x + offset_x, y + offset_y) in my_map:
                sum += my_map[(x + offset_x, y + offset_y)]
    return sum

current_value = 1
x = 0
y = 0

steps_right = 1
steps_up = 1
steps_left = 2
steps_down = 2
my_map = {(0,0): 1}

while(input >= current_value):
    # move right
    for _ in range(steps_right):
        if input >= current_value:
            x += 1
            current_value = sum_surrounding_cells(x, y, my_map)
            my_map[(x,y)] = current_value

    # move up
    for _ in range(steps_up):
        if input >= current_value:
            y -= 1
            current_value = sum_surrounding_cells(x, y, my_map)
            my_map[(x,y)] = current_value

    # move left
    for _ in range(steps_left):
        if input >= current_value:
            x -= 1
            current_value = sum_surrounding_cells(x, y, my_map)
            my_map[(x,y)] = current_value

    # move down
    for _ in range(steps_down):
        if input >= current_value:
            y += 1
            current_value = sum_surrounding_cells(x, y, my_map)
            my_map[(x,y)] = current_value

print(current_value)
