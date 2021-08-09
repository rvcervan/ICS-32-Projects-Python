import connectfour

def print_board(board: [[int]]):
    '''Prints the board of connectfour'''
    for i in range(1, connectfour.BOARD_COLUMNS + 1):
        print(i, end = ' ')
    print()
        
    for row in range(connectfour.BOARD_ROWS):
        for column in range(connectfour.BOARD_COLUMNS):
            if board[column][row] == 0:
                print(". ", end = '')
            elif board[column][row] == 1:
                print("R ", end = '')
            elif board[column][row] == 2:
                print("Y ", end = '')
        print()


def move_type(gamestate: tuple, col: str, num: int):
    '''Drops or pops for player'''
    while True:
##        move = input("Drop or Pop which column?")
##        col = move.split()[0]
##        num = int(move.split()[-1]) - 1
        
        if col.upper() == "DROP":
            gamestate = connectfour.drop(gamestate, num)
            return gamestate
        elif col.upper() == "POP":
            gamestate = connectfour.pop(gamestate, num)
            return gamestate
        else:
            print("INVALID")
            print()
            current_turn(gamestate.turn)
            print_board(gamestate.board)
            


def turn() -> int:
    '''determines turn order'''
    while True:
        turn = input("Who goes first? R or Y?")
        if turn.upper() == "R":
            turn = 1
            print("Red goes first.")
            return turn
        elif turn.upper() == "Y":
            print("Yellow goes first.")
            turn = 2
            return turn
        else:
            print("Enter a valid option")
            print()


def current_turn(player: int):
    '''return who's turn it is'''
    if player == 1:
        print("RED TURN")
    else:
        print("YELLOW TURN")


def victor(gamestate: tuple):
    '''announces victor and ends game'''
    win = False
    
    if connectfour.winner(gamestate) == 1:
        print()
        print("RED IS WINNER")
        win = True
        return win
    elif connectfour.winner(gamestate) == 2:
        print()
        print("YELLOW IS WINNER")
        win = True
        return win
    else:
        return win


def ask_for_move():
    '''Asks for drop or pop'''
    move = input("Player Move (EX: Drop 3, Pop 5): ")
    
    if move.split()[0].upper() == 'DROP':
        return move
    elif move.split()[0].upper() == 'POP':
        return move
    else:
        move
