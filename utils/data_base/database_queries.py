import sqlite3

con = sqlite3.connect('nomes.db')
cursor = con.cursor()

class Queries:


    def name_queries(self):        
        return cursor.execute('SELECT nome FROM names')

# Tests
# ----------------------------
queries = Queries()
nomes = queries.name_queries()

name_list = []
def save_name_list():
    for nome in nomes:
        # print(nome[0])
        name_list.append(nome[0])
    return name_list


print(save_name_list())