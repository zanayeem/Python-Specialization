import xml.etree.ElementTree as ET #XML extraction library
import sqlite3 

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor() #Handler for SQL

# Make some fresh tables using executescript()
#With script multiple SQL commands can be executed at once
cur.executescript('''  
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

#3 New tables are added on the databases

fname = input('Enter file name: ') #Importing the xml for inserting data
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key): #Looking up in an entry whether that key exists or not
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname) #Parsing the XML File
all = stuff.findall('dict/dict/dict') #Findall data in dict/dict/dict
print('Dict count:', len(all))
for entry in all: #All dicts of data one by one
    if ( lookup(entry, 'Track ID') is None ) : continue #if no entry found
    #else:
    name = lookup(entry, 'Name') 
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None : #All fields needed
        continue

    print(name, artist, album, count, rating, length)
    #Inserting artist name
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    #
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0] #Get one row and then first item ie ID
    #Inserting Album name with artist_id foreign key
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0] #Get one row and then first item ie ID
    #Inserting Track info with foreign key album_id
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ? )''', 
        ( name, album_id, length, rating, count ) )

    conn.commit()
