import sys

inp = input("Please enter the name of the file: ")
if len(inp) < 1: inp = "mbox-short"
try:
    file = open(inp + ".txt")
except:
    print("File not found")
    sys.exit()

count = dict()
for line in file:    
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        time_s = time.split(":")        
        for hour in time_s[0].split():
            count[hour] = count.get(hour,0) + 1
            # print(hour)
# print(count)

sorted_hours = list()
for k,v in count.items():   #Converted the dictionary to a list of tuples
    sorted_hours.append( (k,v) )
#print(sorted_hours)

sorted_hours = sorted(sorted_hours)  #Sorted the list asc to desc
#print(sorted_hours)

for k,v in sorted_hours: #Printing out the list of tuples separately
    print(k,v)