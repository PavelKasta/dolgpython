import socket
import SQLserver
#import pickle
#import Test

server_socket = socket.socket()
server_socket.bind(('', 34344))
server_socket.listen(10)

print('Server to start...')

clients = []

while True:
    client, address = server_socket.accept()

    while True:

        data = client.recv(1024)  # получаем данные в байтах
        number = data.decode('utf8')  # декодировали в строку данные

        if int(number) == 1:
            SQLserver.add_book(client)

        elif int(number) == 2:
            SQLserver.delete_book(client)

        elif int(number) == 3:
            SQLserver.find_book(client)

        elif int(number) == 4:
            SQLserver.info_one_book(client)

        elif int(number) == 5:
            SQLserver.info_all_book(client)

        elif int(number) == 6:
            SQLserver.edit_book(client)

server_socket.close()
