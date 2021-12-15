from collections import Counter


def main():
    input_file = open('input.txt', 'r')
    input_values = [line.strip() for line in input_file]

    template, rules = parse_rules_n_template(input_values)

    results = Counter(template)
    pairs = Counter([x + y for x, y in zip(list(template), list(template[1:]))])

    for i in range(40):
        for pair, count in pairs.copy().items():
            pair_first, pair_second = pair[0], pair[-1]
            chars, to_insert = update_chars(rules, pair, results, count)
            update_counts(pairs, pair_first, pair_second, count, to_insert)

    min_key = min(results, key=results.get)
    max_key = max(results, key=results.get)

    answer = results[max_key] - results[min_key]
    # 3692219987038
    print(answer)


def update_chars(rules, pair, chars, count):
    to_insert = rules[pair]
    chars[to_insert] += count
    return chars, to_insert


def update_counts(pairs, pair_first, pair_second, count, to_insert):
    pairs[pair_first + to_insert] += count
    pairs[to_insert + pair_second] += count
    pairs[pair_first + pair_second] -= count
    return pairs


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
