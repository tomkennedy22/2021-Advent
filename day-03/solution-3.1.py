def binary_to_decimal(binary_str):
    return int(binary_str, 2)


input_file = open('input.txt', 'r')
input_values = [line for line in input_file]
n = len(input_values[0]) - 1

gamma_bits = []
epsilon_bits = []
for idx in range(0, n):
    n_bits = [line[idx] for line in input_values]
    if n_bits.count('1') > int((len(input_values) / 2)):
        gamma_bits.append('1')
        epsilon_bits.append('0')
    else:
        gamma_bits.append('0')
        epsilon_bits.append('1')

gamma_binary = "".join(gamma_bits)
epsilon_bits = "".join(epsilon_bits)

# My solution = 845186
print(binary_to_decimal(gamma_binary) * binary_to_decimal(epsilon_bits))

