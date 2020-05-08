# //////////////
import urllib.request
from bs4 import BeautifulSoup
url = input('Enter the URL: ')
count = int(input("Enter count: "))
position = int(input("Enter position: "))
for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')

    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x) #Inserting all the links
        y = tag.text #tag.conntents[0] 
        t.append(y) #Inserting all the names
    
    print (s[position-1]) #Link
    print (t[position-1]) #Name
    url = (s[position-1])
# /////////////
  


     
