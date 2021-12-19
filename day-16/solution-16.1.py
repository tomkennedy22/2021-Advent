input_file = open("input.txt")
hex_data = input_file.readline().strip()
h_size = len(hex_data) * 4
binary_data = ( bin(int(hex_data, 16))[2:] ).zfill(h_size)

version_list = []
i = 0
while i < len(binary_data):
    version = binary_data[i:i+3]
    hex_version = format(int(version, 2), 'x')
    version_list.append(hex_version)
    packet_type = binary_data[i+3:i+6]
    if packet_type == '100':
        x = i+6
        x1 = i+11
        literal_sequence = binary_data[x:x1]
        while binary_data[x] != '0':
            literal_sequence = binary_data[x:x1]
            x = x1
            x1 += 5
            next_sequence_starts_at = x
        if binary_data[x] == '0':
            last_literal_sequence = binary_data[x:x1]
            if any(c in binary_data[x1:] for c in '1'):
                next_starting_position = x1
                i = next_starting_position
            else:
                i = len(binary_data)
    else:
        len_id = binary_data[i+6:i+7]
        if len_id == '0':
            total_length_of_subpackets = binary_data[i+7:i+21]
            next_starting_position = i+22
            i = next_starting_position
        else: 
            total_number_of_subpackets = binary_data[i+7:i+17]
            next_starting_position = i+18
            i = next_starting_position

version_total = sum(map(int, version_list))
#Answer: 917
print(f'Sum of version numbers is: {version_total}')