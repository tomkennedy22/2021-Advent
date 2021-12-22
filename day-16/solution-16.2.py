import datetime
start_time = datetime.datetime.now()


class Bit_Input:
  def __init__(self, bit_input):
    self.bit_input = bit_input
    self.slice_index = 0

  def slice(self, bit_read_count):
    bit_read_end = self.slice_index + bit_read_count
    # print('\nSlicing', self.slice_index, bit_read_end, bit_read_count , len(self.bit_input) )
    # print(f'{" "*self.slice_index }[{" "* (bit_read_count-1)})')
    # print(self.bit_input)

    raw_bits = self.bit_input[self.slice_index:bit_read_end]
    #print(f'raw_bits: [{raw_bits}]')
    self.slice_index = bit_read_end


    return int(raw_bits, 2)

#My python versioning is messed up, math.prod doesn't exist in 3.7 and I'm having dependency issues. This is a placeholder for the function
def prod(arr):
    product = 1
    for elem in arr:
        product *= elem

    return product

def evaluate_value(subpackets, packet_type):
    if packet_type == 0:
        return sum(subpackets)
    elif packet_type == 1:
        return prod(subpackets)
    elif packet_type == 2:
        return min(subpackets)
    elif packet_type == 3:
        return max(subpackets)
    elif packet_type == 5:
        return 1 if subpackets[0]>subpackets[1] else 0
    elif packet_type == 6:
        return 1 if subpackets[0]<subpackets[1] else 0
    elif packet_type == 7:
        return 1 if subpackets[0]==subpackets[1] else 0
    else:
        return 0


def find_bits(bit_input):
  packet_version = bit_input.slice(3)
  packet_type  = bit_input.slice(3)

  if packet_type == 4:
    val = 0
    while True:
      len_type = bit_input.slice(1)
      val = val * 16 + bit_input.slice(4)
      if len_type == 0:
          return val

  subpackets = []
  bit_slice_type = bit_input.slice(1)
  #print('bit_slice', bit_slice)
  if bit_slice_type == 1:
    #print('in if')
    for u in range(0, bit_input.slice(11)):
      subpackets.append(find_bits(bit_input))
  else:
    #print('in else')
    bit_len = bit_input.slice(15)
    end_index = bit_input.slice_index + bit_len
    while bit_input.slice_index < end_index:
      subpackets.append(find_bits(bit_input))

  return evaluate_value(subpackets, packet_type)

dash_line = f'{"-"*60}'
print(dash_line)

test_inputs = [
    ['C200B40A82', 3],
    ['04005AC33890', 54],
    ['880086C3E88112', 7],
    ['CE00C43D881120', 9],
    ['D8005AC2A8F0', 1],
    ['F600BC2D8F', 0],
    ['9C005AC2F8F0', 0],
    ['9C0141080250320F1802104A08', 1],
    [open("input.txt").readline().strip(), 'Live result!'],
]
for test_input in test_inputs:
    input_val = test_input[0]
    input_val = bin(int(input_val, 16))[2:]
    input_val_leading = input_val.zfill(len(test_input[0])*4)

    BI = Bit_Input(input_val_leading)

    print(f'Bit result & expected: *** {find_bits(BI)}, {test_input[1]} ***')

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms'  )
print(dash_line)
