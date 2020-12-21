from utils import (
    get_employees,
    get_sales,
    dict_from_entries,
    find_by_key
)


def employees_with_most_sales():
    print('--- En çok satılan ürünle çalışanları göster ---\n')

    employees = get_employees()
    sales = get_sales()

    products_by_employee = {}

    for e in employees:
        products_by_employee[e['id']] = 0

    for s in sales:
        employee_id = s['employee_id']
        products_by_employee[employee_id] += s['num_products']

    top_employees = []

    for i in range(3):
        top_employee = {"employee_id": -1, "products": -1}

        for k in products_by_employee:
            total_products = products_by_employee[k]
            if total_products > top_employee['products']:
                top_employee = {
                    "employee_id": k,
                    "products": total_products
                }
        top_employees.append(top_employee)
        del products_by_employee[top_employee['employee_id']]

    print('En iyi 3 Calisan:')
    place = 0
    for el in top_employees:
        place += 1
        employee = find_by_key(employees, 'id', el['employee_id'])
        print("%s) %s %s ile %s satilan urunler" % (
            place,
            employee['name'],
            employee['last_name'],
            el['products']
        ))
    print()
