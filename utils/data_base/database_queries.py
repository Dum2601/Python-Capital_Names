import sqlite3
import os
con = sqlite3.connect(os.path.abspath('utils/data_base/nomes.db'))

cursor = con.cursor()

def name_list():
    cursor.execute('SELECT nome FROM names')
    nomes = []
    for linha in cursor.fetchall():
        nomes.append(linha[0])
    
    return nomes

