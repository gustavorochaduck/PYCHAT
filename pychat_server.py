import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # The gethostname take the IP address with the gethostname(The name of the DEVICE) 
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STRAM)
server.bind(ADDR)