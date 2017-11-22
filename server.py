import socket
import SQLserver
import threading
import os
import sys

server_socket = socket.socket()
server_socket.bind(('', 34344))
server_socket.listen(10)

print('Server to start...')


def connecting(client):
    try:
        print("Connect user...")
        while True:
            try:
                data = client.recv(1024)
                number = data.decode('utf8')

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
            except ConnectionResetError:
                print("Disconnect user...")
                break
    except ConnectionAbortedError:
        print("Server to stop...")


def stop_server():
    Stop = str(input("Для отсановки серверы нажмите введите 'stop':\n"))
    if Stop == "stop":
        print("прекращение работы сервера")
        os._exit(0)
    else:
        stop_server()


while True:
    client, address = server_socket.accept()

    main = threading.Thread(target=connecting, args=[client])
    stop = threading.Thread(target=stop_server)
    stop.start()
    main.start()

