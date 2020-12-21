from utils import (
    get_products,
    select_by_id_or_name,
    safe_input
)


def query_inventory_data():

    print("---Envanter verilerini sorgulama---")
    print("Bu hangi ürün?")

    list_products = get_products()

    for products in list_products:
        print(products['id'], products['name'])

    this_product = select_by_id_or_name(list_products, 'product')

    print("Tanimlamasi:", this_product["description"])
    print("Nosu:", this_product["id"])
    print("Birim fiyati: %sTL" % this_product["price"])
    print("Stoktaki Miktari:", this_product["quantity"])
    print("Mevsimi:", this_product["season"])
    print("Kategorileri:", this_product["type"], "-", this_product["sub_type"])
