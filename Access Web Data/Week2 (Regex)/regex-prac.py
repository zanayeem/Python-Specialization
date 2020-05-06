import re
import sys

# re.search() is used instead of find() in regex
inp = input("Enter the name of the file: ")
if len(inp) < 1: inp = "mbox-short" 
try: 
    file = open(inp + ".txt")
except:
    print("File not found.")
    sys.exit()

# #REGEX SEARCH() method used just to find out.
# for line in file: 
#     line = line.rstrip()
#     if re.search("^From",line):  #USING A REGEX LIBRARY PART1 "^" means startswith
#         print(line)

#REGEX SPECIAL CHARACTERS
# " ^ " means startswith
# " * " means zero or more characters
# " \S " means match any non-whitespace character
# " + " means more 1 or more than 1 time
# " ? " means don't be greedy     
# () Help with the extraction process

# for line in file: 
#     line = line.rstrip()
#     if re.search("^X.*:",line):  #Starts with X then some chars and then :
#         print(line)

# for line in file: 
#     line = line.rstrip()
#     if re.search("^X-\S+:",line):  #Starts with 'X-' and follows this character dash pattern ends with :
#         print(line)

# #REGEX FINDALL() method is used to find and extract the required string
# x= "My 2 favourite numbers are 7 and 10."        
# y = re.findall("[0-9]+",x) 
# print(y)
# y = re.findall("[AEIOU]+",x)

# #GREEDY MATCHING
# x = "From: using the : character."
# y = re.findall("^F.+:",x)
# print("GREEDY-MATCHING",y)

# #NON-GREEDY MATCHING
# x = "From: using the : character."
# y = re.findall("^F.+?:",x)
# print("NON-GREEDY MATCHING",y)

# #EFFICIENT EMAIL EXTRACTION using Regex
# for line in file: 
#     line = line.rstrip()
#     if re.search("^From",line):  #USING A REGEX LIBRARY PART1 "^" means startswith
#         print(line)
#         email = re.findall("\S+.@.\S+",line) #1 or more non-blank chars then @ and the 1 or more non-blank chars
#         print(email)

# #Specified extraction process
# x = "From cwen@iupui.edu Thu Jan  3 16:34:40 2008 & From Jan nayeem123able@gmail.com"
# y = re.findall("^From (\S+.@.\S+)",x) #Only choosing the pattern immediately after From
# print(y)

# #Extracting the mail client from the email address
# x = "From cwen@iupui.edu Thu Jan  3 16:34:40 2008"
# y = re.findall("^From .*@([^ ]*)",x) #From space then extract mail client immediately after that
# print(y)

#FIND AND EXTRACT LAST PROBLEM!!!!
y =list()
for line in file: 
    line = line.rstrip()
    word = re.findall("^X-DSPAM-Confidence: ([0-9.]+)",line)  #Starts with 'X-DSPAM....' and extracts the floats as strings
    if len(word) != 1: continue #To filter out the not found
    # print(word)
    word=float(word[0]) #Converting them to floats   
    # print(word)
    y.append(float(word)) #appending them
maximum = max(y)    
print("Maximum: ",maximum)     