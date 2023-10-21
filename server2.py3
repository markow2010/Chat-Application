import socket
import sys

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 6543 

    s_socket = socket.socket()  
    s_socket.bind((host, port))  

    s_socket.listen(2)
    connection, address = s_socket.accept()  
    print("Connection from: " + str(address))
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        connection.send(data.encode())  

    connection.close()  


if __name__ == '__main__':
    server_program()