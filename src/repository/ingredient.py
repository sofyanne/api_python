import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    port='8889',
    database='pythondb',
    user='root',
    password='root')

cursor = db.cursor(dictionary=True)


def get_all_ingredients() -> list:
    query = "SELECT * FROM ingredient"
    cursor.execute(query)
    return cursor.fetchall()


def get_ingredient(id: int) -> dict:
    query = "SELECT * FROM ingredient WHERE id = %s"
    cursor.execute(query, (id,))
    return cursor.fetchone()


def create_new_ingredient(data: dict) -> int:
    query = "INSERT INTO ingredient (labem) VALUES (%(labem)s)"
    cursor.execute(query, data)
    db.commit()
    return cursor.lastrowid


def update_ingredient(data: dict):
    query = "UPDATE ingredient SET labem = %(labem)s WHERE id = %(id)s"
    cursor.execute(query, data)
    db.commit()
