input_file = open("input.txt")
values = [line for line in input_file]

decoded_outputs = []

for line in values:
    data = line.strip().split(' | ')
    signal_patterns = data[0].split()
    signal_patterns = [''.join(sorted(pattern)) for pattern in signal_patterns]
    outputs = data[1].split()
    outputs = [''.join(sorted(output)) for output in outputs]

    mapping = {}
    reverse_mapping = {}

    # Known values
    for pattern in signal_patterns:
        pattern_length = len(pattern)
        # 1
        if pattern_length == 2:
            mapping[pattern] = 1
            reverse_mapping[1] = set(pattern)
        # 4
        elif pattern_length == 4:
            mapping[pattern] = 4
            reverse_mapping[4] = set(pattern)
        # 7
        elif pattern_length == 3:
            mapping[pattern] = 7
            reverse_mapping[7] = set(pattern)
        # 8
        elif pattern_length == 7:
            mapping[pattern] = 8
            reverse_mapping[8] = set(pattern)
        else:
            continue

    for pattern in signal_patterns:
        pattern_length = len(pattern)
        pattern_set = set(pattern)

        if pattern_length == 6:
            if not reverse_mapping[1].issubset(pattern_set):
                mapping[pattern] = 6
            elif reverse_mapping[4].issubset(pattern_set):
                mapping[pattern] = 9
            else:
                mapping[pattern] = 0
        elif pattern_length == 5:
            if reverse_mapping[1].issubset(pattern_set):
                mapping[pattern] = 3
            elif (reverse_mapping[4] | pattern_set) == reverse_mapping[8]:
                mapping[pattern] = 2
            else:
                mapping[pattern] = 5

    # Decode
    x = [str(mapping[output]) for output in outputs]
    decoded = int(''.join(x))
    decoded_outputs.append(decoded)

# 915941
print(sum(decoded_outputs))
