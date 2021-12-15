from collections import Counter


def main():
    input_file = open('input.txt', 'r')
    input_values = [line.strip() for line in input_file]

    template, rules = parse_rules_n_template(input_values)

    for i in range(0, 10):
        template = step(template, rules)

    results = Counter(template)

    min_key = min(results, key=results.get)
    max_key = max(results, key=results.get)

    answer = results[max_key] - results[min_key]
    # 2967
    print(answer)

def step(template, rules):
    to_list = list(template)
    loc = 0

    for i, char in enumerate(template):
        window_start, window_end = i - 1, i + 1
        pair = template[window_start:window_end]
        if pair in rules.keys():
            x = rules[pair]
            to_list.insert(loc, x)
            loc += 2
        else:
            loc += 1

    return ''.join(to_list)


def parse_rules_n_template(input_values):
    rules_dict = {}
    for i, input_value in enumerate(input_values):
        if input_value != '':
            if i == 0:
                template = input_value
            else:
                x = input_value.split(" -> ")
                rules_dict[x[0]] = x[1]
    return template, rules_dict


if __name__ == '__main__':
    main()
