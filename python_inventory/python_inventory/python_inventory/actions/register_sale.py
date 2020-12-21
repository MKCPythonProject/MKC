from utils import (
    safe_input,
    select_by_id_or_name,
    today,
    get_products,
    update_products,
    get_employees,
    get_sales,
    add_sale
)


def register_sale():
    sale = {
        "date": today()
    }

    print("--- Satış kaydı ---\n")
    print("Urunu kim satıyor?")

    employees = get_employees()
    for e in employees:
        print("- %s (%s)" % (e['name'], e['id']))
    print()

    employee = select_by_id_or_name(employees, 'employee')
    sale['employee_id'] = employee['id']

    print("Selected: %s (%s)\n" % (employee['name'], employee['id']))
    print("Bu hangi ürün?")
    products = get_products()

    for p in products:
        print("- (%s) %s (%s adet satilabilir.)" %
              (p['id'], p['name'], p['quantity']))
    print()

    product = select_by_id_or_name(products, 'product')

    sale['product_id'] = product['id']

    print("Secilen: %s (%s) (%s stokta var)\n" %
          (product['name'], product['id'], (product['quantity'])))

    quantity = 0
    while True:
        quantity = safe_input("int_positive", "Kaç urun var? ")
        if quantity > 0 and quantity <= product['quantity']:
            print("Emir geçerlidir. Toplam fiyat hesaplanıyor...")
            break
        else:
            print(
                "Sipariş geçersiz. Lütfen stoktaki miktardan büyük olmayan bir sayı seçin")

    # we are updating the reference, so this dictionary is also modified
    # on the products list
    product['quantity'] -= quantity
    sale['num_products'] = quantity
    sale['total_price'] = quantity * product['price']

    print("\nToplam fiyat: %sTL (+ %sTL vergi)" %
          (sale['total_price'], sale['total_price'] * 0.18))

    sale['id'] = len(get_sales())

    print("\nBu siparişin numarasi", sale['id'])

    update_products(products)
    add_sale(sale)
