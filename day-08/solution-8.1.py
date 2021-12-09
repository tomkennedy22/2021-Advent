input_file = open("input.txt")
values = [line for line in input_file]

output_list = []
for line in values:
    output = line.split('|')[1].strip().split(" ")
    output_list.extend(output)

# Identify all the unique digits
known_digits = []
for output_digit in output_list:
    # 1
    if len(output_digit) == 2:
        known_digits.append(output_digit)
    # 4
    elif len(output_digit) == 4:
        known_digits.append(output_digit)
    # 7
    elif len(output_digit) == 3:
        known_digits.append(output_digit)
    # 8
    elif len(output_digit) == 7:
        known_digits.append(output_digit)
    else:
        continue

print(len(known_digits))
