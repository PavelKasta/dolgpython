import pypyodbc


def add_book(client):
    client.send("Добавте поля для новой книги через Enter:\n Уникильный номер:".encode('utf8'))

    data = client.recv(1024)  # получаем данные в байтах
    num = data.decode('utf8')  # декодировали в строку данные

    client.send("Автор:".encode('utf8'))
    data = client.recv(1024)  # получаем данные в байтах
    aut = data.decode('utf8')  # декодировали в строку данные

    client.send("Название:".encode('utf8'))
    data = client.recv(1024)  # получаем данные в байтах
    nam = data.decode('utf8')  # декодировали в строку данные

    client.send("Год выпуска:".encode('utf8'))
    data = client.recv(1024)  # получаем данные в байтах
    yea = data.decode('utf8')  # декодировали в строку данные

    client.send("Колличество экземпляров:".encode('utf8'))
    data = client.recv(1024)  # получаем данные в байтах
    amo = data.decode('utf8')  # декодировали в строку данные

    connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Books\n"
                   "VALUES('" + num + "', '" + aut + "', '" + nam + "','" + yea + "','" + amo + "')")

    client.send("Книга успешно добавлена!".encode('utf8'))
    connection.commit()
    connection.close()


def find_book(client):
    client.send("Введите название книги которую вы ищите:".encode('utf8'))

    data = client.recv(1024)  # получаем данные в байтах
    Name_Book = data.decode('utf8')  # декодировали в строку данные

    connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
    cursor = connection.cursor()

    find = ("SELECT Название\n"
            "FROM dbo.Books\n"
            "WHERE Название ='" + Name_Book + "'")
    cursor.execute(find)
    results = cursor.fetchall()

    for row in results:
        b_name = row[0]

    try:
        client.send(("Книга '" + str(b_name) + "' присутствует в базе!").encode('utf8'))
    except NameError:
        client.send(("Книга '" + str(Name_Book) + "' отсутствует в базе!").encode('utf8'))

    connection.close()


def delete_book(client):
    client.send("Введите название книги которую хотите удалить:".encode('utf8'))

    data = client.recv(1024)  # получаем данные в байтах
    Name_Book = data.decode('utf8')  # декодировали в строку данные

    connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
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
        connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
        cursor = connection.cursor()

        dell = ("DELETE FROM Books WHERE Название = '" + Name_Book + "'")

        cursor.execute(dell)
        connection.commit()

        client.send("Книга успешно удалена из базы".encode('utf8'))
        connection.close()
    except NameError:
        client.send("Такой книги нет в базе".encode('utf8'))


def edit_book(client):
    client.send("Введите название книги которую хотите изменить:".encode('utf8'))

    data = client.recv(1024)
    name = data.decode('utf8')

    connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
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
        client.send("Новый уникильный номер:".encode('utf8'))

        data = client.recv(1024)  # получаем данные в байтах
        num = data.decode('utf8')  # декодировали в строку данные

        client.send("Автор:".encode('utf8'))
        data = client.recv(1024)  # получаем данные в байтах
        aut = data.decode('utf8')  # декодировали в строку данные

        client.send("Название:".encode('utf8'))
        data = client.recv(1024)  # получаем данные в байтах
        nam = data.decode('utf8')  # декодировали в строку данные

        client.send("Год выпуска:".encode('utf8'))
        data = client.recv(1024)  # получаем данные в байтах
        yea = data.decode('utf8')  # декодировали в строку данные

        client.send("Колличество экземпляров:".encode('utf8'))
        data = client.recv(1024)  # получаем данные в байтах
        amo = data.decode('utf8')  # декодировали в строку данные

        connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
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
    client.send('О какой книге вы хотетие получить информацию:'.encode('utf8'))

    data = client.recv(1024)  # получаем данные в байтах
    Name_Book = data.decode('utf8')  # декодировали в строку данные

    connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
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

        connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
        cursor = connection.cursor()

        mySQLQuery = ("SELECT Уникальный_номер, Автор, Название, Год_выпуска, Колличество_экземпляров\n"
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

            client.send(("||Уникальный_номер:" + str(number) + "||Автор:" + str(author) + "||Название:" + str(name) +
                         "||Год_выпуска:" + str(year) + "||Колличество_экземпляров:" + str(amount)).encode('utf8'))

            connection.close()
    except NameError:
        client.send("Такой книги нет в базе!".encode('utf8'))


def info_all_book(client):
    connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-MIC3C7G7\PASHASERVER;DATABASE=PashaSQL;')
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

    client.send(table.encode("utf8"))
