import mechanics
def user_interface():
    '''plays faller'''
    rows = int(input())
    cols = int(input())
    gamemode = input()

    if gamemode.upper() == 'EMPTY':
        board = empty_gameboard(rows, cols)
        game = mechanics.Game(board, rows, cols)
        print_board(game.board(), rows, cols)

    elif gamemode.upper() == 'CONTENTS':
        board = preset_gameboard(rows, cols)
        game = mechanics.Game(board, rows, cols)
        game.fill_empty_space()
        game.replace_matching()

        print_board(game.board(), rows, cols)
        game.delete_matching()
        if game.full_board() == 0:
            print('GAME OVER')
            return
    while True:


        user = input()
        if user == '':


            if game.board_conditions() == 0:
                if game.star_checker() == 0:
                    game.fill_empty_space()
                    game.replace_matching()
                    print_board(game.board(), rows, cols)
                else:
                    game.delete_matching()
                    game.fill_empty_space()
                    game.replace_matching()
                    print_board(game.board(), rows, cols)
            elif game.board_conditions() == 3:
                game.falling()
                game.freeze_faller()
                print_board(game.board(), rows, cols)
            elif game.board_conditions() == 6:
                game.frozen_faller()
                game.replace_matching()
                print_board(game.board(), rows, cols)
                if game.full_board() == 0:
                    print('GAME OVER')
                    return
        elif user[0].upper() == 'F':
            if int(user[2]) <= cols:
                if game.place_faller_cond() == True:
                    faller = create_faller(user)
                    if game.obstructing_jewel(int(user[2])) == True:

                        game.new_faller(faller)
                        game.drop_faller(int(user[2]))
                        game.freeze_faller()

                print_board(game.board(), rows, cols)
        elif user == 'R':
            game.rotate()

            print_board(game.board(), rows, cols)
        elif user == '>':
            game.move_right()
            game.unfreeze_faller()
            game.freeze_faller()


            print_board(game.board(), rows, cols)
        elif user == '<':
            game.move_left() 
            game.unfreeze_faller()
            game.freeze_faller() 

            print_board(game.board(), rows, cols)
        elif user == 'Q':
            return
        if game.board_checker() == True:
            if game.end_game() == True:
                print('GAME OVER')
                return



def empty_gameboard(rows: int, cols: int):
    '''creates empty gameboard'''
    board = []

    for i in range(rows + 2):
        row = []
        for x in range(cols):
            row.append('   ')
        board.append(row)

    return board


def preset_gameboard(rows: int, cols: int):
    '''Creates a preset gameboard that contains jewels inputted'''
    board = []
    jaws = ['S', 'T', 'V', 'W', 'X', 'Y', 'Z']


    for i in range(2):
        empty_row = []
        for x in range(cols):
            empty_row.append('   ')
        board.append(empty_row)

    for i in range(rows):
        row = []
        jewels = input()
        jewels = jewels[:cols]
        jewels = jewels.split(',')

        for list_of_char in jewels:
            for char in list_of_char:
                if char.upper() in jaws:
                    row.append(' ' + char.upper() + ' ')
                else:
                    row.append('   ')
        board.append(row)

    return board

def create_faller(faller: str):

    '''creates a faller for the game'''
    jewels = ['S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    faller = faller[4:]
    faller_list = []
    faller = faller.replace(' ', '')
    for char in faller:
        if char.upper() in jewels:
            faller_list.append('[{}]'.format(char.upper()))
        else:
            faller_list.append('[ ]')

    return faller_list

def print_board(board: list, row, col):
    '''prints the fully designed gameboard'''
    row = row + 2
    for y in range(2, row):
        print('|', end = '')
        for x in range(col):
            print(board[y][x], end = '')
        print('|', end = '')
        print()
    print(' ' + col * '---' + ' ')



if __name__ == "__main__":
    user_interface()
