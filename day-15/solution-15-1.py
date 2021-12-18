import datetime
start_time = datetime.datetime.now()

def encode_position_str(position, direction = None):
    # (1,2) -> '1,2'
    if direction is None:
        return f'{position[0]},{position[1]}'
    else:
        return f'{position[0] + direction[0]},{position[1] + direction[1]}'


def decode_position_str(node):
    # '1,2' -> (1,2)
    return (int(node.split(',')[0]), int(node.split(',')[1]))


def calculate_neighbors(node, grid, node_map):
    possible_directions = [[-1,0], [1, 0], [0, -1], [0, 1]]

    (x,y) = decode_position_str(node)

    # Silly way to ensure positions are within grid
    possible_directions = [direction for direction in possible_directions if (x + direction[0]) >= 0]
    possible_directions = [direction for direction in possible_directions if (x + direction[0]) < len(grid)]
    possible_directions = [direction for direction in possible_directions if (y + direction[1]) >= 0]
    possible_directions = [direction for direction in possible_directions if (y + direction[1]) < len(grid[0])]

    neighbor_list = [(x + direction[0], y + direction[1]) for direction in possible_directions]

    node_map[node] = {encode_position_str(node_coordinates): grid[node_coordinates[0]][node_coordinates[1]] for node_coordinates in neighbor_list}


input_file = open('input.txt', 'r')

node_map = {}
grid = []

for y, line in enumerate(input_file):
    new_row = []
    for x, num in enumerate(line.strip()):
        coordinate_str = f'{x},{y}'
        node_map[coordinate_str] = {}

        new_row.append(int(num))

    grid.append(new_row)


current_position = (0,0)
target_position = (len(grid) - 1, len(grid[0]) - 1)

for node, node_neighbors in node_map.items():
    calculate_neighbors(node, grid, node_map)

nodes_to_visit = {node: None for node in node_map}
visited_nodes = {}
current_node = '0,0'
total_distance = 0

while len(nodes_to_visit) > 0:
    for neighbour_node, neighbor_distance in node_map[current_node].items():
        if neighbour_node in nodes_to_visit:
            test_distance = total_distance + neighbor_distance

            if nodes_to_visit[neighbour_node] is None or nodes_to_visit[neighbour_node] > test_distance:
                nodes_to_visit[neighbour_node] = test_distance

    visited_nodes[current_node] = total_distance
    del nodes_to_visit[current_node]

    next_nodes = [[node, distance] for node, distance in nodes_to_visit.items() if distance is not None]
    if len(next_nodes) > 0:
        current_node, total_distance = sorted(next_nodes, key = lambda x: x[1])[0]


traversal_time = visited_nodes[encode_position_str(target_position)]


dash_line = f'{"-"*60}'
print(dash_line)
print(f'traversal_time: *** {traversal_time} ***')

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms'  )
print(dash_line)
