import sqlite3

conn = sqlite3.connect('email-org-countdb2.sqlite') #Creates or connects with existing database
cur = conn.cursor() #The sql handler

cur.execute('DROP TABLE IF EXISTS Counts') #Drop table if any exists

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')  #Create COUNTS  table

fname = input('Enter file name: ') 
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)  #Opening the file to write to database
for line in fh: 
    if not line.startswith('From '): continue
    pieces = line.split()
    org = pieces[1]  #Extracting the org address with splitting
    parts = org.split('@') #Splitting @
    org = parts[1] #Extracting the organization domain
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) # "?" is a placeholder
    row = cur.fetchone() #Fetch only one row
    if row is None: #If row empty
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else: #If row exists 
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit() #Writing everything to database

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10' #Searching
print("Counts: ")
for row in cur.execute(sqlstr): #Extracting each row and printing
    print(str(row[0]), row[1]) 
    # count += row[1]
# print("The number of org per org.:",count)

cur.close() #CLOSE sqlite connection
