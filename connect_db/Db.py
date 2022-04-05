import mailbox
import mysql.connector

db = mysql.connector.connect(
    host= '127.0.0.1',
    port='8889',
    database= 'pythondb',
    user= 'root',
    password = 'root'
)


cursor= db.cursor()

def getAllUsers():
    query = 'SELECT * FROM user'
    cursor.execute(query)
    return cursor.fetchall()


def getUser(id: int):
    query = ('SELECT * FROM user WHERE id = %s')
    cursor.execute(query, (id,))
    return cursor.fetchone()


def createUser(firstname: str, lastname: str, email: str, password: str):
    query = 'INSERT INTO user (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)'
    cursor.execute(query, (firstname, lastname, email, password))
    db.commit()
    return cursor.lastrowid

def updateUser(firstname: str, lastname: str, email: str, password: str, id: int):
    query = 'UPDATE user SET (firstname, lastname, email, password) VALUES (%s, %s, %s, %s) WHERE id = %s'
    cursor.execute(query, (firstname, lastname, email, password, id))
    db.commit()
    return


print(createUser("Test", "Test2", "test@test", "azert"))


db.close()