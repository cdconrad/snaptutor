import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

with open('schema.sql') as f:
    script = f.read()
    cur.executescript(script)

cur.execute("INSERT INTO textbooks (title, price) VALUES ('Snappy Software', 7.99)")
cur.execute("INSERT INTO textbooks (title, price) VALUES ('Snappy Data Management', 9.99)")
cur.execute("INSERT INTO prompts (TextbookID, reflection, msg) VALUES (1, 'This is a test reflection.', 'This is a test message.')")

connection.commit()
connection.close()