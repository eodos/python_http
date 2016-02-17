import socket
# import sys

HOST, PORT = "169.254.164.6", 7
# data = " ".join(sys.argv[1:])
data = "1"*946  # packet size: 1KB
received = ""

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server
    sock.connect((HOST, PORT))
    for i in range(1, 51):
        # Send data
        sock.sendall(data)
        # Receive data from the server
        received = sock.recv(1024)

finally:
    # Shut down
    sock.close()

print "Sent:     {}".format(data)
print "Received: {}".format(received)

del data
del received
