import socket
import threading
import func as fc

fc.cleanTerminal()

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # The gethostname take the IP address with the gethostname(The name of the DEVICE) 
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

def handle_client(client_socket):
    while True:
        try: #Try will find if it haves some ghost variable
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            for client in clients:
                if client != client_socket:
                    client.send(message.encode('utf-8'))
            
        except:
            clients.remove(client_socket)
            client.socket.close()
            break

def start_server():
    fc.pc_ascii()
    fc.typingAnimationClearProgram("$ STARTING...\n")
    server.listen()
    print(f'$ Client Started on {SERVER} : {PORT}')

    while True:
        client_socket, client_address = server.accept()
        print(f'$ New Connection from: {client_address}')
        clients.append(client_socket) 

        thread = threading.Thread(target=handle_client, args=(client_socket,))  
        thread.start()

if __name__ == '__main__':
    start_server()