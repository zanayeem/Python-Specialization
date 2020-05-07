#WEEK3
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Default notations
# mysock.connect(('data.pr4e.org',80)) #Establishing connection with server
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #Content url
# mysock.send(cmd) #Sending the command to get the content
# 
# while True:
#     data = mysock.recv(512) #Receiving the encoded data upto 512 characters
#     if len(data) < 1: break #If not data then break
#     print(data.decode()) #Decoding and print
# mysock.close() 
# # INITIALLY THERE WILL BE SOME METADATA FOLLOWED BY THE ACTUAL CONTENT

#ASSIGNMENT : TO post the details of the metadata or header information 

# #WEEK4
# #ALTERNATELY urlib makes it easier
# import urllib.parse , urllib.request , urllib.error
# file = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
# # for line in file:
# #     print(line.decode().strip())
#    
# #Making a dict of counts
# counts = dict()
# for line in file:
#     y = (line.decode().strip()) #DECODING FROM UTF8 to string
#     print(y)
#     for word in y.split(): #Spliting into words
#         counts[word] = counts.get(word,0) + 1 
# print(counts)

# #Using BeautifulSoup
import urllib.parse , urllib.request , urllib.error
from bs4 import BeautifulSoup as BS #LIBRARY FOR PARSING HTML DOCS

url = input("Enter the url link: ")
html = urllib.request.urlopen(url).read() #READING THE LINK DOCUMENT
print(html) #HTML file as coded
soup = BS(html , 'html.parser') #Create an object of BS to parse the doc

#Retrieve all of the anchor tabs
tags = soup('a') #finding the a tags 
for tag in tags:
    print(tag.get('href',None)) #href as in to find links ReGex eq: href="(.+)"