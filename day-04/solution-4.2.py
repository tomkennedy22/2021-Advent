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
    winning_cards = []
    card_positions = []
    #results = {}
    for card in bingo_matrix:
        card_position = find_card_position(card, bingo_matrix)
        for row in card:
            if count_matches(row, numbers_to_check) == 5:
                #results[card] = card_position
                winning_cards.append(card)
                card_positions.append(card_position)
                return winning_cards, card_positions
                #return results
    

def search_columns(bingo_matrix, numbers_to_check):
    winning_cards = []
    card_positions = []
    #results = {}
    for card in bingo_matrix:
        card_position = find_card_position(card, bingo_matrix)
        for column in card.T:
            if count_matches(column, numbers_to_check) == 5:
                #results[card] = card_position
                winning_cards.append(card)
                card_positions.append(card_position)
                return winning_cards, card_positions
                #return results


def get_drawn_numbers():
    input_file = open("test_input.txt")
    f_line = input_file.readline()
    drawn_numbers = f_line.strip().split(",")
    return drawn_numbers

def generate_bingo_matrix():
    input_file = open("test_input.txt")
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
    while len(bingo_matrix) > 0:        
        print(f'i is: {i}')
        print(f'bingo matrix is: {bingo_matrix}')
        print(f'winning matrix is: {winning_matrix}')
        numbers_to_check = drawn_numbers[0:i]
        print(f'checking numbers: {numbers_to_check}')
        row_search_result = search_rows(bingo_matrix, numbers_to_check)
        print(f'row search result is: {row_search_result}')
        #length_of_result = len(row_search_result[0]) 
        #print(f'length of result is {length_of_result}')
        column_search_result = search_columns(bingo_matrix, numbers_to_check)
        print(f'column search result is: {column_search_result}')
        #length_of_result = len(column_search_result[0]) 
        #print(f'length of result is {length_of_result}')
        #try:
        if row_search_result == None and column_search_result == None:
            i += 1
        else:
            if column_search_result == None:
                if row_search_result:
                    result_length = len(row_search_result)
                    print(f'length of row search result is: {result_length}')
                    if result_length == 2:
                        winning_card = row_search_result[0]
                        card_position = row_search_result[1]
                        bingo_matrix = np.delete(bingo_matrix, card_position, axis=0)
                        winning_matrix = np.append(winning_matrix, np.reshape(winning_card,(1,5,5)), axis=0)
                    elif result_length > 2:
                        for result in row_search_result:
                        #if len(row_search_result[0]) == 5:
                            #print(f'search result is {row_search_result}')
                            print(f'search result is {result}')
                            print(len(result))
                                #winning_card = row_search_result[0]
                            winning_card = result[0]
                            print(f"card {winning_card} is the winner!")
                            card_position = result[1][0]
                            print(f'card position is: {card_position}')
                            print(f"card {winning_card} is the winner!")
                                #print(np.shape(winning_card))
                            bingo_matrix = np.delete(bingo_matrix, card_position, axis=0)
                            print(f'bingo matrix after deletion is: {bingo_matrix}')
                            winning_matrix = np.append(winning_matrix, np.reshape(winning_card,(1,5,5)), axis=0)
                    i += 1
            elif column_search_result:
                result_length = len(column_search_result)
                print(f'length of row search result is: {result_length}')
                if result_length == 2:
                    winning_card = column_search_result[0]
                    card_position = column_search_result[1]
                    bingo_matrix = np.delete(bingo_matrix, card_position, axis=0)
                    winning_matrix = np.append(winning_matrix, np.reshape(winning_card,(1,5,5)), axis=0)
                elif result_length > 2:
                    for result in column_search_result:
                        print(f'search result is {result}')
                        print(len(result))
                        #if len(column_search_result[0]) == 5:
                        winning_card = result[0]
                        card_position = result[1][0]
                        print(f'card position is: {card_position}')
                        print(f"card {winning_card} is the winner!")
                        #print(np.shape(winning_card))
                        bingo_matrix = np.delete(bingo_matrix, card_position, axis=0)
                        print(f'bingo matrix after deletion is: {bingo_matrix}')
                        winning_matrix = np.append(winning_matrix, np.reshape(winning_card,(1,5,5)), axis=0)
                i += 1
                    
    print(f'winning matrix is: {winning_matrix}')
    print(f'numbers searched are: {numbers_to_check}')
    numbers_to_sum = []
    last_winning_card = winning_matrix[-1]
    for row in last_winning_card:
        for number in row:
            if number not in numbers_to_check:
                numbers_to_sum.append(int(number))
    total = sum(numbers_to_sum)
    print(f'total is: {total}')
    last_number_called = int(numbers_to_check[-1])
    print(f'last number called was: {last_number_called}')
    final_score = total * last_number_called
    return(final_score)



score = get_final_score()
print(score)



