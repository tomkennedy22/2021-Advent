import math

def generate_circular_array(lst, len, start, repeat):
    i = start
    c_array = []

    while i < len + start :
        c_array.append(lst[(i % len)])
        i = i + 1

    return c_array*repeat

def determine_repeat(moves):
    if moves % 10 != 0:
        return int(math.ceil(moves / 10.0))+1
    else:
        return int(moves / 10)+1
        

def take_turn(player_start, last_roll):
    deterministic_die = generate_circular_array(die_lst, len(die_lst), last_roll, 1)
    player_moves = sum(deterministic_die[0:2+1])
    player_positions = generate_circular_array(position_list, len(position_list), player_start-1, determine_repeat(player_moves))
    player_score = player_positions[player_moves]
    last_roll = deterministic_die[2]
    start_position = player_positions[player_moves]
    return (player_score, last_roll, start_position)

player_1_start = 2
player_2_start = 1

position_list = list(range(1,10+1))
die_lst = list(range(1,100+1))

turn = 1
last_roll = 0
player_1_score = []
player_2_score = []

while sum(player_1_score) < 1000 and sum(player_2_score) < 1000:
    (player_1_turn, last_roll, player_1_start_position) = take_turn(player_1_start, last_roll)
    player_1_score.append(player_1_turn)
    if sum(player_1_score) >= 1000 or sum(player_2_score) >= 1000:
        break 
    else:
        turn += 1
        (player_2_turn, last_roll, player_2_start_position) = take_turn(player_2_start, last_roll)
        player_2_score.append(player_2_turn)
        if sum(player_1_score) >= 1000 or sum(player_2_score) >= 1000:
            break 
        else:
            turn += 1
            player_1_start = player_1_start_position 
            player_2_start = player_2_start_position


final_player_1_score = sum(player_1_score)
final_player_2_score = sum(player_2_score)
losing_score = min(final_player_1_score, final_player_2_score)
final_die_rolls = turn*3
answer = losing_score*final_die_rolls
#Answer: 797160
print(f"Answer is: {answer}")