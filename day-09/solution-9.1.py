# treat each line of input as a list and put the lists into a tuple
# number the lists 
# write loop that does: 
# for each number check the list elements before and after it, and check the lists above and below on the same index
# if all of those numbers are greater than the number, add it to a list of low points

input_file = open('test_input.txt', 'r')
#input_values = [list(line.strip().split()) for line in input_file]
input_values= [list(line.strip()) for line in input_file]

for sequence in input_values:
    for i in range(0, len(sequence)):
        sequence[i] = int(sequence[i])

i = 0
for sequence in input_values:
    for item in sequence:
        print(item)
       
    #for item in sequence:
            #print(item)
            
def compare_horizontal_neighbors(lst):
    for i, x in enumerate(lst):
        if x - lst[i-1] > 0 and x - lst[i+1] < 0:
            return True

def compare_vertical_neighbors(current_list, list_above, list_below):
    result = [c < b and c < a for c, b, a in zip(current_list, list_below, list_above)]
    return result

def find_vertical_neighbors():
    return True


vertical_result = compare_vertical_neighbors(input_values[2], input_values[1], input_values[3])
print(vertical_result)
#>>> a = [0, 4, 10, 100]

# basic enumerate without condition:
#>>> [x - a[i - 1] for i, x in enumerate(a)][1:]
#[4, 6, 90]

# enumerate with conditional inside the list comprehension:
#>>> [x - a[i - 1] for i, x in enumerate(a) if i > 0]
#[4, 6, 90]

# the zip version seems more concise and elegant:
#>>> [t - s for s, t in zip(a, a[1:])]
#[4, 6, 90]






#lists = input_values
#print(input_lists)
