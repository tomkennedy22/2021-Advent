import datetime
start_time = datetime.datetime.now()

import heapq
import json

def encode_position_str(position, direction = None):
    # (1,2) -> '1,2'
    if direction is None:
        return f'{position[0]},{position[1]}'
    else:
        return f'{position[0] + direction[0]},{position[1] + direction[1]}'


def decode_position_str(node):
    # '1,2' -> (1,2)
    return (int(node.split(',')[0]), int(node.split(',')[1]))


def get_grid_value(grid, node_str):
    node_vals = decode_position_str(node_str)
    return grid[node_vals[0]][node_vals[1]]

def set_grid_value(grid, node_str, val):
    node_vals = decode_position_str(node_str)
    grid[node_vals[0]][node_vals[1]] = val


def calculate_neighbors(node, grid, node_map):
    possible_directions = [
        [-1,0],
        [1, 0],
        [0, -1],
        [0, 1]
    ]

    (x,y) = decode_position_str(node)

    # Silly way to ensure positions are within grid
    possible_directions = [direction for direction in possible_directions if (x + direction[0]) >= 0]
    possible_directions = [direction for direction in possible_directions if (x + direction[0]) < len(grid)]
    possible_directions = [direction for direction in possible_directions if (y + direction[1]) >= 0]
    possible_directions = [direction for direction in possible_directions if (y + direction[1]) < len(grid[0])]

    neighbor_list = [(x + direction[0], y + direction[1]) for direction in possible_directions]

    node_map[node]['neighbors'] = [encode_position_str(node_coordinates) for node_coordinates in neighbor_list]


def increment_values(arr, modifier):
    new_arr = []

    for num in arr:
        adj_num = num + modifier
        if adj_num > 9:
            adj_num = adj_num % 9

        new_arr.append(adj_num)

    return new_arr


input_file = open('input.txt', 'r')

node_map = {}
grid = []

for y, line in enumerate(input_file):
    new_row = []
    for x, num in enumerate(line.strip()):

        new_row.append(int(num))

    grid.append(new_row)

for row in grid:
    original_row = row.copy()
    for modifier in range(1,5):
        row += increment_values(original_row, modifier)

grid_len = len(grid)
for modifier in range(1,5):
    for row_ind in range(0, grid_len):
        grid.append(increment_values(grid[row_ind], modifier))

total_values = len(grid) * len(grid[0])
max_value = total_values * 10

for y, row in enumerate(grid):
    for x, num in enumerate(row):
        coordinate_str = f'{x},{y}'
        node_map[coordinate_str] = {'distance': num,'running_distance': max_value, 'neighbors': {}}


current_position = (0,0)
target_position = (len(grid) - 1, len(grid[0]) - 1)


for node, node_neighbors in node_map.items():
    calculate_neighbors(node, grid, node_map)

nodes_to_visit = {node: None for node in node_map}
visited_nodes = {}
current_node = '0,0'
total_distance = 0

iterations = 0

node_map[current_node]['running_distance'] = 0
node_map[current_node]['distance'] = 0

nodes_to_visit = [(0, current_node)]

while len(nodes_to_visit) > 0:
    current_distance, current_node = heapq.heappop(nodes_to_visit)

    if current_distance > node_map[current_node]['running_distance']:
        continue

    for neighbor_node in node_map[current_node]['neighbors']:
        neighbor_distance = node_map[neighbor_node]['distance']
        test_distance = current_distance + neighbor_distance

        if test_distance < node_map[neighbor_node]['running_distance']:
            node_map[neighbor_node]['running_distance'] = test_distance
            heapq.heappush(nodes_to_visit, (test_distance, neighbor_node))


traversal_time = node_map[encode_position_str(target_position)]['running_distance']


dash_line = f'{"-"*60}'
print(dash_line)
print(f'traversal_time: *** {traversal_time} ***')

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms'  )
print(f'\tTarget position: {target_position}'  )
print(dash_line)
