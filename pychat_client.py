import func as fc
import socket
import threading
userName = input("User Name: ")
serverHost = input('The IP adress from the Server: ')
serverPort = 5050   # input('The Port from the Server: ')

fc.acssi_client_art()
fc.typingAnimationClearProgram('$ Loging...\n')

def recive_menssages(client_socked):
    while True:
        try:
            messsage = client_socked.recv(1024).decode('utf-8')
            print(messsage)

        except:
            print("$ Disconected from the Server!!!")
            client_socked.close()
            break

def send_menssages(client_socked):
    while True:
        menssage = input(f"$ {userName}> ")
        client_socked.send(menssage.encode('uft-8'))

def start_client():
    client_socked = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socked.connect((serverHost, serverPort))

    recive_thread = threading.Thread(target=recive_menssages, args=(client_socked,))
    recive_thread.start()

if __name__ == '__main__':
    start_client()