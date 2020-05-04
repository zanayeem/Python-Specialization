import sys
inp = input("Enter the name of your file: ")
if len(inp) < 1 : inp = "mbox-short"
try:
    file = open(inp + ".txt")
except:
    print("File not found")
    sys.exit()

counts = dict()
for line in file:
    if line.startswith("From: "):
        words = line.split()
        #print(words)
        wordsAt1 = words[1]
        #print(wordsAt1)
        for word in wordsAt1.split(): #VERYY IMPORTANT!!!!! (Since we are not being able to use the word variable directly we split the wordsAt1)
            counts[word] = counts.get(word,0) + 1 #Taking words instead of word because the [1] index contains only the email addresses which we need.
#print(counts)

#Finding the highest occurence
bigCount = None
bigWord = None
for key,value in counts.items():
    if bigCount == None or value > bigCount:
        bigCount = value
        bigWord = key
print(bigCount,bigWord)
