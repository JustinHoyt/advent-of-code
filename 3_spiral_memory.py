from typing import Dict, Tuple, List
from math import ceil, sqrt
# input = 347991
input = 5

input_root = ceil(sqrt(input))
matrix_size = input_root + 1 if input_root % 2 == 0 else input_root
origin_xy = ceil(matrix_size / 2)
matrix = [[0 for col in range(matrix_size)] for row in range(matrix_size)]

for i in range(input):
    pass
