import datetime
import multiprocessing as mp

start_time = datetime.datetime.now()

input_file = open("input.txt")
f_line = input_file.readline().strip().split(',')
numbers = [int(number) for number in f_line]

eight_day_left_count = sum([number == 8 for number in numbers]) #0
seven_day_left_count = sum([number == 7 for number in numbers]) #0
six_day_left_count = sum([number == 6 for number in numbers]) #0
five_day_left_count = sum([number == 5 for number in numbers]) #38
four_day_left_count = sum([number == 4 for number in numbers]) #34
three_day_left_count = sum([number == 3 for number in numbers]) #45
two_day_left_count = sum([number == 2 for number in numbers]) #39
one_day_left_count = sum([number == 1 for number in numbers]) #144
zero_day_left_count = sum([number == 0 for number in numbers]) #0


day = 1
for day in range(1, 256 + 1):
    one_day_holder = one_day_left_count
    one_day_left_count = two_day_left_count
    two_day_left_count = three_day_left_count
    three_day_left_count = four_day_left_count
    four_day_left_count = five_day_left_count
    five_day_left_count = six_day_left_count
    six_day_left_count = zero_day_left_count + seven_day_left_count
    seven_day_left_count = eight_day_left_count
    eight_day_left_count = zero_day_left_count
    zero_day_left_count = one_day_holder
    total_fish = zero_day_left_count + one_day_left_count + two_day_left_count + three_day_left_count + four_day_left_count + five_day_left_count + six_day_left_count + seven_day_left_count + eight_day_left_count
    day += 1

# Answer: 1674303997472
print(total_fish)

