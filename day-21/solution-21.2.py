from functools import lru_cache

player_1_start_position = 2
player_2_start_position = 1


@lru_cache(maxsize=None)
def take_turn_recursive(player_1_position, player_2_position, player_1_score, player_2_score, which_player_turn):
    win_count = [0, 0]

    if player_1_score >= 21:
        return 1, 0
    elif player_2_score >= 21:
        return 0, 1

   

    for roll_1 in [1, 2, 3]:
        for roll_2 in [1, 2, 3]:
            for roll_3 in [1, 2, 3]:
                moves = sum([roll_1, roll_2, roll_3])
                if which_player_turn == 1:
                    new_player_1_position = ((player_1_position - 1 + moves) % 10) +1
                    new_player_1_score = player_1_score + new_player_1_position
                    player_1_wins, player_2_wins = take_turn_recursive(new_player_1_position, player_2_position, new_player_1_score, player_2_score, 2)

                else:
                    new_player_2_position = ((player_2_position - 1 + moves) % 10) +1
                    new_player_2_score = player_2_score + new_player_2_position
                    player_1_wins, player_2_wins = take_turn_recursive(player_1_position, new_player_2_position, player_1_score, new_player_2_score, 1)


                win_count[0] += player_1_wins
                win_count[1] += player_2_wins 
                    
    return win_count
        

win_count = take_turn_recursive(player_1_start_position, player_2_start_position, 0, 0, 1)
answer = max(win_count)
#answer: 27464148626406
print(f'Answer is {answer}')
                






