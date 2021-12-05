import numpy as np

def count_matches(list_to_search, list_to_check):
    match_count = 0
    for item in list_to_search:
        if item in list_to_check:
            match_count += 1
    return match_count

def find_card_position(card, bingo_matrix):
    lst = card.tolist()
    list_matrix = bingo_matrix.tolist()
    position_of_card = list_matrix.index(lst)
    return position_of_card

def search_rows(bingo_matrix, numbers_to_check):
    winning_sets = []
    card_positions = set()

    for card in bingo_matrix:
        card_position = find_card_position(card, bingo_matrix)
        for row in card:
            if count_matches(row, numbers_to_check) == 5:
                if card_position not in card_positions:
                    winning_sets.append((card, card_position))
                    card_positions.add(card_position)

    return sorted(winning_sets, key = lambda s: s[1], reverse= True)


def search_columns(bingo_matrix, numbers_to_check):
    winning_sets = []
    card_positions = set()

    for card in bingo_matrix:
        card_position = find_card_position(card, bingo_matrix)
        for column in card.T:
            if count_matches(column, numbers_to_check) == 5:
                if card_position not in card_positions:
                    winning_sets.append((card, card_position))
                    card_positions.add(card_position)

    return sorted(winning_sets, key = lambda s: s[1], reverse= True)


def get_drawn_numbers():
    input_file = open("input.txt")
    f_line = input_file.readline()
    drawn_numbers = f_line.strip().split(",")
    return drawn_numbers

def generate_bingo_matrix():
    input_file = open("input.txt")
    bingo_lines = input_file.readlines()[1:]

    clean_bingo_lines = []

    for line in bingo_lines:
        clean_bingo_lines.append(line.strip().split())

    filtered_bingo_lines = list(filter(None, clean_bingo_lines))

    grouped_lines = [filtered_bingo_lines[x:x+5] for x in range(0, len(filtered_bingo_lines), 5)]

    bingo_matrix = np.array(grouped_lines)
    return bingo_matrix

def generate_winning_matrix():
    winning_matrix = np.zeros((1, 5, 5))
    return winning_matrix

def get_final_score():
    drawn_numbers = get_drawn_numbers()
    winning_matrix = generate_winning_matrix()

    bingo_matrix = generate_bingo_matrix()
    i = 5
    while len(bingo_matrix) > 0 and i < len(drawn_numbers):
        numbers_to_check = drawn_numbers[0:i]
        print('Calling value', numbers_to_check[-1])

        row_search_result = search_rows(bingo_matrix, numbers_to_check)
        #print('processing N columns', len(row_search_result))
        for winning_row in row_search_result:
            winning_card = winning_row[0]
            card_position = winning_row[1]
            #print('removing card at card_position', card_position, len(bingo_matrix))
            bingo_matrix = np.delete(bingo_matrix, card_position, axis=0)
            #print('adding winning_card', winning_card)
            winning_matrix = np.append(winning_matrix, np.reshape(winning_card,(1,5,5)), axis=0)

        column_search_result = search_columns(bingo_matrix, numbers_to_check)
        #print('processing N columns', len(column_search_result))
        for winning_column in column_search_result:
            winning_card = winning_column[0]
            card_position = winning_column[1]
            #print('removing card at card_position', card_position, len(bingo_matrix))
            bingo_matrix = np.delete(bingo_matrix, card_position, axis=0)
            #print('adding winning_card', winning_card)
            winning_matrix = np.append(winning_matrix, np.reshape(winning_card,(1,5,5)), axis=0)


        i +=1

    numbers_to_sum = []
    last_winning_card = winning_matrix[-1]
    for row in last_winning_card:
        for number in row:
            if number not in numbers_to_check:
                numbers_to_sum.append(int(number))
    total = sum(numbers_to_sum)
    last_number_called = int(numbers_to_check[-1])
    final_score = total * last_number_called
    print(f'Final Number Called: {last_number_called}, Total Unseen numbers: {total}, Final Score: {final_score}')

    return(final_score)


score = get_final_score()
