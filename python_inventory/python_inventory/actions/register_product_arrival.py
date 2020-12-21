from utils import (
    get_products,
    select_by_id_or_name,
    safe_input,
    update_products
)


def register_product_arrival():
    print("--- Ürün gelişini kaydedin ---\n")
    print("Bu hangi ürün?")

    menu = get_products()

    for thing in menu:
        print(thing['id'], thing['name'])

    chooosen_product = select_by_id_or_name(menu, 'product')

    arrival_quantity = safe_input('int_positive', 'Gelen miktar adeti:')

    chooosen_product['quantity'] += arrival_quantity

    print('%s urununden %s adet giriş yapildi' %
          (chooosen_product['name'],arrival_quantity))
    print('%s yeni urun adetidir' % chooosen_product['quantity'])
    update_products(menu)