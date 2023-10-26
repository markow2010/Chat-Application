# Chat-Application

# Socket Communication 

This repository contains two Python scripts for setting up a simple client-server communication using sockets. The client can send messages to the server, which responds to the messages. Additionally, the server can save the received messages to a log file.

## Client

### Usage

To run the client script, execute it with the following command-line arguments:

python3 client.py -s <ip> -p <port> -l <logfile>


- `<ip>`: The IP address of the server.
- `<port>`: The port number the server is listening on.
- `<logfile>`: The name of the log file to save received messages.

### Code Explanation

The client script (`client.py`) connects to the server using the specified IP address and port. It sends a message to the server and receives a response. The received message is then saved to a log file.

- `import socket` and `import sys` are used for socket communication and handling command-line arguments, respectively.
- The script checks if the command-line arguments are provided correctly, and if not, it prints an error message.
- It creates a socket, connects to the server, sends a message, receives a response, and saves the response to the specified log file.
- The client script handles possible errors related to connections and file operations.

## Server

### Usage

To run the server script, execute it without any arguments:

python3 server.py


The server will listen on the specified port (1122 in the code).

### Code Explanation

The server script (`server.py`) listens for incoming connections and communicates with the client.

- `import socket` is used for socket communication.
- The server listens on a specified port (1122 in the code) for incoming connections.
- When a client connects, it accepts the connection and communicates with the client by sending and receiving messages.
- The server program can handle multiple clients sequentially but not simultaneously.
- It is a basic example of a socket server, and it can be further extended for more advanced use cases.

## Note

This is a simple example of socket communication and does not include error handling for all possible scenarios. It is intended for educational purposes and can be extended and improved as needed.
