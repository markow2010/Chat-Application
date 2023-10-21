import socket
import sys
import random

if sys.argv[1] == '-p' and sys.argv[3] == '-l':
    port = int(sys.argv[2])
    log = str(sys.argv[4])
    
    socket = socket.socket()
    print("socket created successfully")
socket.bind(('', port))
print("binded")
socket.listen(2)
file = open(log, 'a')
m_f = open("quotes.txt", 'r')
(cs, address) = socket.accept()
print("established connection from : ", str(address))
while True:
    recieved = cs.recv(1024).decode()
    if not recieved:
        break
    print(" they say : ", str(recieved))
    file.write(recieved)
    file.write("\n")

    if recieved.find("network") != -1:
        randomInt = random.randint(0, 29)
        while randomInt != 0:
            response = next(m_f)
            randomInt = randomInt - 1
        m_f.seek(0)
        print(response)
        cs.send(response.encode())
socket.close()
file.close()





