inputfile = input("Enter file name: ")
flist = list()
try:
    file = open(inputfile + ".txt")
except:
    print("file not found!")
    quit

for line in file:
    line = line.rstrip()
    for words in line.split():
        if words not in flist:
            flist.append(words)

flist.sort()
print(flist)   

# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# count=0
# for line in fh:
#      line = line.rstrip()
    
#      for word in line.split():
        
#         if word not in lst:
            
#             lst.append(word)
            
           

# 	


# lst.sort()
# print(lst)