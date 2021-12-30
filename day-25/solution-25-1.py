import datetime
import math
start_time = datetime.datetime.now()

input_file = open("input.txt")

def print_grid(cucumber_grid, min_x_bound, max_x_bound, min_y_bound, max_y_bound):

    print('\n')
    cucumbers = []
    for y in range(min_y_bound, max_y_bound+1):
        cucumber_row = []
        for x in range(min_x_bound, max_x_bound+1):
            coordinate = cucumber_grid[f'{x},{y}']
            cucumber_row.append(coordinate.type)
        print( ''.join(cucumber_row))

def find_cucumbers(cucumber_grid, direction = 'south'):
    search_char = '>' if direction == 'east' else 'v'
    result_set = set()

    for coordinate_str, coordinate in cucumber_grid.items():
        if coordinate.type == search_char:
            result_set.add(coordinate_str)

    return result_set


class Coordinate:

    def __init__(self, x, y, type):

        self.x = x
        self.y = y
        self.coordinate_string = f'{self.x},{self.y}'
        self.type = type

    def add_neighbors(self, image_grid, max_x_bound, max_y_bound, null_coordinate):

        self.neighbors = []

        neighbor_directions = [
            [-1,  -1], [0, -1], [1, -1],
            [-1,   0], [0,  0], [1,  0],
            [-1,   1], [0,  1], [1,  1],
        ]

        # if self.x == max_x_bound or self.x == 0:
        #     return False
        #
        # if self.y == max_y_bound or self.y == 0:
        #     return False

        for neighbor_direction in neighbor_directions:
            grid_coordinate_str = f'{self.x + neighbor_direction[0]},{self.y + neighbor_direction[1]}'
            self.neighbors.append(image_grid.get(grid_coordinate_str, null_coordinate))


    def calculate_pixel(self, image_enhancement_algorithm):

        neighbor_pixels = [neighbor.pixel for neighbor in self.neighbors]
        neighbor_pixel_str = ''.join(neighbor_pixels)

        neighbor_pixel_str = neighbor_pixel_str.replace('.', '0').replace('#', '1')

        neighbor_pixel_val = int(neighbor_pixel_str, 2)
        # print('neighbor_pixel_val', self.coordinate_string, neighbor_pixel_val, neighbor_pixel_str, image_enhancement_algorithm[neighbor_pixel_val])

        self.next_pixel = image_enhancement_algorithm[neighbor_pixel_val]
        return None


    def next_coordinate_str(self, max_x_bound, max_y_bound):
        next_x = self.x
        next_y = self.y
        if self.type == '>':
            next_x += 1
            next_x %= (max_x_bound + 1)
        elif self.type == 'v':
            next_y += 1
            next_y %= (max_y_bound + 1)

        new_coordinate_str = f'{next_x},{next_y}'

        # print('next_coordinate_str', self.type, f'{self.x},{self.y} to {next_x},{next_y}', new_coordinate_str )

        return new_coordinate_str


    def __repr__(self):
        return f'[{self.x}, {self.y}: {self.pixel}]'


cucumber_grid = {}
east_bound_cucumbers = set()
south_bound_cucumbers = set()

for y, line in enumerate(input_file):

    new_grid_row = []
    for x, cell in enumerate(line.strip()):
        cucumber_grid[f'{x},{y}'] = Coordinate(x, y, cell)

max_x_bound = x
max_y_bound = y

print('max_x_bound', max_x_bound, 'max_y_bound', max_y_bound)

print_grid(cucumber_grid, 0, max_x_bound, 0, max_y_bound)

step_count = 1
still_moving = True


while still_moving:
    movement_count = 0
    east_bound_cucumbers = find_cucumbers(cucumber_grid, 'east')
    south_bound_cucumbers = find_cucumbers(cucumber_grid, 'south')
    moving_cucumbers = []

    print(f'================\nStep {step_count}')

    # print(east_bound_cucumbers)
    # print(south_bound_cucumbers)
    #
    for cucumber_coordinate_str in list(east_bound_cucumbers):
        next_coordinate_str = cucumber_grid[cucumber_coordinate_str].next_coordinate_str(max_x_bound, max_y_bound)
        if next_coordinate_str not in east_bound_cucumbers and next_coordinate_str not in south_bound_cucumbers:
            cucumber_grid[next_coordinate_str].next_type = '>'
            cucumber_grid[cucumber_coordinate_str].next_type = '.'
            moving_cucumbers.append(next_coordinate_str)
            moving_cucumbers.append(cucumber_coordinate_str)
            movement_count += 1

    # print('Moving ', moving_cucumbers)
    for cucumber_coordinate_str in list(moving_cucumbers):
        cucumber_grid[cucumber_coordinate_str].type = cucumber_grid[cucumber_coordinate_str].next_type
        cucumber_grid[cucumber_coordinate_str].next_type = '.'

    east_bound_cucumbers = find_cucumbers(cucumber_grid, 'east')
    south_bound_cucumbers = find_cucumbers(cucumber_grid, 'south')
    moving_cucumbers = []
    # print_grid(cucumber_grid, 0, max_x_bound, 0, max_y_bound)

    for cucumber_coordinate_str in list(south_bound_cucumbers):
        next_coordinate_str = cucumber_grid[cucumber_coordinate_str].next_coordinate_str(max_x_bound, max_y_bound)
        if next_coordinate_str not in east_bound_cucumbers and next_coordinate_str not in south_bound_cucumbers:
            cucumber_grid[next_coordinate_str].next_type = 'v'
            cucumber_grid[cucumber_coordinate_str].next_type = '.'
            moving_cucumbers.append(next_coordinate_str)
            moving_cucumbers.append(cucumber_coordinate_str)
            movement_count += 1

    # print('Moving ', moving_cucumbers)
    for cucumber_coordinate_str in list(moving_cucumbers):
        cucumber_grid[cucumber_coordinate_str].type = cucumber_grid[cucumber_coordinate_str].next_type
        cucumber_grid[cucumber_coordinate_str].next_type = '.'


    # print(f'movement_count: {movement_count}')
    # print_grid(cucumber_grid, 0, max_x_bound, 0, max_y_bound)

    if movement_count == 0 :
        still_moving = False
    else:
        step_count += 1




dash_line = f'{"-"*60}'
print(dash_line)
print(f'step_count: *** {step_count} ***')

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms'  )
print(dash_line)
