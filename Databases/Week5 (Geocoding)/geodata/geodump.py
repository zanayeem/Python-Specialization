import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations') #LOCATION has (address,geodata)
fhand = codecs.open('where.js', 'w', "utf-8") #Codec for JS is UTF8,write
fhand.write("myData = [\n")
count = 0
for row in cur :
    data = str(row[1].decode()) #GEODATA
    try: js = json.loads(str(data))
    except: continue

    if not('status' in js and js['status'] == 'OK') : continue #Validity
    #EXTRACTING LAT ,LONG, FORMATTED ADDRESS
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    try :
        print(where, lat, lng)

        count = count + 1 #Counting the number of records
        if count > 1 : fhand.write(",\n") #Writing in Where.js
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output) #Sending to where.js
    except:
        continue

fhand.write("\n];\n")#Writing is whre.js formatting
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

