from itertools import product 
import ast 

input_file = open("sample_input.txt")
reboot_steps = input_file.readlines()

directions = []
min_vertices = []
max_vertices = []

for step in reboot_steps:
    step = step.strip().split(" ")
    directions.append(step[0])
    coordinates = step[1].split(',')
    points = []
    for c in coordinates:
        c = c.strip('x=').strip('y=').strip('z=')
        c = c.replace('..', ',')
        c = ast.literal_eval(c)
        points.append(c)
    min_points = []
    max_points = []
    for point in points:
        min_val = min(point)
        min_points.append(min_val)
    for point in points:
        max_val = max(point)
        max_points.append(max_val)
    min_vertices.append(min_points)
    max_vertices.append(max_points)
print(min_vertices)
print(max_vertices)
print(directions)

    
def find_total_points(max_vertex, min_vertex):
    x_dif = max_vertex[0] - min_vertex[0]
    y_dif = max_vertex[1] - min_vertex[1]
    z_dif = max_vertex[2] - min_vertex[2]
    num_points = (x_dif +1) * (y_dif+1) * (z_dif+1)
    return num_points

def find_line_overlap(max_vertex_a, min_vertex_a, max_vertex_b, min_vertex_b, line):
    if line == 'x':
        i = 0 
    elif line == 'y':
        i = 1
    elif line == 'z':
        i = 2
    calc = min(max_vertex_a[i], max_vertex_b[i]) - max(min_vertex_a[i], min_vertex_b[i])
    return calc


def find_points_overlap(line_overlap):
    if line_overlap < 0:
        points_overlap = 0
    else:
        points_overlap = line_overlap + 1
    return points_overlap

def find_volume_overlap(*args): #the args should be the x, y, and z line overlaps
    volume = 1
    for a in args:
        if a != 0:
            volume *= a
    return volume

# 1. using only the points given, find volume inclusive of points (10, 10, 10) (12, 12, 12)
# 2. using only points given (not range), find vertices 
# volume = # of cubes turned on / off
# 3. find volume of next cube and vertices of next cube (11, 11, 11) (13, 13, 13)
# find overlap of x line, y line, and z line from all pervious cuboids
# multiply those to find volume of overlap
# number on - overlap = how many new cubes get turned on or off
# add number of cubes now on or off to total
# continue 


on_cube_count = 0
i = 0
for i in range(0, len(directions)):
    if directions[i] == 'on':
        cuboid_points = find_total_points(max_vertices[i], min_vertices[i])
        x_overlap = find_line_overlap()
        on_cube_count += cuboid_points

    


   






