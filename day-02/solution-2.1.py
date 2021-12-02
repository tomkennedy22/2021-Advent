input_file = open('input.txt', 'r')
input_values = [line for line in input_file]

h_position = 0
depth = 0
for i in input_values:
    x = i.split(" ")
    direction = x[0]
    magnitude = int(x[1])

    if direction == 'forward':
        h_position += magnitude
    elif direction == 'down':
        depth += magnitude
    elif direction == 'up':
        depth -= magnitude

# My Solution: 1990000
print(h_position * depth)
