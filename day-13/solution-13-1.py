import datetime
import math
start_time = datetime.datetime.now()

input_file = open("input.txt")

class Coordinate:

    def __init__(self, coordinate_line):

        coordinates = coordinate_line.split(',')

        self.x = int(coordinates[0])
        self.y = int(coordinates[1])

    def fold(self, instruction):

        setattr(self, instruction.direction, instruction.split_coordinate - abs(getattr(self, instruction.direction) - instruction.split_coordinate))

    def __repr__(self):
        return f'[{self.x}, {self.y}]'


class Instruction:

    def __init__(self, instruction_line):

        instruction_line = instruction_line.replace('fold along ', '')
        instruction_line = instruction_line.split('=')

        self.direction = instruction_line[0]
        self.split_coordinate = int(instruction_line[1])

    def __repr__(self):

        return f'fold along {self.direction}={self.split_coordinate}'


coordinates = []
fold_instructions = []

for line in input_file:
    line = line.strip()
    if len(line) == 0:
        continue
    elif 'fold' in line:
        fold_instructions.append(Instruction(line))

    else:
        coordinates.append(Coordinate(line))

max_x = max([coordinate.x for coordinate in coordinates])
max_y = max([coordinate.y for coordinate in coordinates])

fold_instructions = [fold_instructions[0]]

for instruction in fold_instructions:

    for coordinate in coordinates:
        coordinate.fold(instruction)

        if instruction.direction == 'y':
            max_y = instruction.split_coordinate
        else:
            max_x = instruction.split_coordinate


grid = [[' ' for row in range(0, max_x + 1)] for col in range(0, max_y + 1)]
display_char = u"\u2588"

for coordinate in coordinates:
    try:
        grid[coordinate.y][coordinate.x] = display_char
    except Exception as e:
        print(e, coordinate)

dot_count = 0

for row_ind, col in enumerate(grid):
    print(''.join(col))
    for col_ind, cell in enumerate(col):
        dot_count += 1 if cell == display_char else 0


dash_line = f'{"-"*60}'
print(dash_line)
print(f'Dot count: *** {dot_count} ***')

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms'  )
print(f'\tGrid bounds: {max_x}, {max_y}'  )
print(dash_line)
