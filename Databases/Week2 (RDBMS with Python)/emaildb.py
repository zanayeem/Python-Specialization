import sqlite3

conn = sqlite3.connect('emaildb.sqlite') #Creates or connects with existing database
cur = conn.cursor() #The sql handler

cur.execute('DROP TABLE IF EXISTS Counts') #Drop table if any exists

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')  #Create COUNTS  table

fname = input('Enter file name: ') 
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)  #Opening the file to write to database
for line in fh: 
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]  #Extracting the email address with splitting
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) # "?" is a placeholder
    row = cur.fetchone() #Fetch only one row
    if row is None: #If row empty
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else: #If row exists 
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit() #Writing everything to database

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10' #Searching

for row in cur.execute(sqlstr): #Extracting each row and printing
    print(str(row[0]), row[1]) 

cur.close() #CLOSE sqlite connection
