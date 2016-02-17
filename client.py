import socket

TCP_IP = 'localhost'
TCP_PORT = 9999
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((TCP_IP, TCP_PORT))
s2.send(MESSAGE)
data = s2.recv(BUFFER_SIZE)
s2.close()

print "received data:", data
