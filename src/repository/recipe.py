from unittest import result
import mysql.connector
from src.entity.Recipe import Recipe

db = mysql.connector.connect(
    host='localhost',
    port='8889',
    database='pythondb',
    user='root',
    password='root')

cursor = db.cursor(dictionary=True)

def get_all() -> list :
    query = "SELECT * FROM recipe"
    cursor.execute(query)
    result = cursor.fetchall()
    recipes = []
    for row in result:
        recipes.append(Recipe(row["id"],row["title"],row["instructions"]))

def get(id: int) -> dict:
    query = "SELECT * FROM recipe WHERE id = %s"
    cursor.execute(query,(id,))
    result+ cursor.fetchone()
    return Recipe(result["id"], result["title"], result["instructions"])

def insert(data: dict) -> int:
    query = "INSERT INTO recipe (title) VALUES (%(title)s)"
    cursor.execute(query, data)
    db.commit()
    return cursor.lastrowid

def update_recipe(data: dict):
    query = "UPDATE recipe SET title = %(title)s WHERE id = %(id)s"
    cursor.execute(query, data)
    db.commit()

