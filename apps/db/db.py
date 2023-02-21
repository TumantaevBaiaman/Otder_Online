from config import user, password, db_name, ip
import psycopg2

try:
    connection = psycopg2.connect(
        host=ip,
        user=user,
        password=password,
        database=db_name,
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS pizza(
                id serial PRIMARY KEY,
                img_id varchar(150) NOT NULL,
                pizza_name varchar(50) NOT NULL,
                description varchar(255) NOT NULL,
                payment int NOT NUll
                );
                """
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS telbot_user(
                id_order bigint NOT NULL,
                username varchar(50) NOT NULL,
                phone varchar(50) NOT NULL,
                email varchar(50) NOT NULL
                );
                """
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS basket(
                id serial PRIMARY KEY,
                id_user bigint NOT NULL,
                product varchar(150) NOT NULL,
                payment int NOT NUll
                );
                """
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS user_order(
                id serial PRIMARY KEY,
                id_user bigint NOT NULL,
                product varchar(8000) NOT NULL,
                payment int NOT NUll,
                created_at date NOT NULL DEFAULT now()
                );
                """
        )

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"server version: {cursor.fetchone()}")

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS drink(
                id serial PRIMARY KEY,
                img_id varchar(150) NOT NULL,
                drink_name varchar(50) NOT NULL,
                description varchar(255) NOT NULL,
                payment int NOT NUll
                );
                """
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS account(
                id serial PRIMARY KEY,
                id_user bigint NOT NULL,
                username varchar(255) NOT NULL,
                email varchar(255) NOT NULL,
                phone varchar(255) NOT NULL
                );
                """
        )

except Exception as ex:
    print("Error")

finally:
    pass