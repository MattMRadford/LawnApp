import sqlite3

connection = sqlite3.connect('database.db')
c = connection.cursor()

c.execute('''CREATE TABLE clients (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          address TEXT NOT NULL,
          phone TEXT NOT NULL,
          frequency TEXT NOT NULL)''')
connection.commit()
connection.close()