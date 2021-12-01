input_file = open('input.txt', 'r')
input_values = [int(line) for line in input_file]

previous_depth = None
increase_count = 0
for depth_value in input_values:
    increase_count += 1 if previous_depth is not None and depth_value > previous_depth else 0
    previous_depth = depth_value

print(increase_count)