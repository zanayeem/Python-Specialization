# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:31:32 2020

@author: Zannatun Nayeem
"""
import sys
inp = input("Enter the name of your file: ")
try:
    file = open(inp + ".txt")
except:
    print("File not found")
    sys.exit()

counts = dict() 
for line in file:
    words = line.split() #Splitting lines and storing the words
    for word in words:
        counts[word] = counts.get(word,0) + 1 #keeping count of word occurence
#print(counts) #Dictionary prints
 
bigCount = None
bigWord = None
for word,count in counts.items():
    if bigCount == None or count > bigCount:
        bigWord = word
        bigCount = count
print(bigWord,bigCount)        

    
