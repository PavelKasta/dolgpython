# -*-coding:UTF-8-*-

import socket
import pickle

client_socket = socket.socket()
client_socket.connect(('localhost', 34344))

while True:
    print(("\n\nВыберете пункт меню:\n"
           "<1> - Добавить новую книгу\n"
           "<2> - Удалить книгу\n"
           "<3> - Найти книгу\n"
           "<4> - Просмотреть информацию о книге\n"
           "<5> - Просмотреть информацию о всех книгах\n"
           "<6> - Модифицировать информацию о книгах\n"
           "<7> - Выход\n Введите пункт меню <1-7>:"))
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

        count = input('>')
        client_socket.send(count.encode('utf8'))

        data = client_socket.recv(1024)
        print(data.decode('utf-8'))

        count = input('>')
        client_socket.send(count.encode('utf8'))

        data = client_socket.recv(1024)
        print(data.decode('utf-8'))

        count = input('>')
        client_socket.send(count.encode('utf8'))

        data = client_socket.recv(1024)
        print(data.decode('utf-8'))

        count = input('>')
        client_socket.send(count.encode('utf8'))

        data = client_socket.recv(1024)
        print(data.decode('utf-8'))

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
        data = client_socket.recv(2048)
        print(data.decode('utf-8'))

    if number == 6:

        data = client_socket.recv(1024)
        print(data.decode('utf-8'))

        number = input('>')
        client_socket.send(number.encode('utf8'))

        data = client_socket.recv(1024)

        if str(data.decode('utf-8')) == "Новый уникильный номер:":
            print(data.decode('utf-8'))

            number = input('>')
            client_socket.send(number.encode('utf8'))

            data = client_socket.recv(1024)
            print(data.decode('utf-8'))

            number = input('>')
            client_socket.send(number.encode('utf8'))

            data = client_socket.recv(1024)
            print(data.decode('utf-8'))

            number = input('>')
            client_socket.send(number.encode('utf8'))

            data = client_socket.recv(1024)
            print(data.decode('utf-8'))

            number = input('>')
            client_socket.send(number.encode('utf8'))

            data = client_socket.recv(1024)
            print(data.decode('utf-8'))

            number = input('>')
            client_socket.send(number.encode('utf8'))

            data = client_socket.recv(1024)
            print(data.decode('utf-8'))

        else:
            print(data.decode('utf-8'))

