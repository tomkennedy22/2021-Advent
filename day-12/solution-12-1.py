import datetime
import math
start_time = datetime.datetime.now()


class Cave:

    def __init__(self, cave_name):

        self.cave_name = cave_name
        self.connected_caves = []

        if cave_name == cave_name.lower():
            self.cave_size = 's'
        else:
            self.cave_size = 'L'

    def cave_can_be_visited(self, visited_set):
        if self.cave_name not in visited_set or self.cave_size == 'L':
            return True

        return False

    def add_connection(self, connected_cave):
        self.connected_caves.append(connected_cave)

    def __repr__(self):
        return f"{self.cave_name} is a {self.cave_size} cave, and is connected to caves {[cave.cave_name for cave in self.connected_caves]}"

input_file = open("input.txt")
paths = [line.strip().split('-') for line in input_file]

cave_map = {}

path_count = 0

for path in paths:
    path_start = path[0]
    path_end = path[1]

    if path_start not in cave_map:
        path_start_cave = Cave(path_start)
        cave_map[path_start] = path_start_cave

    if path_end not in cave_map:
        path_end_cave = Cave(path_end)
        cave_map[path_end] = path_end_cave

    path_start_cave = cave_map[path_start]
    path_end_cave = cave_map[path_end]

    path_start_cave.add_connection(path_end_cave)
    path_end_cave.add_connection(path_start_cave)


def traverse_caves(current_cave, visited_set = [], path_count = 0):

    visited_set.append(current_cave.cave_name)

    if current_cave.cave_name == 'end':
        return path_count + 1

    for connected_cave in current_cave.connected_caves:
        if connected_cave.cave_can_be_visited(visited_set):
            path_count += traverse_caves(connected_cave, visited_set.copy())

    return path_count

    

path_count = traverse_caves(cave_map['start'], [])

dash_line = f'{"-"*60}'
print(dash_line)
print(f'Path count: *** {path_count} ***')

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms'  )
print(dash_line)
