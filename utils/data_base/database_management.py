# All the DataBase queries will be performed here

import sqlite3

con = sqlite3.connect('nomes.db')
cursor = con.cursor()


cursor.execute('CREATE TABLE names (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)')