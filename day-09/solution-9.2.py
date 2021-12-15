#failed attempt

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

def get_current_list_from_position(position, input_values):
    list_index = position[0]
    current_list = find_current_list(input_values, list_index)
    return current_list 

def get_index_from_position(position):
    index = position[1]
    return index
        
        
def find_horizontal_neighbors_until_9(current_list, position):
    horizontal_neighbors = []
    positions = []
    if i == 0:
        horizontal_neighbors = horizontal_neighbors_right(current_list, position, horizontal_neighbors)
    elif i == len(current_list) - 1:
        horizontal_neighbors= horizontal_neighbors_left(current_list, position, horizontal_neighbors)
    else:
        right_list = horizontal_neighbors_right(position, current_list, horizontal_neighbors)
        left_list = horizontal_neighbors_left(position, current_list, horizontal_neighbors)
        horizontal_neighbors.extend(right_list)
        horizontal_neighbors.extend(left_list)
    return horizontal_neighbors

#need to find x,y coordinates of each point instead of just the point
#pass in input values each time?
# if x,y coordinate has already been added don't add it again

def horizontal_neighbors_left(position, current_list, neighbor_list):
    x = 1
    positions = []
    lst_index = position[0]
    i = position[1]
    result_set = set()
    while i-x >= 0:
            if current_list[i-x] != 9:
                neighbor_list.append(current_list[i-x])
                positions.append((lst_index, i-x))
                x += 1
            else: 
                break
    return positions

def horizontal_neighbors_right(position, current_list, neighbor_list):
    x = 1
    positions = []
    lst_index = position[0]
    i = position[1]
    while i+x <= len(current_list):
            if current_list[i+x] != 9:
                neighbor_list.append(current_list[i+x])
                positions.append((lst_index, i+x))
                x += 1
            else:
                break
    return positions



def vertical_neighbors_up(position, input_values, neighbor_list):
    lst_index = position[0]
    index = position[1]
    positions = []
    x = 1 
    while lst_index-x >= 0:
        if input_values[lst_index-x][index] != 9:
            neighbor_list.append(input_values[lst_index-x][index])
            positions.append((lst_index-x, index))
            x -= 1
        else:
            break 
    return positions

def vertical_neighbors_down(position, input_values, neighbor_list):
    lst_index = position[0]
    index = position[1]
    positions = []
    x = 1 
    while lst_index+x <= len(input_values):
        if input_values[lst_index+x][index] != 9:
            neighbor_list.append(input_values[lst_index+x][index])
            positions.append((lst_index+x, index))
            x += 1
        else:
            break 
    return positions

def find_vertical_neighbors_until_9(position, input_values):
    vertical_neighbors = []
    lst_index = position[0]
    if lst_index == 0:
        vertical_neighbors = vertical_neighbors_down(position, input_values, vertical_neighbors)
    elif lst_index == len(input_values) - 1:
        vertical_neighbors = vertical_neighbors_up(position, input_values, vertical_neighbors)
    else:
        up_list = vertical_neighbors_up(position, input_values, vertical_neighbors)
        down_list = vertical_neighbors_down(position, input_values, vertical_neighbors)
        vertical_neighbors.extend(up_list)
        vertical_neighbors.extend(down_list)
    return vertical_neighbors
                

results = find_low_points(input_values)
low_points = results[0]
positions = results[1]

basin_dict = {}
basin_points = []
for x in range(0, len(low_points)):
    #point = low_points[x]
    print(f'current point is: {x}')
    position = positions[x]
    print(f'current position is: {position}')
    current_list = get_current_list_from_position(position, input_values)
    print(f'current list is: {current_list}')
    i = get_index_from_position(position)
    print(f'index is: {i}')
    basin_dict[position] = basin_points
    print(f'basin dict: {basin_dict}')
    horizontal_neighbors = find_horizontal_neighbors_until_9(current_list, position)
    print(f'horizontal neighbors: {horizontal_neighbors}')
    if len(horizontal_neighbors) > 0:
        basin_points.append(horizontal_neighbors)
    else: 
        break
    for neighbor in horizontal_neighbors:
        if len(horizontal_neighbors) > 0:
            vertical_neighbors = find_vertical_neighbors_until_9(position, input_values)
            print(f'vertical neighbors: {vertical_neighbors}')
            if vertical_neighbors not in basin_points:
                basin_points.extend(vertical_neighbors)
                print(f'basin points {basin_points}')
            else: 
                continue 
        else: 
            break
        for neighbor in vertical_neighbors:
            if len(vertical_neighbors) > 0:
                horizontal_neighbors = find_horizontal_neighbors_until_9(current_list, position)
                if horizontal_neighbors not in basin_points:
                    basin_points.extend(horizontal_neighbors)
                    print(f'basin points after searching horizontal neighbors of vertical neighbors: {basin_points}')
                else: 
                    continue 
            else:
                break
print(basin_dict)
print(basin_dict.keys())



# for each low point:
# add the point to the list of points being collected
# find horizontal neighbors until you reach 9
# add the horizontal neighbors to a list
# find the vertical neighbors until you reach 9 for each horizontal neighbor in the list, adding their neighbors to a list too
# find vertical neighbors until you reach 9
# add the vertical neighbors to a list
# find horizontal neighbors until you reach 9 for each vertical neighbor in the list, adding their neighbors to a list
# determine the length of the list and add it to a new basin size list

# then, keep only the 3 largest basins and multiply them together
