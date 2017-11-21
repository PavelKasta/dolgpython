# -*-coding:UTF-8-*-

import socket

Сlient_Socket = socket.socket()
Сlient_Socket.connect(('localhost', 34344))
print(("\n\n"
       "<1> - Добавить новую книгу\n"
       "<2> - Удалить книгу\n"
       "<3> - Найти книгу\n"
       "<4> - Просмотреть информацию о книге\n"
       "<5> - Просмотреть информацию о всех книгах\n"
       "<6> - Модифицировать информацию о книгах\n"))
try:
    while True:

        print("Выберете пункт меню:")
        while True:

            try:
                number = int(input('>'))

                if number >= 1 and number <= 8:
                    break
            except ValueError as e:
                print("Введите ЧИСЛО от 1 до 7.")

        client_socket.send(str(number).encode('utf8'))

        if number == 1:
            data = client_socket.recv(1024)
            print(data.decode('utf-8'))

            for row in range(0, 5):
                count = input('>')
                client_socket.send(count.encode('utf8'))

                data = client_socket.recv(1024)
                print(data.decode('utf-8'))

        if number == 2 or number == 3 or number == 4:
            data = client_socket.recv(1024)
            print(data.decode('utf-8'))

            number = input('>')
            client_socket.send(number.encode('utf-8'))

            data = client_socket.recv(1024)
            print(data.decode('utf-8'))

        if number == 5:
            data = client_socket.recv(8192)
            print(data.decode('utf-8'))

        if number == 6:

            data = client_socket.recv(1024)
            print(data.decode('utf-8'))

            number = input('>')
            client_socket.send(number.encode('utf8'))

            data = client_socket.recv(1024)

            if str(data.decode('utf-8')) == "Новый уникильный номер:":
                print(data.decode('utf-8'))

                for row in range(0, 5):
                    number = input('>')
                    client_socket.send(number.encode('utf8'))

                    data = client_socket.recv(1024)
                    print(data.decode('utf-8'))

            else:
                print(data.decode('utf-8'))
except ConnectionResetError:
    print("прекращение работы сервера")
