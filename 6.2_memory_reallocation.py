from typing import Set, Dict, Tuple, List

# inputs = "0 2 7 0"
inputs = "11 11 13 7 0 15 5 5 4 4 1 1 7 1 15 11"
combination_locations = {}  # type: Dict[str, int]
count = 0
while inputs not in combination_locations:
    # combination_locations.add(inputs)
    combination_locations[inputs] = count
    int_inputs = [int(x) for x in inputs.split(" ")]  # type: List[int]
    high_index = int_inputs.index(max(int_inputs))
    high_value = int_inputs[high_index]
    int_inputs[high_index] = 0

    for i in range(1, high_value + 1):
        next_index = (high_index + i) % (len(int_inputs))
        int_inputs[next_index] += 1

    count += 1
    inputs = ' '.join([str(x) for x in int_inputs])

print(count - combination_locations[inputs])
