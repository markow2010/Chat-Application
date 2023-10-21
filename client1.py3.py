import socket
import sys
try:
	if sys.argv[1] == '-s' and sys.argv[3] == '-p' and sys.argv[5] == '-l':
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		FileName=str(sys.argv[6])
		ip = socket.gethostname()
		p = int(sys.argv[4])
		print("arguments read correctly")
		try:	
			s.connect((ip, p))
			print("connection succeeded")
		except connection_failed:
			print("connection_failed: was the ip of p miss-input?")
		print("What would you like to send to the server?")
		message = input()

		s.send(message.encode())
		recieved = s.recv(1024).decode()
		print(recieved)
		s.close()
		try:
			file = open(FileName, 'a')
			file.write(recieved)
			file.close()
		except file_failure:
			print("file_failure: The file Failed to open and write correctly")		
	else:
		print("formatted incorectly, use client.py3 -s <ip> -p <p> -l <logfile>")
except incorrect_use:
	print("incorrect_use: use format client.py3 -s <ip> -p <p> -l <logfile>")







