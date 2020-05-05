# (x,y) = (99,'abstract')
# print(x,y)

#items() returns a list of tuples in dict() data structure
d = dict()
d = {'a': 25 , 'c': 55, 'b':2 }
for key,value in d.items():
    print(key,value)

print(d.items()) #List of tuples
print(d)    #Dictionary
print(sorted(d.items())) #Sorting

for key,value in sorted(d.items()): #loopping and printing by sorting
    print(key,value)
    
#Comparing in tuples
(1,3,5) < (2,4,6) #Only compares the first one in position
(1,3,5) < (1,4,6) #If first one is equals then check for the next position and continues similarly
(1,5,5) < (1,4,6) #Returns FALSE

#Sort by values
tmp = list()
for key,value in d.items():
    tmp.append( (value,key) ) #list can only take 1 arguements so sending them as tuple
print("Before sorting", tmp)

tmp = sorted(tmp, reverse=True) #sorting in descending order
print("After sorting",tmp)

for key,value in tmp[:10]: #Printing them separately
    print(key,value)