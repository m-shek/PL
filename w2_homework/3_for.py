"""
Домашнее задание №1
Цикл for: Продажи товаров
* Дан список словарей с данными по количеству проданных телефонов
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
sold_phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 1]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}
]


def common_sum(items_sold):
    sold_amount = 0
    for sold in items_sold:
        sold_amount += sold
    avg = get_avg_val(sold_amount, len(items_sold))
    sum_and_items = {"sold_sum": sold_amount, "sold_count": len(items_sold), "avg_sum": avg}
    return sum_and_items


def get_avg_val(any_sum_value, count):
    avg_val = round((any_sum_value / count), 2)
    return avg_val


def main():
    common_avg_sum = 0
    common_avg_count = 0
    for one_product in sold_phones:
        sold_sum = common_sum(one_product['items_sold'])['sold_sum']
        count_items = common_sum(one_product['items_sold'])['sold_count']
        avg_product = common_sum(one_product['items_sold'])['avg_sum']
        common_avg_sum += sold_sum
        common_avg_count += count_items
        print(f"Суммарное количество продаж для товара {one_product['product']}: {sold_sum}")
        print(f"Среднее количество продаж для товара {one_product['product']}: {avg_product}")
    print(f"Суммарное количество продаж всех товаров : {common_avg_sum}")
    print(f"Среднее количество продаж всех товаров {get_avg_val(common_avg_sum, common_avg_count)}")

if __name__ == "__main__":
    main()
   