input_file = open('input.txt', 'r')
input_values = [int(line) for line in input_file]

window_size = 3
place = 0
increase_count = 0
previous_sum = None

for idx, value in enumerate(input_values):
    window = input_values[idx:idx+window_size]
    if len(window) == 3:
        sum_value = sum(window)
        increase_count += 1 if previous_sum is not None and sum_value > previous_sum else 0
        previous_sum = sum_value

print(increase_count)