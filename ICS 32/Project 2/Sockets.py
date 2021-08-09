import socket

def connect(host: str, port: int):
    '''connects to the specified address'''

    connect_address = (host, port)

    the_socket = socket.socket()
    the_socket.connect(connect_address)

    socket_input = the_socket.makefile('r')
    socket_output = the_socket.makefile('w')

    return the_socket, socket_input, socket_output

def connect_for_cf() -> 'connection':
    while True:
        try:

            host = get_host()
            port = get_port()
            
            print('Connecting to {} (port {})...'.format(host, port))
            connection = connect(host, port)
            print('Connected!')

            return connection
        except:
            print("Connection Failed. Try Again.")

def get_host() -> str:
    '''gets the ip address'''
    
    while True:
        host = input("Host: ").strip()

        if host == '':
            print('Please specify a host')
        else:
            return host

def get_port() -> int:
    '''gets the port'''
    
    while True:
        try:
            port = int(input("Port: ").strip())

            if port < 0 or port > 65535:
                print("Ports must be an integer between 0 and 65535")
            else:
                return port
        except ValueError:
            print('Ports must be an integer between 0 and 65535')

def read_message() -> str:
    '''ask user what message they would like to send'''

    return input("Player Move: ")



#################################


def read_username() -> str:
    '''ask user for username they would like to send'''
    
    user  = input("Username: ")
    
    return "I32CFSP_HELLO " + user

def play_game() -> str:
    '''plays CF game by returning AI_GAME'''
    return 'AI_GAME'



##################################



def print_response(response: str) -> None:
    '''Prints the response sent back from the server'''

    print("Response: " + response)

def close(connection: 'connection') -> None:
    '''Close connection'''

    the_socket, socket_input, socket_output = connection

    the_socket.close()
    socket_input.close()
    socket_output.close()

def send_message(connection: 'connection', message: str) -> None:
    '''
    Sends a message to the server via a connection that is assumed
    to be open
    '''

    the_socket, socket_input, socket_output = connection

    socket_output.write(message + '\r\n')
    socket_output.flush()

def receive_response(connection: 'connection') -> None:
    '''Receives a response from the server via connection'''

    the_socket, socket_input, socket_output = connection

    return socket_input.readline()[:-1]
















        
