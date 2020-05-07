# #Using BeautifulSoup
import urllib.parse , urllib.request , urllib.error
from bs4 import BeautifulSoup as BS #LIBRARY FOR PARSING HTML DOCS

url = input("Enter the url link: ")
html = urllib.request.urlopen(url).read() #READING THE LINK DOCUMENT
# print(html) #HTML file as coded
soup = BS(html , 'html.parser') #Create an object of BS to parse the doc

total = [] #or list()
tags = soup('span')
for tag in tags:
    # print(tag) #Printing out only the span tags
    # print(tag.contents[0]) #Printing out the contents ie. numbers
    conv = int(tag.text) #Converting to integer
    total.append(conv) #Appending the numbers to a list
# print (total)
summify = sum(total)
print(summify)

    
    
# ... GUIDE TO EXTRACT PARTS OF A CERTAIN TAG
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#    # Look at the parts of a tag
#    print 'TAG:',tag
#    print 'URL:',tag.get('href', None)
#    print 'Contents:',tag.contents[0] or tag.text
#    print 'Attrs:',tag.attrs    