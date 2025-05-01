# All the DataBase queries will be performed here

import sqlite3

con = sqlite3.connect('nomes.db')
cursor = con.cursor()


# cursor.execute('CREATE TABLE names (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)')


# names = [
#     ("Douglas",),
#     ("Maria",),
#     ("Joao",),
#     ("Carla",),
#     ("Lucas",),
#     ("Fernanda",),
#     ("Rafael",),
#     ("Beatriz",)
# ]

# cursor.executemany('INSERT INTO names (nome) VALUES (?)', names)
# con.commit()

# names = [
#     (1, "douglas"),
#     (2, "maria"),
#     (3, "joao"),
#     (4, "carla"),
#     (5, "lucas"),
#     (6, "fernanda"),
#     (7, "rafael"),
#     (8, "beatriz")
# ]

# for id_, nome in names:
#     cursor.execute('UPDATE names SET nome = ? WHERE id = ?', (nome, id_))

# con.commit()