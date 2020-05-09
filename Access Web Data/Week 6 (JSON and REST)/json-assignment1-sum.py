import urllib.request
import json

url = input("Enter the JSON url: ")
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_484190.json"

data = urllib.request.urlopen(url) #Retrieving utf8 data 
data = data.read().decode() #Decoding to strings from utf8

js = json.loads(data) #Loading the json data
print(json.dumps(js, indent=4)) #Printing with proper indents

counts = list()
for item in js['comments']: #Catching items inside the comments list
    print(item['count']) #Printing only the counts
    counts.append(int(item['count'])) #Pushing them to a list
print(counts) 

maxify = sum(counts)
print("The sum of the counts:",maxify)