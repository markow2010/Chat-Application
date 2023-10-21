import socket
import sys

s = socket.socket()
print("Socket successfully created")
port = 2223

s.bind(('', port))
print("socket binded to %s" %(port))

s.listen(1)
print("socket is listening")

while True:
    c, addr = s.accept()
    r = c.recv(1024).decode()
    print('Got connection from', addr)
    message = "Thank you for connecting."
    c.send(message.encode("utf-8"))
    print("\nFrom client: " + str(r))
    print("Shutting down server.")
    c.close()
    break