from .other import dict_to_csv_line

keys = ('id', 'name', 'price', 'quantity',
        'season', 'type', 'sub_type', 'description')


def get_products():
    data = []
    file = open('urunler.csv')

  #  search = input('ID or name of the product?: ')
    for line in file:
        spacing = line.split(',')
        product = {
            "id": int(spacing[0]),
            "name": spacing[1],
            "price": float(spacing[2]),
            "quantity": int(spacing[3]),
            "season": spacing[4],
            "type": spacing[5],
            "sub_type": spacing[6],
            "description": spacing[7].replace('\n', '')
        }
        data.append(product)

    file.close()
    return data


def update_products(product_list):
    file = open('urunler.csv', 'w')
    for p in product_list:
        line = dict_to_csv_line(p, keys)
        file.write(line)

    file.close()
