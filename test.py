import json
file_path = r'C:\Users\itvis\PycharmProjects\pythonProject\venv\orders_july_2023.json'
with open(file_path, "r") as my_file:
# считываем информацию из файла и преобразовываем строку json в словарь
    orders = json.load(my_file)
max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'1.Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')

max_quantity = 0
max_order = ''
max_quantity_list = []
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_order = order_num
        max_quantity = quantity
        max_quantity_list.clear()
        max_quantity_list.append(order_num)
    elif quantity == max_quantity:
        max_quantity_list.append(order_num)
print(f'2.Номера заказов с самым большим количеством товаров: {max_quantity_list}, количество товаров в заказе: {max_quantity}')


max_day_order = 0
day_order = {}
for order_num, orders_data in orders.items():
    date = orders_data['date']
    day_order[date] = day_order.get(date, 0) + 1
max_day_order = max(day_order.values())
for key, value in day_order.items():
    if value == max_day_order:
        day = key
print(f'3.{day} было сделано больше всего заказов, количество заказов в этот день: {max_day_order}')

users = {}
max_orders = 0
for order_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    users[user_id]=users.get(user_id, 0) + 1
max_orders = max(users.values())
for key, value in users.items():
    if value == max_orders:
        user_id = key
print(f'4.Самое большое количество заказов сделал пользователь: {user_id}')

user_dict = {}
max_price = 0
for order_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    user_dict[user_id] = user_dict.get(user_id, 0) + orders_data['price']
max_price = max(user_dict.values())
for key, value in user_dict.items():
    if value == max_price:
        user_id = key
print(f"5.Пользователь {user_id} имеет саммую большую суммарную стоймость заказов за июль {max_price}")

price_sum = 0
price_count = 0
for order_num, orders_data in orders.items():
    price_sum += orders_data['price']
    price_count = len(orders)
print(f"6.Средняя стоймость заказа в июле: {price_sum//price_count}")

price_sum = 0
all_quantity = 0
for order_num, orders_data in orders.items():
    price_sum += orders_data['price']
    all_quantity += orders_data['quantity']
print(f"7.Средняя стоймость товара в июле: {price_sum//all_quantity}")
