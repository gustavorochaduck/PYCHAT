import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # The gethostname take the IP address with the gethostname(The name of the DEVICE) 
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STRAM)
server.bind(ADDR)

def handle_client(conn, addr):
    pass

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        print(f"[ACTIVE CONNECTIONS] {thread.activeCount() -1}")