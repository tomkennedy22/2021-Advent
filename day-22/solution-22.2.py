import ast 

input_file = open("input.txt")
reboot_steps = input_file.readlines()

directions = []
min_vertices = []
max_vertices = []

for step in reboot_steps:
    step = step.strip().split(" ")
    if step[0] == 'on':
        directions.append(1)
    else:
        directions.append(-1)
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
    
#print(directions)
#print(min_vertices)
#print(max_vertices)

def check_for_intersect(cuboid_a, cuboid_b):
    if not(cuboid_a[0] <= cuboid_b[1] and cuboid_a[1] >= cuboid_b[0]):
        return False
 
    if not(cuboid_a[2] <= cuboid_b[3] and cuboid_a[3] >= cuboid_b[2]):
        return False
 
    if not(cuboid_a[4] <= cuboid_b[5] and cuboid_a[5] >= cuboid_b[4]):
        return False
 
    return True

def create_cuboid_from_list(min_vertices_list, max_vertices_list, direction_list, i):
    min_x = min_vertices_list[i][0]
    max_x = max_vertices_list[i][0]
    min_y = min_vertices_list[i][1]
    max_y = max_vertices_list[i][1]
    min_z = min_vertices_list[i][2]
    max_z = max_vertices_list[i][2]
    direction = direction_list[i]
    return (min_x, max_x, min_y, max_y, min_z, max_z, direction)



def find_intersection_cuboid(cuboid_a, cuboid_b):
    min_x = max(cuboid_a[0], cuboid_b[0])
    max_x = min(cuboid_a[1], cuboid_b[1])
    min_y = max(cuboid_a[2], cuboid_b[2])
    max_y = min(cuboid_a[3], cuboid_b[3])
    min_z = max(cuboid_a[4], cuboid_b[4])
    max_z = min(cuboid_a[5], cuboid_b[5])

    direction = cuboid_a[6] * cuboid_b[6]

    if cuboid_a[6] == 1 and cuboid_b[6] == 1:
        direction = -1
    elif cuboid_a[6] == -1 and cuboid_b[6] == -1:
        direction = 1
    elif cuboid_a[6] == 1 and cuboid_b[6] == -1:
        direction = 1 
    
    return (min_x, max_x, min_y, max_y, min_z, max_z, direction)


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


def find_total_points(cuboid):
    x_dif = cuboid[1] - cuboid[0]
    y_dif = cuboid[3] - cuboid[2]
    z_dif = cuboid[5] - cuboid[4]
    num_points = (x_dif +1) * (y_dif+1) * (z_dif+1)
    return num_points

cuboids = []

i = 0
for i in range(0, 420):
    #print(f'i is {i}')
    current_cuboid = create_cuboid_from_list(min_vertices, max_vertices, directions, i)

    intersections = [] 

    for cuboid in cuboids:
        if check_for_intersect(current_cuboid, cuboid):
            intersection_cuboid = find_intersection_cuboid(current_cuboid, cuboid)
            intersections.append(intersection_cuboid)

    for intersection_cuboid in intersections:
        cuboids.append(intersection_cuboid)

    if directions[i] == 1:
        cuboids.append(current_cuboid)
        #print(f'cuboid list is now: {cuboids}')

    on_cube_count = 0

    for cuboid in cuboids:
        on_cube_count += find_total_points(cuboid) * cuboid[6]

print(f'Answer is: {on_cube_count}')
#Answer: 1325473814582641

