from math import prod

input_file = open("input.txt")
hex_data = input_file.readline().strip()
h_size = len(hex_data) * 4
binary_string = ( bin(int(hex_data, 16))[2:] ).zfill(h_size)

i = 0

def evaluate_recursive(binary_string):
    global i
    print(f'i is {i}')
    packet_type = binary_string[i+3:i+6]
    packets = []
    len_id = binary_string[i+6:i+7]

    #base case
    if packet_type == '100':
        literals = []
        x = i+6
        x1 = i+11
        literal_sequence = binary_string[x:x1]
        while binary_string[x] != '0':
            literal_sequence = binary_string[x:x1]
            num_bits = binary_string[x+1:x1]
            literals.append(num_bits)
            x = x1
            x1 += 5
            next_sequence_starts_at = x
        if binary_string[x] == '0':
            last_literal_sequence = binary_string[x:x1]
            num_bits = binary_string[x+1:x1]
            literals.append(num_bits)
            if any(c in binary_string[x1:] for c in '1'):
                next_starting_position = x1
                i = next_starting_position
            else:
                i = len(binary_string) #?
                return int("".join(literals), 2)
        return int("".join(literals), 2)

    #recursive case
    
    if len_id == '0':
        total_length_of_subpackets = binary_string[i+7:i+21+1]
        length_as_num = int(total_length_of_subpackets, 2)
        next_starting_position = i+22
        end_position = next_starting_position + length_as_num
        i = next_starting_position
        while i <= end_position:
            packets.append(evaluate_recursive(binary_string))
            print(packets)

    else: 
        total_number_of_subpackets = binary_string[i+7:i+17+1]
        num_as_num = int(total_number_of_subpackets, 2)
        next_starting_position = i+18
        i = next_starting_position
        for n in range(num_as_num):
           packets.append(evaluate_recursive(binary_string))
           print(packets)
        

    if packet_type == '000':
        return sum(packets)
    elif packet_type == '001':
        return prod(packets)
    elif packet_type == '010':
        return min(packets)
    elif packet_type == '011':
        return max(packets)
    elif packet_type == '101':
        return int(packets[0] > packets[1])
    elif packet_type == '110':
        return int(packets[0] < packets[1])
    elif packet_type == '111':
        return int(packets[0] == packets[1])

answer = evaluate_recursive(binary_string)
print(f'Answer is: {answer}')

#answer might be 2975066198