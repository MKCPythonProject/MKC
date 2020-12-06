from utils import (
    safe_input,
    get_products,
    get_employees,
    get_sales
)

from actions import (
    register_sale,
    register_product_arrival,
    query_inventory_data,
    employees_with_most_sales,
    most_sold_items
)

def main():
    print("\n\n[LOGO]\n\n")
    print("MKC' ye Hoşgeldiniz.")
    print("""
Menü seçim :

1. Satış kaydı
2. Ürün gelişini kaydedin
3. Envanter verilerini sorgulama
4. En çok satılan ürünler
5. En çok satış yapan çalışanlar
6. Satış raporu oluşturun
7. Yalnızca sezonluk ürünleri göster
8. Müşteri memnuniyeti formu
""")

    while True:

        action = safe_input('int_positive', 'Seçiminiz: ')

        if action > 0 and action < 9:
            break

        print("Seçiminizi 1-8 arası giriniz...")


    if action == 1:
        register_sale()
    elif action == 2:
        register_product_arrival()
    elif action == 3:
        query_inventory_data()
    elif action == 4:
        print(4)
        print("--- Most sold items ---")
    elif action == 5:
        employees_with_most_sales()
    elif action == 6:
        print(6)
        print("--- Çalışanın satış raporunu oluşturun ---")
    elif action == 7:
        print(7)
        print("--- Yalnızca sezonluk ürünleri göster ---")
    else:
        print(8)
        print("--- Müşteri memnuniyeti formu ---")

    print("Mkc_depo'yu kullandığınız için teşekkürler. İyi günler \ n")


while True:
    main()

    again = input("Yeniden başlamak ister misin? (y / n)").strip()[0].lower()

    if (again == 'y'):
        continue
    else:
        print("Kendinize iyi bakın.\n")
        break

        
