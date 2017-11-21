import pypyodbc

BUFFSIZE = 1024


def send_message(message, client):
    client.send(message.encode('utf8'))


def message(client):
    data = client.recv(BUFFSIZE)
    return data.decode('utf8')


def add_book(client):
    client.send("Добавте поля для новой книги через Enter:\n Уникильный номер:".encode('utf8'))
    num = message(client)

    send_message("Автор", client)
    aut = message(client)

    send_message("Название", client)
    nam = message(client)

    send_message("Год выпуска", client)
    yea = message(client)

    send_message("Колличество экземпляров", client)
    amo = message(client)

    connection = pypyodbc.connect('DRIVER={SQL Server};\
    SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Books\n"
                   "VALUES('" + num + "', '" + aut + "', '" + nam + "','" + yea + "','" + amo + "')")

    send_message("Книга успешно добавлена", client)
    connection.commit()
    connection.close()


def find_book(client):
    send_message("Введите название книги которую вы ищите:", client)
    Name_Book = message(client)

    connection = pypyodbc.connect('DRIVER={SQL Server};\
        SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
    cursor = connection.cursor()

    find = ("SELECT Название\n"
            "FROM dbo.Books\n"
            "WHERE Название ='" + Name_Book + "'")
    cursor.execute(find)
    results = cursor.fetchall()

    for row in results:
        b_name = row[0]

    try:
        send_message("Книга '" + str(b_name) + "' присутствует в базе!", client)
    except NameError:
        send_message("Книга '" + str(Name_Book) + "' отсутствует в базе!", client)

    connection.close()


def delete_book(client):
    send_message("Введите название книги которую хотите удалить:", client)

    Name_Book = message(client)

    connection = pypyodbc.connect('DRIVER={SQL Server};\
        SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
    cursor = connection.cursor()

    find = ("SELECT Название\n"
            "FROM dbo.Books\n"
            "WHERE Название ='" + Name_Book + "'")
    cursor.execute(find)
    results = cursor.fetchall()
    connection.close()
    for row in results:
        b_name = row[0]

    try:
        str(b_name)
        connection = pypyodbc.connect('DRIVER={SQL Server};\
            SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
        cursor = connection.cursor()

        dell = ("DELETE FROM Books WHERE Название = '" + Name_Book + "'")

        cursor.execute(dell)
        connection.commit()

        send_message("Книга успешно удалена из базы", client)
        connection.close()
    except NameError:
        send_message("Такой книги нет в базе", client)


def edit_book(client):
    send_message("Введите название книги которую хотите изменить:", client)

    name = message(client)

    connection = pypyodbc.connect('DRIVER={SQL Server};\
        SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
    cursor = connection.cursor()

    find = ("SELECT Название\n"
            "FROM dbo.Books\n"
            "WHERE Название ='" + name + "'")
    cursor.execute(find)
    results = cursor.fetchall()

    for row in results:
        b_name = row[0]

    try:
        str(b_name)
        send_message("Новый уникильный номер:", client)
        num = message(client)

        send_message("Автор:", client)
        aut = message(client)

        send_message("Год выпуска:", client)
        yea = message(client)

        send_message("Колличество экземпляров:", client)
        amo = message(client)

        send_message("Название книги:", client)
        nam = message(client)

        connection = pypyodbc.connect('DRIVER={SQL Server};\
            SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
        cursor = connection.cursor()

        number = (
            "UPDATE Books\n"
            "SET Уникальный_номер= '" + num + "'\n"
                                              "WHERE Название= '" + name + "'"
        )
        cursor.execute(number)
        connection.commit()

        author = (
            "UPDATE Books\n"
            "SET Автор= '" + aut + "'\n"
                                   "WHERE Название= '" + name + "'"
        )
        cursor.execute(author)
        connection.commit()

        year = (
            "UPDATE Books\n"
            "SET Год_выпуска= '" + yea + "'\n"
                                         "WHERE Название= '" + name + "'"
        )
        cursor.execute(year)
        connection.commit()

        amount = (
            "UPDATE Books\n"
            "SET Колличество_экземпляров= '" + amo + "'\n"
                                                     "WHERE Название= '" + name + "'"
        )
        cursor.execute(amount)
        connection.commit()

        name_b = (
            "UPDATE Books\n"
            "SET Название= '" + nam + "'\n"
                                      "WHERE Название= '" + name + "'"
        )

        cursor.execute(name_b)
        connection.commit()

        client.send("параметры книги успешно изменены!".encode('utf8'))
        connection.close()

    except NameError:

        client.send("Такой книги нет в базе!".encode('utf8'))


def info_one_book(client):
    send_message('О какой книге вы хотетие получить информацию:', client)

    Name_Book = message(client)

    connection = pypyodbc.connect('DRIVER={SQL Server};\
        SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
    cursor = connection.cursor()

    find = ("SELECT Название\n"
            "FROM dbo.Books\n"
            "WHERE Название ='" + Name_Book + "'")

    cursor.execute(find)
    results = cursor.fetchall()
    connection.close()
    for row in results:
        b_name = row[0]
    try:
        str(b_name)

        connection = pypyodbc.connect('DRIVER={SQL Server};\
            SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
        cursor = connection.cursor()

        mySQLQuery = ("SELECT Уникальный_номер, Автор, Название, Год_выпуска,\
         Колличество_экземпляров\n"
                      "FROM dbo.Books\n"
                      "WHERE Название ='" + Name_Book + "'")

        cursor.execute(mySQLQuery)
        results = cursor.fetchall()

        for row in results:
            number = row[0]
            author = row[1]
            name = row[2]
            year = row[3]
            amount = row[4]

            count = str("Уникальный_номер: {0:7}\t Автор: {1:20}\t Название: {2:20}\t Год_выпуска: {3:7}\t "
                        "Колличество_экземпляров: "
                        "{4:7}\t\n".format(number, author, name, year, amount))

            send_message(count, client)

            connection.close()
    except NameError:
        send_message("Такой книги нет в базе!", client)


def info_all_book(client):
    connection = pypyodbc.connect('DRIVER={SQL Server};\
        SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
    cursor = connection.cursor()

    mySQLQuery = ("SELECT Уникальный_номер, Автор, Название, Год_выпуска, Колличество_экземпляров\n"
                  "FROM dbo.Books")

    cursor.execute(mySQLQuery)
    results = cursor.fetchall()
    connection.close()

    table = str()
    for row in results:
        number = row[0]
        author = row[1]
        name = row[2]
        year = row[3]
        amount = row[4]

        count = str("Уникальный_номер: {0:7}\t Автор: {1:20}\t Название: {2:20}\t Год_выпуска: {3:7}\t "
                    "Колличество_экземпляров: "
                    "{4:7}\t\n".format(number, author, name, year, amount))
        table = table + count

    send_message(table, client)
