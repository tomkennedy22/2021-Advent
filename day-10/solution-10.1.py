input_file = open("input.txt")
values = [line for line in input_file]

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

search = []
errors = []

for line in values:
    for char in line:
        if char in pairs.keys():
            search.append(pairs[char])
        elif char == search[-1]:
            search.pop()
        else:
            errors.append(char)
            break

# Scoring
score = 0
for char in errors:
    if char == ')':
        score += 3
    if char == ']':
        score += 57
    if char == '}':
        score += 1197
    if char == '>':
        score += 25137

# Answer = 411471
print(score)
