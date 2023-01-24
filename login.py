import getpass
import hashlib
import mysql.connector

connection = mysql.connector.connect(
    host = '192.168.8.2',
    user = '5infgr7',
    password = '5infgr7',
    db = '5infgr7_pizzaDB'
)
print(connection.is_connected())

username = input("Username: ")
password = getpass.getpass()
hash_object = hashlib.sha256()
hash_object.update(password.encode())
hash_value = hash_object.hexdigest()
print(hash_value)
cur = connection.cursor()
query = """
    INSERT INTO users (username,password)
    VALUES (%s,%s);
"""
cur.execute(query,(username,hash_value))
connection.commit()
