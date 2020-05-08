import xml.etree.ElementTree as ET
import urllib.request

url = input("Enter the url: ")
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_484189.xml"

html = urllib.request.urlopen(url).read() #READING THE LINK DOCUMENT
# print(html) #HTML file as coded

stuff = ET.fromstring(html)  #Load 
lst = stuff.findall('comments/comment') #Searching all

x = list()
for item in lst:
    print('Name', item.find('name').text)
    print('Count', item.find('count').text)
    x.append(int(item.find('count').text)) #Append the list with the counts
print(x)
maxify = sum (x)
print(maxify)



