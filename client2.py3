import socket
import sys

def client_program():
    host = socket.gethostname()
    port = 6543

    c_socket = socket.socket()
    c_socket.connect((host, port))
    message = input(" -> ")

    while message.lower().strip() != 'bye':
        c_socket.send(message.encode())
        data = c_socket.recv(1024).decode()
        print('Received from server: ' + data)
        message = input(" -> ")
    c_socket.close()

if __name__ == '__main__':
    client_program()