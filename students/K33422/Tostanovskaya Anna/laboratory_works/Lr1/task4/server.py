import threading
import socket

host = '127.0.0.1'
port = 14902

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(10)
print(host, port)

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(16384)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break



def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        # запрашиваем и записываем ники участников
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(16384).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        # транслируем новое подключение и ник участника
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('utf-8'))
        client.send('Connected to server!'.encode('utf-8'))
        # начинаем обработку потока для участника чата
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()