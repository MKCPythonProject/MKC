from utils import (
    get_sales,
    get_products
)


def most_sold_items():
    print("--- En çok satılan ürünler ---")
    print("Şimdiye kadar en çok satılan 3 ürün:")

    products = get_products()
    sales_file = get_sales()

    products_sold = {}

    for sold_items in sales_file:
        products_sold[sold_items["num_products"]] = 0
    for product in products:
        product_id = product["product_id"]
        products_sold[product_id] += product["num_products"]
        print(product)
