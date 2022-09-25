import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE PASS(name varchar(30),regno number(15),phone number(12),dept varchar(25),year number(1),purpose varchar(100))
''')
conn.commit()
conn.close()