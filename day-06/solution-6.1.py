import datetime
start_time = datetime.datetime.now()

input_file = open("input.txt")
f_line = input_file.readline().strip().split(',')
numbers = [int(number) for number in f_line]


def model_fish(fish):
    for i, x in enumerate(fish):
        if x > 0:
            fish[i] -= 1
        else:
            fish[i] += 6
            fish.append(9)
    return fish


days = 1
for day in range(1, 80 + 1):
    fish = model_fish(numbers)

# Answer: 371379
print(f'{"-"*60}\nNumber of fish on final day: *** {len(fish)} ***')

end_time = datetime.datetime.now()
print(f'\tExecution time: {int((end_time - start_time).total_seconds() * 1000)}ms\n{"-"*60}'  )
