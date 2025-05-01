import sqlite3

class Queries:
    def __init__(self):
        self.con = sqlite3.connect('nomes.db')
        self.cursor = self.con.cursor()

    def name_queries(self):
        self.cursor.execute('SELECT nome FROM names')
        return self.cursor.fetchall()



