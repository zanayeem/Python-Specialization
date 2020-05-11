import sqlite3

conn = sqlite3.connect('mydb.sqlite')
cur = conn.cursor()

# cur.execute('''
# CREATE TABLE Ages ( 
#   name VARCHAR(128), 
#   age INTEGER
# )            
# ''')

cur.execute('''
INSERT INTO Ages (name, age) VALUES ('Demetrius', 26);
''')