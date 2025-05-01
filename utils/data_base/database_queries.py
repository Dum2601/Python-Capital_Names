import sqlite3

class Queries:
    def __init__(self):
        self.con = sqlite3.connect('nomes.db')
        self.cursor = self.con.cursor()

    def name_queries(self):        
        return self.cursor.execute('SELECT nome FROM names')

queries = Queries()
nomes = queries.name_queries()

for nome in nomes:
    print(nome[0])
