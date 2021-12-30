from itertools import product 

input_file = open("input.txt")
reboot_steps = input_file.readlines()

directions = []
x_vals = []
y_vals = []
z_vals = []

for step in reboot_steps:
    step = step.strip().split(" ")
    directions.append(step[0])
    coordinates = step[1].split(",")
    x_vals.append(coordinates[0])
    y_vals.append(coordinates[1])
    z_vals.append(coordinates[2])


def get_value_lists(raw_vals):
    cleaned_vals = []
    for n in raw_vals:
        n = n[2:]
        n = n.replace("..",",")
        n = n.split(",")
        n_0 = int(n[0])
        n_1 = int(n[1])
        if -51 < n_0 < 51 and -51 < n_1 < 51:
            cleaned_vals.append((n_0,n_1))

    result_list = []
    for item in cleaned_vals:
        n_coordinates = list(range(item[0], item[1]+1))
        result_list.extend([n_coordinates])

    return result_list


x_list = get_value_lists(x_vals)
y_list = get_value_lists(y_vals)
z_list = get_value_lists(z_vals)

 
def cartesian_product(x, y, z):
    return set(product(x, y, z))

on_cubes = set()
i=0
while i < len(x_list):
    product_set = cartesian_product(x_list[i], y_list[i], z_list[i])
    if directions[i] == 'on':
        for p_set in product_set:
            on_cubes.add(p_set)
    elif directions[i] == 'off':
        for p_set in product_set:
            if p_set in on_cubes:
                on_cubes.remove(p_set)
    i += 1

answer = len(on_cubes)
#581108
print(f'Answer is: {answer}')

   
