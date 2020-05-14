import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

#SQL command to search a query
cur.execute('''
SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X                      
''')
#Printing out the searched result [0] index 
print(cur.fetchone()[0])

# print(cur.fetchall()) #Fetches all relevant data as a list

