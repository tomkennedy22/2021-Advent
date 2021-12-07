import datetime
start_time = datetime.datetime.now()

def find_median(arr):

    # O(n log(n)) algo complexity...
    arr = sorted(arr)

    if len(arr) % 2 == 0:
        return int((arr[int(len(arr) / 2) - 1] + arr[int(len(arr) / 2)]) / 2)
    return int(arr[int(len(arr) / 2) - 1])


input_file = open("input.txt")
f_line = input_file.readline().strip().split(',')
starting_positions = [int(position) for position in f_line]

position_to_move_to = find_median(starting_positions)
# O(n) algo complexity
fuel_used = sum([abs(position - position_to_move_to) for position in starting_positions])


dash_line = f'{"-"*60}'
print(dash_line)
print(f'Fuel used: *** {fuel_used} ***')

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms'  )
print(f'\tMedian position: {position_to_move_to}'  )
print(dash_line)
