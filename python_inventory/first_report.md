```
Eva Pérez     A01568830
Víctor Puga   A01568636
```

# First Report

## Theme

<div align="center" >
    <h3>Starbucks Inventory Program</h3>
    <img 
        height="100" 
        width="100" 
        src="https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Starbucks_Corporation_Logo_2011.svg/1200px-Starbucks_Corporation_Logo_2011.svg.png"/>
</div>

## Tasks

- Register sales `(Víctor)`
- Register product arrivals `(Eva)`
- Query inventory data `(Eva)`
- Most sold items `(Eva)`
- Employees with most sales `(Víctor)`
- Generate employee's sales report `(Víctor)`

---

- Show only seasonal products `(Eva)`
- Customer satisfaction form `(Víctor)`

## Screens

### 0. Main Menu

```
Select an action

1. Register sale
2. Register product arrival
3. Query inventory data
4. Most sold items
5. Employees with most sales
6. Generate sales report
7. Show only seasonal products
8. Customer satisfaction form

Action: _____                                       ⇢  Action: 2
```

### 1. Register Sale

```
Action: 1

--- Register sale ---

Who is selling the product?:
- Juan (1)
- Pedro (2)

Name or Id: _____                                   ⇢  Name or Id: Pedro
                                                    ⇢  Name or Id: 2

Which product is it?:
- Coffee (1) (3 in stock)
- Tea (2) (10 in stock)

Name or Id: _____                                   ⇢  Name or Id: Coffee
                                                    ⇢  Name or Id: 1

How many items? _____                               ⇢  How many items? 4

The order is valid. Calculating total price...

Total price: $_____ (+ _____ tax)

This order's id is _____

Press enter to return to main screen
Press r to register another sale
```

### 2. Register Product Arrival

```
Action:2
--- Register product arrival ---

Which product is it?:
- Coffee (1)
- Tea (2)

Name or Id: _____                                   ⇢  Name or Id: Coffee
                                                    ⇢  Name or Id: 1

Recent arrival quantity: _____                      ⇢  Recent arrival quantity: 123456
OKAY. You registered _____ items of _____ product
Now there are _____ in stock

Press enter to return to main screen
Press r to register another product
```

### 3. Query Inventory Data

```
Action: 3
--- Query inventory data ---

Which product is it?:
- Coffee (1)
- Tea (2)

Name or Id: _____                                   ⇢  Name or Id: Coffee
                                                    ⇢  Name or Id: 1

Information for _____

Description: _____
Id: _____
Price per unit: _____
Quantity in stock: _____
Season: _____
Categories: _____, _____

Press enter to return to main screen
Press r to search another product
```

### 4. Most Sold Item

```
Action: 4
--- Most sold items ---

Top 3 most sold product until now:
1) _____ with _____ units sold
2) _____ with _____ units sold
3) _____ with _____ units sold

Press enter to return to main screen
```

### 5. Show Employee with Most Items Sold

```
Action: 5
--- Show employees with most items sold ---

Top 3 employees:
1) _____ with _____ items sold
2) _____ with _____ items sold
3) _____ with _____ items sold

Press enter to return to main screen
```

### 6. Generate Sales Report

```
Action: 6
--- Generate employee's sales report ---

Select an employee?:
- Juan (1)
- Pedro (2)

Name or Id: _____                                   ⇢  Name or Id: Pedro
                                                    ⇢  Name or Id: 2

Creating archive...
Archive saved as "_____"

Press enter to return to main screen
Press r to generate another report
```

#### Sample output file

```
| EMPLOYEE NAME |         |             |
| ------------- | ------- | ----------- |
| PRODUCT ID    | NAME    | QUANTITY    |
| PRODUCT ID    | NAME    | QUANTITY    |
| PRODUCT ID    | NAME    | QUANTITY    |
```

### 7. Show Only Seasonal Products

```
Action: 7
--- Show only seasonal products ---

Season: _____

Products available only this season:
- _____
- _____
- _____

Press enter to return to main screen
Press r to search in another season
```

### 8. Customer Satisfaction Form

```
Action: 8
--- Customer satisfaction form ---

Which is your sale id (it is found on your receipt)? _____

How was our service? (1, 2, 3, 4, 5) _____

Cool. Thanks for giving us your feedback.
We hope to see you again.

Press enter to return to main screen
```

## Data Models

### Products

| **id** | **name** | **price** | **quantity** | **season** | **type** | **syb_type** | **description** |
| ------ | :------: | :-------: | :----------: | :--------: | :------: | :----------: | :-------------: |
| `int`  | `string` |  `float`  |    `int`     |  `string`  | `string` |   `string`   |    `string`     |

```python
product = {
    "id": 0,
    "name": "Frappe",
    "price": 20.00,
    "quantity": 234567,
    "season": "ALL",
    "type": "DRINK",
    "sub_type": "COLD_COFFEE",
    "description": "..."
}
```

### Employees

| **id** | **name** | **last_name** | **position** |
| ------ | :------: | :-----------: | :----------: |
| `int`  | `string` |   `string`    |   `string`   |

```python
employee = {
    "id": 0,
    "name": "John",
    "last_name": "Appleseed",
    "position": "MANAGER",
}
```

### Sale

| **id** | **date** | **total_price** | **num_products** | **product_id** | **employee_id** |
| :----: | :------: | :-------------: | :--------------: | :------------: | :-------------: |
| `int`  | `string` |     `float`     |      `int`       |     `int`      |      `int`      |

```python
sale = {
    "id": 0,
    "date": "18/01/2020",
    "total_price": 300.00,
    "num_products": 15,
    "product_id": 0,
    "employee_id": 0,
}
```

### Feedback (Beta)

| **id** | **date** | **sale_id** | **rating** |
| ------ | :------: | :---------: | :--------: |
| `int`  | `float`  |    `int`    |   `int`    |

```python
feedback = {
    "id": 0,
    "date": "18/01/2020",
    "sale_id": 0,
    "rating": 5,
}
```

## Enumerations

| **Seasons** |     | **Rating** |     | **Positions** |     | **Types** |     | **Sub Types**   |
| :---------- | --- | :--------- | --- | :------------ | --- | :-------- | --- | :-------------- |
| `"ALL"`     |     | `1`        |     | `"REGISTER"`  |     | `"DRINK"` |     | `"HOT_COFFEE"`  |
| `"SPRING"`  |     | `2`        |     | `"MANAGER"`   |     | `"FOOD"`  |     | `"HOT_DRINK"`   |
| `"SUMMER"`  |     | `3`        |     | `"WAITER"`    |     |           |     | `"HOT_DRINK"`   |
| `"FALL"`    |     | `4`        |     | `"BARISTA"`   |     |           |     | `"COLD_COFFEE"` |
| `"WINTER"`  |     | `5`        |     |               |     |           |     | `"COLD_DRINK"`  |
|             |     |            |     |               |     |           |     | `"COLD_DRINK"`  |
|             |     |            |     |               |     |           |     | `"BREAKFAST"`   |
|             |     |            |     |               |     |           |     | `"LUNCH"`       |
|             |     |            |     |               |     |           |     | `"SNACK"`       |
