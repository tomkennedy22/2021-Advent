import datetime
import math
start_time = datetime.datetime.now()

def fuel_calculator(starting_position, ending_position):
    distance_traveled = abs(starting_position - ending_position)

    return int(((distance_traveled ** 2) + distance_traveled) / 2)


#Had to do funny logic here... floor and ceil give different average values, causing different fuel used. We can just test both floor & ceil
def find_means(arr):

    return (math.floor(sum(arr) / len(arr)), math.ceil(sum(arr) / len(arr)))


input_file = open("input.txt")
f_line = input_file.readline().strip().split(',')
starting_positions = [int(position) for position in f_line]


possible_positions_to_move_to = find_means(starting_positions)
min_fuel_used = 0
for position_to_move_to in possible_positions_to_move_to:
    fuel_used = sum([fuel_calculator(position, position_to_move_to) for position in starting_positions])
    min_fuel_used = min(min_fuel_used, fuel_used) or fuel_used


dash_line = f'{"-"*60}'
print(dash_line)
print(f'Fuel used: *** {min_fuel_used} ***')

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms'  )
print(f'\tMedian position: {position_to_move_to}'  )
print(dash_line)
