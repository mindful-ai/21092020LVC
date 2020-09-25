import socket


def client_program():
    host = '127.0.0.1'  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    # ---------------------------------------------------------------

    # take user input
    message = input(" -> ")  

    while message.lower().strip() != 'bye':
        # send message
        client_socket.send(message.encode())

        # receive response
        data = client_socket.recv(1024).decode()
        # show in terminal
        print("From the server -> ", data)

        # Repeat
        message = input(" -> ")

    # ---------------------------------------------------------------


    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
