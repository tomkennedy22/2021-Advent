import datetime
import json
start_time = datetime.datetime.now()

import functools
from itertools import permutations

input_file = open("input.txt")
input_lines = [eval(line) for line in input_file]


def add_left(a, b):
    if not b:
        return a
    if type(a) == int:
        return a + b
    return [add_left(a[0], b), a[1]]


def add_right(a, b):
    if not b:
        return a
    if type(a) == int:
        return a + b
    return [a[0], add_right(a[1], b)]


def explode_pair(x, layer):
    print('x', type(x), x)
    if type(x) == int:
        return False, x, 0, 0
    left, right = x
    if layer == 4:
        return True, 0, left, right
    exploded, nxt, l, r = explode_pair(left, layer+1)
    if exploded:
        return True, [nxt, add_left(right, r)], l, 0
    exploded, nxt, l, r = explode_pair(right, layer+1)
    if exploded:
        return True, [add_right(left, l), nxt], 0, r
    return False, x, 0, 0


def split_num(x):
    if type(x) == int:
        if x > 9:
            return [x // 2, x // 2 + (x & 1)]
        return x
    l, r = x
    left = split_num(l)
    if left != l:
        return [left, r]
    return [l, split_num(r)]


def add_snails(a, b):
    res = [a, b]
    while True:
        exploded, res, _, _ = explode_pair(res, 0)
        if not exploded:
            prev = res
            res = split_num(res)
            if res == prev:
                return res


def magnitude(x):
    if type(x) == int:
        return x
    return 3 * magnitude(x[0]) + 2 * magnitude(x[1])


cur = input_lines[0]
for line in input_lines[1:]:
    cur = add_snails(cur, line)
mag_result = magnitude(cur)





dash_line = f'{"-"*60}'
print(dash_line)
print(f'res: *** {mag_result} ***')

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms'  )
print(dash_line)
