def median(data_list):
    data_list.sort()
    mid = len(data_list) // 2
    return (data_list[mid] + data_list[~mid]) / 2


input_file = open("input.txt")
values = [line for line in input_file]

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

errors = []
autocompletions = []

for line in values:
    search = []
    for char in line:
        if char in pairs.keys():
            search.append(pairs[char])
        elif char == search[-1]:
            search.pop()
        elif char == '\n':
            search.reverse()
            autocompletions.append(search)
        else:
            errors.append(char)
            break


# Scoring
scores = []
for line in autocompletions:
    score = 0
    for char in line:
        if char == ')':
            score = 5 * score + 1
        if char == ']':
            score = 5 * score + 2
        if char == '}':
            score = 5 * score + 3
        if char == '>':
            score = 5 * score + 4

    scores.append(score)

# Solution = 3122628974
print(int(median(scores)))
