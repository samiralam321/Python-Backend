import sqlite3

connection = sqlite3.connect("users.db")

connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT
)
""")


connection.commit()

# what is row_factory : it makes database rows easier to use
# what is cursor ? : It executes SQL queries 
# what is connection? : It connects python to database




