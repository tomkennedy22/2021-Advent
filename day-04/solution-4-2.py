BOARD_DIAMETER = 5

class Board:

    def __init__(self, id):

        self.id = id
        self.board_won = False
        self.board_values = []
        self.all_values = set()
        self.seen_values = set()
        self.unseen_values = set()

    def add_row(self, input_line):

        values = [int(val) for val in input_line.split(' ') if len(val) > 0]
        self.board_values.append(values)

        for value in values:
            self.all_values.add(value)
            self.unseen_values.add(value)

    def filled_board(self):

        self.possible_sets = []

        for x in range(0, BOARD_DIAMETER):
            self.possible_sets.append( set( [self.board_values[x][y] for y in range(0, BOARD_DIAMETER)] ) )
            self.possible_sets.append( set( [self.board_values[y][x] for y in range(0, BOARD_DIAMETER)] ) )


    def value_called(self, val):
        if val in self.unseen_values:
            self.seen_values.add(val)
            self.unseen_values.remove(val)

            return self.check_board()

        return False


    def check_board(self):

        if len(self.seen_values) < BOARD_DIAMETER:
            return False

        for possible_set in self.possible_sets:
            if possible_set.issubset(self.seen_values):
                self.board_won = True
                return True

        return False

    def __repr__(self):

        s = ''
        for row in self.board_values:
            s += ''.join([' '*(3-len(str(val))) + str(val) for val in row]) + '\n'

        return s


def process_called_values():
    input_file = open('input.txt', 'r')
    input_lines = [line for line in input_file]

    called_values = []
    board = None

    boards = []
    completed_boards = set()

    for ind, input_line in enumerate(input_lines):
        if (ind == 0):
            called_values = [int(val) for val in input_line.split(',')]

        elif ((ind % 6) == 1):
            if board is not None:
                board.filled_board()
                boards.append(board)

            board = Board(len(boards))

        else:
            board.add_row(input_line)

    for called_value in called_values:
        for board in boards:
            if board.id in completed_boards:
                continue

            if board.value_called(called_value):
                completed_boards.add(board.id)

                if len(completed_boards) == len(boards):
                    return called_value * sum(board.unseen_values)





print('Resulting value:', process_called_values())
