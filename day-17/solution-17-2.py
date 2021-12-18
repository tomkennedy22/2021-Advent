import datetime
import json
start_time = datetime.datetime.now()


def in_target(x, y, target_x_area, target_y_area):
    return min(target_x_area) <= x <= max(target_x_area) and min(target_y_area) <= y <= max(target_y_area)


def test_inputs(x, y, x_velocity, y_velocity, target_x_area, target_y_area):

    initial_velocities = (x_velocity, y_velocity)
    highest_y = y
    hit_target = False
    while x <= max(target_x_area) and y >= min(target_y_area) and not hit_target:
        x += x_velocity
        y += y_velocity
        if x_velocity > 0:
            x_velocity -= 1
        elif x_velocity < 0:
            x_velocity += 1

        y_velocity -= 1

        highest_y = max([highest_y, y])
        hit_target = hit_target or in_target(x, y, target_x_area, target_y_area)

    if hit_target:
        return 1
    return 0

input_file = open("input.txt")
input_line = input_file.readline()

#'target area: x=20..30, y=-10..-5' -> (20,30) (10, -5)
input_split = input_line.strip().replace(',', '=').replace('..','=').split('=')

target_x_area = (int(input_split[1]), int(input_split[2]))
target_y_area = (int(input_split[4]), int(input_split[5]))


hit_count = 0
for x_velocity in range(1, max(target_x_area) + 50):
    for y_velocity in range(min(target_y_area) - 10,900):
        hit_count += 1 if test_inputs(0, 0, x_velocity, y_velocity, target_x_area, target_y_area) else 0


dash_line = f'{"-"*60}'
print(dash_line)
print(f'Hit count: *** {hit_count} ***')

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms'  )
print(dash_line)
