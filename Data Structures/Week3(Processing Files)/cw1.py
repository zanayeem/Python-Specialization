# file=open("mbox.txt")
# count=0
# for line in file:
#     count= count+1
# print(count)

# file=open("mbox-short.txt")
# input= file.read()
# print(input[:40])

# file=open("mbox.txt")
# count=0
# count_total=0
# for line in file:
#     line=line.rstrip() #Strips of all the whitespace in between the lines
#     if line.startswith("From: "): #Selects line which stars with From: 
#         print(line)
#         count=count+1
#     count_total += 1
# print("Total lines: ", count_total)
# print("TOtal searched lines: ", count)

# #ALTERNATE OF THE ^ CODE:
# file=open("mbox.txt")
# count=0
# count_total=0
# for line in file:
#     line=line.rstrip() #Strips of all the whitespace in between the lines
#     if not line.startswith("From: "): #If line doesn't start with that go back up
#         continue
#     else: #If line starts with that print line
#         print(line)

# #Using in line
# file=open("mbox.txt")
# count=0
# count_total=0
# for line in file:
#     line=line.rstrip() #Strips of all the whitespace in between the lines
#     if not "@uct.ac.za" in line: #If line doesn't start with that go back up
#         continue
#     else: #If line starts with that print line
#         print(line)
        
# #PROMPT FILE NAME
# name= input("Enter the file name: ")
# file=open(name)
# count=0
# count_total=0
# for line in file:
#     line=line.rstrip() #Strips of all the whitespace in between the lines
#     if line.startswith("From: "): #Selects line which stars with From: 
#         print(line)
#         count=count+1
#     count_total += 1
# print("Total lines: ", count_total)
# print("TOtal searched lines: ", count)

#TRY and EXCEPT
# name= input("Enter the file name: ")
# try:
#     file=open(name)
# except:
#     print("The desired file cannot be found!!")
#     quit  

# count=0
# count_total=0
# for line in file:
#     line=line.rstrip() #Strips of all the whitespace in between the lines
#     if line.startswith("From: "): #Selects line which stars with From: 
#         print(line)
#         count=count+1
#     count_total += 1
# print("Total lines: ", count_total)
# print("TOtal searched lines: ", count)

# #Graded Assignments 1
# inputfile = input("Enter file name: ")
# try:
#     file = open(inputfile + ".txt")
# except:
#     print("file not found!")

# for line in file:
#     line = line.rstrip()
#     line = line.upper()
#     print(line)
        
# Use the file name mbox-short.txt as the file name
inputfile = input("Enter file name: ")
try:
    file = open(inputfile + ".txt")
except:
    print("file not found!")

count = 0 #Initializing all the variables
total = 0
zero_pos = 0
conf_no=0
for line in file:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count += 1 #Increasing count 
    zero_pos = line.find("0")  #Finding the position of 0 in every line
    conf_no = line[zero_pos:]  #Recording the numbers every loop
    total += float(conf_no) #Adding all the numbers

avg= total/count    #Averaging the sum of the values
print("Average spam confidence:", avg)





