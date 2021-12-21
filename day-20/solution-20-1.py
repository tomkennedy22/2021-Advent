import datetime
import math
start_time = datetime.datetime.now()

input_file = open("input.txt")

def print_grid(image_grid, min_x_bound, max_x_bound, min_y_bound, max_y_bound):

    print('\n')
    pixels = []
    for x in range(min_x_bound, max_x_bound):
        pixel_row = []
        for y in range(min_y_bound, max_y_bound):
            coordinate = image_grid[f'{x},{y}']
            pixel_row.append(coordinate.pixel)
        print(''.join(pixel_row))


class Coordinate:

    def __init__(self, x, y, pixel):

        self.x = x
        self.y = y
        self.coordinate_string = f'{self.x},{self.y}'
        self.pixel = pixel
        self.next_pixel = '.'

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

    def set_new_pixel(self):
        self.pixel = self.next_pixel

    def calculate_pixel(self, image_enhancement_algorithm):

        neighbor_pixels = [neighbor.pixel for neighbor in self.neighbors]
        neighbor_pixel_str = ''.join(neighbor_pixels)

        neighbor_pixel_str = neighbor_pixel_str.replace('.', '0').replace('#', '1')

        neighbor_pixel_val = int(neighbor_pixel_str, 2)
        # print('neighbor_pixel_val', self.coordinate_string, neighbor_pixel_val, neighbor_pixel_str, image_enhancement_algorithm[neighbor_pixel_val])

        self.next_pixel = image_enhancement_algorithm[neighbor_pixel_val]
        return None


    def __repr__(self):
        return f'[{self.x}, {self.y}: {self.pixel}]'


image_enhancement_algorithm = ''
image_grid = {}

max_x_bound = 0
max_y_bound = 0
min_x_bound = 0
min_y_bound = 0

null_coordinate = Coordinate(None, None, '.')

for line_number, line in enumerate(input_file):

    # print(line_number, line)
    if line_number == 0:
        image_enhancement_algorithm = line.strip()

    elif line_number == 1:
        continue

    else:
        y = line_number - 2
        max_y_bound = max([max_y_bound, y])
        new_grid_row = []
        for x, pixel in enumerate(line.strip()):
            image_grid[f'{x},{y}'] = Coordinate(x, y, pixel)
            max_x_bound = max([max_x_bound, x])


enhancement_iterations = 2
max_x_bound = max_x_bound + enhancement_iterations
max_y_bound = max_y_bound + enhancement_iterations
min_x_bound = -1 * enhancement_iterations
min_y_bound = -1 * enhancement_iterations

for x in range(min_x_bound, max_x_bound + 1):

    for y in range(min_y_bound, max_y_bound + 1):
        # print('building', x, y)
        coordinate_string = f'{x},{y}'
        if coordinate_string not in image_grid:
            image_grid[coordinate_string] = Coordinate(x, y, '.')


for coordinate_string, coordinate in image_grid.items():
    coordinate.add_neighbors(image_grid, max_x_bound, max_y_bound, null_coordinate)


print(image_grid)
print_grid(image_grid, min_x_bound, max_x_bound, min_y_bound, max_y_bound )
for enhancement_iteration in range(1, enhancement_iterations+1):
     for coordinate_string, coordinate in image_grid.items():
         coordinate.calculate_pixel(image_enhancement_algorithm)

     for coordinate_string, coordinate in image_grid.items():
         coordinate.set_new_pixel()
         #print(coordinate.pixel, coordinate.next_pixel)
     print_grid(image_grid, min_x_bound, max_x_bound, min_y_bound, max_y_bound )

pixel_count = len([coordinate for coordinate_string, coordinate in image_grid.items() if coordinate.pixel == '#'])


dash_line = f'{"-"*60}'
print(dash_line)
print(f'Dot count: *** {pixel_count} ***')

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms'  )
print(dash_line)
