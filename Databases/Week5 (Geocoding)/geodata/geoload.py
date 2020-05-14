import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False: #GoogleAPI service url
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data") #This is the typed search data.
count = 0
for line in fh:
    if count > 200 : #Data more than 200 will not be retrieved at once
        print('Retrieved 200 locations, restart to retrieve more')
        break

    address = line.strip() 
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try: #If exists in the database
        data = cur.fetchone()[0]   
        print("Found in database ",address)
        continue
    except:
        pass #No errors just move to next line

    parms = dict()  #EMBEDDING THE API KEY TO THE URL for access
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1 #keeping counts

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue
    #Checking the validity of data
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break
    #Entry to database sql command
    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit() #Commits to database
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5) #Every 10 retrieval 5 sec break

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
#memoryview helping to push the json data into database