
input_file = open("input.txt")
f_line = input_file.readline().strip().split(',')
numbers = [int(number) for number in f_line]


def model_fish(fish):
    for i, x in enumerate(fish):
        if x in (9, 8, 7, 6, 5, 4, 3, 2, 1):
            fish[i] -= 1
        elif x == 0:
            fish[i] += 6
            fish.append(9)
    return fish


days = 1
while days <= 80:
    fish = model_fish(numbers)
    print(len(fish))
    days += 1

# Answer: 371379



