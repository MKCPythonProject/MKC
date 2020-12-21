from .other import dict_from_entries

keys = ('id', 'name', 'last_name', 'position')


def get_employees():

    employees = []

    file = open('calisanlar.csv')

    for line in file:
        id, name, last_name, position = line.split(',')

        employees.append(dict_from_entries(keys, (
            int(id),
            name,
            last_name,
            position.rstrip()
        )))

    file.close()
    return tuple(employees)

# def get_employees():

#     keys = ('id', 'name', 'last_name', 'position')
#     employees = []

#     file = open('employees.csv')

#     for line in file:
#         values = line.split(',')
#         employees.append({
#             keys[0]: int(values[0]),
#             keys[1]: values[1],
#             keys[2]: values[2],
#             keys[3]: values[3].rstrip(),
#         })

#     file.close()
#     return employees
