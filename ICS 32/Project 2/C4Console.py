import connectfour
import SharedFunctions
def user_interface():
    '''Offline version of Connectfour'''
##    turn_order = SharedFunctions.turn()

    gamestate = connectfour.new_game()
##    gamestate = gamestate._replace(turn = turn_order)
    
    while True:
        try:
            print()
            SharedFunctions.current_turn(gamestate.turn)
            SharedFunctions.print_board(gamestate.board)

            move = SharedFunctions.ask_for_move()
            col = move.split()[0]
            num = int(move.split()[-1]) - 1
            
            
            gamestate = SharedFunctions.move_type(gamestate, col, num)
            

            if SharedFunctions.victor(gamestate) == True:
                SharedFunctions.print_board(gamestate.board)
                return
        except:
            print("INVALID")
    

if __name__ == "__main__":
    user_interface()
