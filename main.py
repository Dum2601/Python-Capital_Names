from utils.data_base.database_queries import name_list



name_list = name_list()
# print(name_list)

def capital_letters():
    fixed_names = []
    for names in name_list:
        names_modified = names.title()
        fixed_names.append(names_modified)
    return fixed_names


print(capital_letters())