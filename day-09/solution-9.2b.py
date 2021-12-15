from collections import deque

input_file = open('test_input.txt', 'r')
input_values= [list(line.strip()) for line in input_file]

for sequence in input_values:
    for i in range(0, len(sequence)):
        sequence[i] = int(sequence[i])


def compare_horizontal_neighbors(current_list, i):
    if i == 0:
        if current_list[i] - current_list[i+1] < 0:
            return True
        else:
            return False
    elif i == len(current_list) - 1:
        if current_list[i] - current_list[i-1] < 0:
            return True
        else:
            return False
    elif current_list[i] - current_list[i-1] < 0 and current_list[i] - current_list[i+1] < 0:
        return True
    else:
        return False

def compare_vertical_neighbors(current_list, list_above, list_below, i):
    results = [c < b and c < a for c, b, a in zip(current_list, list_below, list_above)]
    result = results[i]
    return result

def find_current_list(input_values, i):
    current_list = input_values[i]
    return current_list

def find_list_above(input_values, i):
    if i == 0:
        return [9 for i in range(len(input_values[i]))]
    else:
        list_above = input_values[i-1]
    return list_above 

def find_list_below(input_values, i):
    if i == len(input_values) - 1:
        return [9 for i in range(len(input_values[i]))]
    else:
        list_below = input_values[i+1]
    return list_below


def find_low_points(input_values):
    results = []
    low_points = []
    positions = []
    for i in range(0, len(input_values)):
        current_list = find_current_list(input_values, i)
        list_above = find_list_above(input_values, i)
        list_below = find_list_below(input_values, i)
        for x in range(0, len(current_list)):
            vertical_result = compare_vertical_neighbors(current_list, list_above, list_below, x)
            horizontal_result = compare_horizontal_neighbors(current_list, x)
            if vertical_result and horizontal_result:
                low_points.append(current_list[x])
                positions.append((i, x))
                results.append(low_points)
                results.append(positions)

    return results

# ----------------------------------

#def find_neighbors

def find_basin(input_values, i, x):
    basin = []
    basin_points = set()
    queue = deque([(i, x)])

    while queue:
        (current_i, current_x) = queue.pop()

        if (current_i, current_x) in basin_points:
            continue
        else: 
            basin_points.add((current_i, current_x))
            if input_values[current_i][current_x] != 9:
                basin.append((current_i, current_x))
                #queue.extend(([next_i, next_x) for (next_i, next_x) in ])