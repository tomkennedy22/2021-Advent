import datetime
import json
start_time = datetime.datetime.now()


def in_target(x, y, target_x_area, target_y_area):
    if min(target_x_area) <= x <= max(target_x_area) and min(target_y_area) <= y <= max(target_y_area):
        return True

    return False


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
        print('Testing', json.dumps({'initial_velocities': initial_velocities, 'x':x, 'y':y, 'highest_y':highest_y, 'x_velocity':x_velocity, 'y_velocity':y_velocity, 'target_x_area': target_x_area, 'target_y_area': target_y_area}))
        return highest_y
    return 0

input_file = open("input.txt")
input_line = input_file.readline()

#'target area: x=20..30, y=-10..-5' -> (20,30) (10, -5)
input_split = input_line.strip().replace(',', '=').replace('..','=').split('=')

target_x_area = (int(input_split[1]), int(input_split[2]))
target_y_area = (int(input_split[4]), int(input_split[5]))

x = 0
y = 0

highest_y = 0
for x_velocity in range(1, max(target_x_area) + 1):
    for y_velocity in range(0,1000):
        highest_y = max([highest_y, test_inputs(0, 0, x_velocity, y_velocity, target_x_area, target_y_area)])


dash_line = f'{"-"*60}'
print(dash_line)
print(f'Highest y: *** {highest_y} ***')

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms'  )
print(f'\tGrid bounds: {x}, {y}'  )
print(dash_line)
