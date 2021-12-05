import numpy as np

def count_matches(list_to_search, list_to_check):
    match_count = 0
    for item in list_to_search:
        if item in list_to_check:
            match_count += 1
    return match_count

def search_rows(bingo_matrix, numbers_to_check):
    for card in bingo_matrix:
        for row in card:
            if count_matches(row, numbers_to_check) == 5:
                winning_card = card
                return winning_card
    

def search_columns(bingo_matrix, numbers_to_check):
    for card in bingo_matrix:
        for column in card.T:
            if count_matches(column, numbers_to_check) == 5:
                winning_card = card
                return winning_card


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



def find_winning_card():
    bingo_matrix = generate_bingo_matrix()
    drawn_numbers = get_drawn_numbers()
    i = 5
    while i < len(drawn_numbers):
        numbers_to_check = drawn_numbers[0:i]
        row_search_result = search_rows(bingo_matrix, numbers_to_check)
        column_search_result = search_columns(bingo_matrix, numbers_to_check)
        try:
            if row_search_result == None and column_search_result == None:
                i += 1
        except:
            try:
                if len(row_search_result) == 5:
                    winning_card = row_search_result
                    print(f"card {winning_card} is the winner!")
                    break
            except:
                if len(column_search_result) == 5:
                    winning_card = column_search_result
                    print(f"card {winning_card} is the winner!")
                    break
                    
    
    numbers_to_sum = []
    for row in winning_card:
        for number in row:
            if number not in numbers_to_check:
                numbers_to_sum.append(int(number))
    
    total = sum(numbers_to_sum)
    last_number_called = int(numbers_to_check[-1])
    final_score = total * last_number_called
    return(final_score)
   

score = find_winning_card()
# My Solution: 8580
print(score)

