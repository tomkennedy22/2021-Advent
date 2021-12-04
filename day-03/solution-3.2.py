from collections import Counter
from itertools import groupby

def binary_to_decimal(binary_str):
    return int(binary_str, 2)


def remove_from_master_list(bit, input_values, bit_position):
    bit_position_adjusted = bit_position -1
    if len(input_values) == 1:
        return input_values
    else:
        values_to_keep = []
        for value in input_values:
            bit_of_interest = int(value[bit_position_adjusted])
            if bit_of_interest == bit:
                values_to_keep.append(value)
        return values_to_keep


def find_most_common(bit_list):
    frequencies = groupby(Counter(bit_list).most_common(), lambda x:x[1])
    most_common = [val for val,count in next(frequencies)[1]]
    if len(most_common) > 1:
        most_common = 1
    else:
        most_common = most_common[0]
    return int(most_common)



def find_least_common(bit_list):
    n = len(bit_list)
    frequencies = groupby(Counter(bit_list).most_common()[: -n - 1: -1], lambda x:x[1])
    least_common = [val for val,count in next(frequencies)[1]]
    if len(least_common) > 1:
        least_common = 0
    else:
        least_common = least_common[0]
    return int(least_common)

def generate_bit_list(input_values, n):
    for idx in range(0, n):
        n_bits = [line[idx] for line in input_values]
    return n_bits


def find_oxygen_rating(original_values, updated_values):
    i = 1
    while len(updated_values) != 1:
        if i == 1:
            input_values = original_values
        else:
            input_values = updated_values
        bit_list = generate_bit_list(input_values, i)
        most_common = find_most_common(bit_list)
        updated_values = remove_from_master_list(most_common, input_values, i)
        i += 1
    oxygen_rating_bits = updated_values
    oxygen_binary = "".join(oxygen_rating_bits)
    oxygen_rating_decimal = binary_to_decimal(oxygen_binary)
    return oxygen_rating_decimal


def find_co2_rating(original_values, updated_values):
    i = 1
    while len(updated_values) != 1:
        if i == 1:
            input_values = original_values
        else:
            input_values = updated_values
        bit_list = generate_bit_list(input_values, i)
        least_common = find_least_common(bit_list)
        updated_values = remove_from_master_list(least_common, input_values, i)
        i += 1
    co2_rating_bits = updated_values
    co2_binary = "".join(co2_rating_bits)
    co2_rating_decimal = binary_to_decimal(co2_binary)
    return co2_rating_decimal

input_file = open('input.txt', 'r')
original_values = [line for line in input_file]
updated_values = []

oxygen_rating = find_oxygen_rating(original_values, updated_values)
co2_rating = find_co2_rating(original_values, updated_values)
life_support_rating = oxygen_rating * co2_rating

# My solution = 4636702
print(life_support_rating)