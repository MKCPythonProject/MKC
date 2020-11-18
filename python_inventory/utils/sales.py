from .other import dict_to_csv_line, dict_from_entries

columns = (
    'id',
    'date',
    'total_price',
    'num_products',
    'product_id',
    'employee_id'
)


def get_sales():
    sales = []
    file = open('satislar.csv')
    for line in file:
        id, date, total_price, num_products, product_id, employee_id = line.split(
            ',')

        sales.append(dict_from_entries(columns, (
            int(id),
            date,
            float(total_price),
            int(num_products),
            int(product_id),
            int(employee_id.rstrip()),
        )))

    file.close()
    return tuple(sales)


def add_sale(sale):
    file = open('satislar.csv', 'a')
    line = dict_to_csv_line(sale, columns)

    file.write(line)
    file.close()
