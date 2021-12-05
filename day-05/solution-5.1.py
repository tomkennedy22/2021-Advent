import datetime
start_time = datetime.datetime.now()

def interpret_input(line):
    # Input: 535,940 -> 684,940
    # Output: {x1: 535, y1: 940, x2: 684, y2: 940}
    line = line.replace(' ', '').replace('->', ',')
    split_line = line.split(',')

    return {'x1': int(split_line[0]),'y1': int(split_line[1]),'x2': int(split_line[2]),'y2': int(split_line[3])}


input_file = open('input.txt', 'r')
coordinates = [interpret_input(line) for line in input_file]

# Exclude diagonals
coordinates = [coordinate for coordinate in coordinates if coordinate['x1'] == coordinate['x2'] or coordinate['y1'] == coordinate['y2']]

map = {}

for coordinate_obj in coordinates:

    ## Determine step direction: 1 for when x2 > x1, -1 for x2 < x1, 1 for equal
    ##  This helps us build the range of coordinates in the correct direction
    if coordinate_obj['x1'] == coordinate_obj['x2']:
        x_step = 1
    else:
        x_step = int((coordinate_obj['x2'] - coordinate_obj['x1']) / abs(coordinate_obj['x2'] - coordinate_obj['x1']))

    if coordinate_obj['y1'] == coordinate_obj['y2']:
        y_step = 1
    else:
        y_step = int((coordinate_obj['y2'] - coordinate_obj['y1']) / abs(coordinate_obj['y2'] - coordinate_obj['y1']))


    for x in range(coordinate_obj['x1'], coordinate_obj['x2'] + x_step, x_step):
        for y in range(coordinate_obj['y1'], coordinate_obj['y2'] + y_step, y_step):
            coordinate = f'{x},{y}'

            if coordinate not in map:
                map[coordinate] = 0

            map[coordinate] += 1

coordinates_with_multiple_visits = [coordinate for coordinate, count in map.items() if count >= 2]
print(f'{"-"*60}\nNumber of coordinates with multiple visits: *** {len(coordinates_with_multiple_visits)} ***')
# Answer: 5294

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms\n{"-"*60}'  )
