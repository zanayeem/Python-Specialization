import sys
#Extractions of Weekdays
inputfile = input("Enter file name: ")
try:
    file = open(inputfile + ".txt")
except:
    print("File not found, enter a valid file name")
    sys.exit()
count=0
for line in file:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()  #Splitting the words in the line into a list
    #print(words[2]) #printing the weekdays
    email = words[1] #extracting the mail address
    print(email) #Printing the mail address
    count += 1   
print("There were", count, "lines in the file with From as the first word")

