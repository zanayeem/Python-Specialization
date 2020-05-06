import re
import sys

# re.search() is used instead of find() in regex
inp = input("Enter the name of the file: ")
if len(inp) < 1: inp = "regex_sum_484185" 
try: 
    file = open(inp + ".txt")
except:
    print("File not found.")
    sys.exit()

mylist = list()
for line in file:
    line = line.rstrip()
    #print(line)
    numbers = re.findall("[0-9]+",line) #Finding all the numbers
    if len(numbers) <= 0: continue #If in a line there is no numbers skip it
    # print(numbers) #Checking the list of numbers per line
    # print(len(numbers))  #Checking the length of that list
    x = len(numbers) #saving the length for the loop to run
    for i in range(x): 
        print(numbers[i-1])  #index -1 so that it starts from [0]
        mylist.append(int(numbers[i-1])) #Appending the numbers in to the list separately and not as list
print(mylist)
maxi = sum(mylist) #Summing the values in the list
print(maxi) 


