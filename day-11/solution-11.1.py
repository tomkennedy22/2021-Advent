# failed attempt

input_file = open("test_input.txt")
input_values = [list(line.strip()) for line in input_file]

data = [list(map(int,i)) for i in input_values]

def find_coordinates(data):
    coordinates=[((i,j),v) for i,lst in enumerate(data) for j,v in enumerate(lst)]
    co_dict = {}
    for coordinate in coordinates:
        co_dict[coordinate[0]] = coordinate[1]
    return co_dict

def add_one_to_coordinate_values(coordinate, coordinates):
    value = coordinates[coordinate]
    d = {}
    d[coordinate] = value +1
    coordinates.update(d)
    return coordinates

def find_neighbors(coordinate, coordinates):
    neighbors = []
    horizontal_position = coordinate[1]
    vertical_position = coordinate[0]
    up = (vertical_position -1, horizontal_position)
    right = (vertical_position, horizontal_position +1)
    down = (vertical_position +1, horizontal_position)
    left = (vertical_position, horizontal_position -1)
    up_right = (vertical_position-1, horizontal_position+1)
    down_right = (vertical_position+1, horizontal_position+1)
    down_left = (vertical_position+1, horizontal_position-1)
    up_left = (vertical_position-1, horizontal_position-1)
    if up in coordinates:
        neighbors.append(up)
    if right in coordinates:
        neighbors.append(right)
    if down in coordinates:
        neighbors.append(down)
    if left in coordinates:
        neighbors.append(left)
    if up_right in coordinates:
        neighbors.append(up_right)
    if down_right in coordinates:
        neighbors.append(down_right)
    if down_left in coordinates:
        neighbors.append(down_left)
    if up_left in coordinates:
        neighbors.append(up_left)
    return neighbors


def complete_one_step(data):
    #data = [list(map(lambda x:x+1, x)) for x in data]
    max_num = max([sub_list[-1] for sub_list in data])
    coordinates = find_coordinates(data)
    print(f'coordinates are: {coordinates}')
    already_flashed = []
    flash_count = 0
    #if max_num > 9:
    while max_num > 9:
        print(f'started while loop -----------')
        check_list = [key for key,value in coordinates.items() if value >9]
        if len(check_list) == 0:
            continue
        print(f' values greater than 9 are: {check_list}')
        #print(f'value of 3,9 is {coordinates[(3,9)]}')
        #for key in coordinates.keys():
        for key in check_list:
            #while max_num > 9:
            #print(f'current coordinate: {key}')
            #print(f'value of coordinate: {coordinates[key]}')
            if coordinates[key] <= 9:
                continue
            else:
                neighbor_list = []
                already_flashed.append(key)
                print(f'already flashed list is: {already_flashed}')
                print(f'coordinate that flashed is: {key, coordinates[key]}')
                coordinates[key] = 0
                flash_count += 1
                print(f'flash count is now: {flash_count}')
                
                neighbors = find_neighbors(key, coordinates)
        
                neighbor_list.extend(neighbors)
                print(f'found {len(neighbors)} neighbors: {neighbors}')
                print(f'full list of neighbors is: {neighbor_list}')

                for neighbor in neighbor_list:
                    if neighbor in already_flashed:
                        neighbor_list.remove(neighbor)
                    else:
                        coordinates = add_one_to_coordinate_values(neighbor, coordinates)
                        max_num = max(coordinates.values())
                        if max_num <= 9:
                            break
                        else:
                            continue
    return flash_count


    
def run_steps(data):
    flash_count_list = []
    i = 1
    for i in range(1, 10+1):
        data = [list(map(lambda x:x+1, x)) for x in data]
        print(f'Starting step #{i}')
        flash_count = complete_one_step(data)
        print(f'flash count in step {i} is {flash_count}')
        flash_count_list.append(flash_count)
    return flash_count_list 

# flash_list = run_steps(data)
# total_flashes = sum(flash_list)
# print(total_flashes)



