import Sockets
import connectfour
import SharedFunctions



def move_error(connection: 'connection'):
    while True:
        move = SharedFunctions.ask_for_move()
        number = move.split()
        
        if int(number[-1]) > 7 or int(number[-1]) < 1:
            
            Sockets.send_message(connection, move.upper())
            
            response = Sockets.receive_response(connection)
            state = Sockets.receive_response(connection)
            
            Sockets.print_response(response)
            Sockets.print_response(state)
            
        else:
            return move.upper()
        

def user_interface():
    '''Online version of C4'''
    
    connection = Sockets.connect_for_cf()
    
    username = Sockets.read_username()
    Sockets.send_message(connection, username)
    response = Sockets.receive_response(connection)
    Sockets.print_response(response)

    Sockets.send_message(connection, Sockets.play_game())
    response = Sockets.receive_response(connection)
    Sockets.print_response(response)

    gamestate = connectfour.new_game()
    SharedFunctions.print_board(gamestate.board)
    print()

    while True:

        try:

            if connectfour.winner(gamestate) == 1:
                won = Sockets.receive_response(connection)
                Sockets.print_response(won)
                Sockets.close(connection)
                return

            message = move_error(connection)
            
            col = message.split()[0].upper()
            num = int(message.split()[-1]) - 1

            gamestate = SharedFunctions.move_type(gamestate, col, num)
            SharedFunctions.print_board(gamestate.board)
            print()

            
            Sockets.send_message(connection, message)

            if connectfour.winner(gamestate) == 1:
                won = Sockets.receive_response(connection)
                Sockets.print_response(won)
                Sockets.close(connection)
                return
            
            accept = Sockets.receive_response(connection)
            move = Sockets.receive_response(connection)
            Sockets.print_response(accept)
            Sockets.print_response(move)
            state = Sockets.receive_response(connection)
            


            COL = move.split()[0].upper()
            NUM = int(move.split()[-1]) - 1

            gamestate = SharedFunctions.move_type(gamestate, COL, NUM)
            SharedFunctions.print_board(gamestate.board)


            Sockets.print_response(state)
            if connectfour.winner(gamestate) == 2:
                Sockets.close(connection)
                return
            print()
        except:
            print("INVALID")



if __name__ == "__main__":
    user_interface()
