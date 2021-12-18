import itertools
from collections import deque

input_file = open("input.txt")
input_values = [list(line.strip()) for line in input_file]

data = [list(map(int,i)) for i in input_values]

def find_neighbors(data, x, y):
    potential_neighbors = itertools.product(range(x-1, x+2), range(y-1, y+2))
    valid_neighbors = lambda x_val, y_val: 0 <= x_val < len(data) and 0 <= y_val < len(data[x]) and (x_val, y_val) != (x, y)
    neighbors = []
    for (x_val, y_val) in potential_neighbors:
        if valid_neighbors(x_val, y_val):
            neighbors.append((x_val, y_val))
    return neighbors


def find_values_greater_than_9(data):
    flash_list = []
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] > 9:
                flash_list.append((x, y))
    return flash_list


def complete_one_step(data):
    new_data = [list(map(lambda x:x+1, x)) for x in data]
    flash_list = find_values_greater_than_9(new_data)
    flash_queue = deque(flash_list)
    already_flashed = set(flash_list)

    while flash_queue:
        (x, y) = flash_queue.pop()
        neighbors = find_neighbors(data, x, y)
        for (x_val, y_val) in neighbors:
            new_data[x_val][y_val] += 1 
            neighbor = new_data[x_val][y_val]
            if neighbor > 9 and (x_val, y_val) not in already_flashed:
                flash_queue.append((x_val, y_val))
                already_flashed.add((x_val, y_val))

    flashed_count = len(already_flashed)
    return (flashed_count, [[num if num <= 9 else 0 for num in line] for line in new_data])

def run_steps(data):
    current_data = list(data)
    total_flashes = 0
    for i in range(100):
        print(f'starting step {i}')
        (step_flash_count, current_data) = complete_one_step(current_data)
        total_flashes += step_flash_count
    return total_flashes

total_flashes = run_steps(data)
# Answer: 1647
print(total_flashes)



