def parse_input_row(row):
    split_row = row.split(' ')
    return {'direction': split_row[0], 'magnitude': int(split_row[1])}

input_file = open('input.txt', 'r')
input_values = [parse_input_row(line) for line in input_file]

h_position = 0
depth = 0
aim = 0
for step in input_values:

    if step['direction'] == 'forward':
        h_position += step['magnitude']
        depth += step['magnitude'] * aim
    elif step['direction'] == 'down':
        aim += step['magnitude']
    elif step['direction'] == 'up':
        aim -= step['magnitude']

# My Solution: 1990000
print(h_position * depth)
