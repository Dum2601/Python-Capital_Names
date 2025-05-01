from utils.data_base.database_queries import Queries

queries = Queries()
nomes = queries.name_queries()


for nome in nomes:
    print(nome[0])