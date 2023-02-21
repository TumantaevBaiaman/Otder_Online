from apps.db.db import connection


def info_pizza():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT id, img_id, pizza_name, description, payment FROM pizza;""")
        data = cursor.fetchall()
        data_pizza = []
        for i in data:
            data_pizza.append([i[0], i[1], i[2], i[3], i[4]])
        return data_pizza


def info_drink():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT id, img_id, drink_name, description, payment FROM drink;""")
        data = cursor.fetchall()
        data_pizza = []
        for i in data:
            data_pizza.append([i[0], i[1], i[2], i[3], i[4]])
        return data_pizza


def add_pizza(data: dict):
    img_id = data['img_id']
    pizza_name = data['pizza_name']
    description = data['description']
    payment = int(data['payment'])

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO pizza(img_id, pizza_name, description, payment) VALUES (%s, %s, %s, %s);",
                (
                    img_id,
                    pizza_name,
                    description,
                    payment
                )
            )
    except:
        print("Error")


def add_drink(data: dict):
    img_id = data['img_id']
    drink_name = data['drink_name']
    description = data['description']
    payment = int(data['payment'])

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO drink(img_id, drink_name, description, payment) VALUES (%s, %s, %s, %s);",
                (
                    img_id,
                    drink_name,
                    description,
                    payment
                )
            )
    except:
        print("Error")


def basket_pizza(data):

    id_user = data['id_user']
    product = data['product']
    payment = int(data['payment'])

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO basket(id_user, product, payment) VALUES (%s, %s, %s);",
                (
                    id_user,
                    product,
                    payment
                )
            )
    except:
        print("Error")


def info_order(id_user):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, id_user, product, payment, created_at FROM user_order WHERE id_user=(%s);", (id_user,))
        data = cursor.fetchall()
        data_basket = []
        for i in data:
            data_basket.append([i[0], i[1], i[2], i[3], i[4]])
        return data_basket


def order_pizza(data):
    id_user = data['id_user']
    product = data['product']
    payment = int(data['payment'])
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO user_order(id_user, product, payment) VALUES (%s, %s, %s);",
                (
                    id_user,
                    product,
                    payment
                )
            )
    except:
        print("Error")


def info_basket(id_user):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, id_user, product, payment FROM basket WHERE id_user=(%s);", (id_user,))
        data = cursor.fetchall()
        data_basket = []
        for i in data:
            data_basket.append([i[0], i[1], i[2], i[3]])
        return data_basket


def add_user(data: dict):
    id_user = data['id_user']
    username = data['username']
    email = data['email']
    phone = int(data['phone'])

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO account(id_user, username, email, phone) VALUES (%s, %s, %s, %s);",
                (
                    id_user,
                    username,
                    email,
                    phone
                )
            )
    except:
        print("Error")


def all_user():

    with connection.cursor() as cursor:
        cursor.execute("SELECT id, id_user, username, email, phone FROM account")
        data = cursor.fetchall()
        data_basket = []
        for i in data:
            data_basket.append(i[1])
        return data_basket


def info_email(id_user):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, id_user, email FROM account WHERE id_user=(%s);", (id_user,))
        data = cursor.fetchall()
        data_email = []
        for i in data:
            data_email.append(i[2])
        return data_email


def delete_data_in_basket(id_product):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM basket WHERE id=(%s);", (id_product,))

