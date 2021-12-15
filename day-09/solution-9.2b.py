from collections import deque
import math

input_file = open('input.txt', 'r')
input_values= [list(line.strip()) for line in input_file]

for sequence in input_values:
    for i in range(0, len(sequence)):
        sequence[i] = int(sequence[i])

def check_if_low_point(input_values, x, y):
    for (x_val, y_val) in find_neighbors(input_values, x, y):
        orig_value = input_values[x][y]
        neighbor = input_values[x_val][y_val]
        if orig_value == 9 or neighbor < orig_value:
            return False
    return True

def find_neighbors(input_values, x, y):
    neighbor_positions = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    neighbor_list = []
    for (x_val, y_val) in neighbor_positions:
        if 0 <= x_val < len(input_values) and 0 <= y_val < len(input_values[x]):
            neighbor_list.append((x_val, y_val))
    return neighbor_list



def find_low_points_new(input_values):
    low_points = []
    for x in range(len(input_values)):
        for y in range(len(input_values[x])):
            if check_if_low_point(input_values, x, y):
                low_points.append((x, y))
    return low_points


def find_basin(input_values, x, y):
    basin = []
    checked_points = set()
    queue = deque([(x,y)])
    while queue:
        (x_val, y_val) = queue.pop()
        if (x_val, y_val) in checked_points:
            continue
        else:
            checked_points.add((x_val, y_val))
            if input_values[x_val][y_val] != 9:
                basin.append((x_val, y_val))
                for (neighbor_x, neighbor_y) in find_neighbors(input_values, x_val, y_val):
                    neighbors_to_add = []
                    if (neighbor_x, neighbor_y) not in checked_points:
                        neighbors_to_add.append((neighbor_x, neighbor_y))
                        queue.extend(neighbors_to_add)
    return basin



low_points = find_low_points_new(input_values)

basins = [] 
for (x, y) in low_points:
    basin = find_basin(input_values, x, y)
    basins.append(basin)

length_list = []
for basin in basins: 
    length_list.append(len(basin))

top_three = sorted(length_list, reverse=True)[0:3]
result = math.prod(top_three)
#Answer: 1038240
print(result)


