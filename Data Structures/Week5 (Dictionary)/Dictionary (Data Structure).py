# #import sys
# duffle_bag = dict()
# duffle_bag['money']= [10,45,50]
# duffle_bag['money'][2] = duffle_bag['money'][2] + 5 
# print(duffle_bag)

# duffle_bag = {'money': [26,35,33,55,66,66,65], 'gold': 25, 'gem': 55}
# print(duffle_bag)

# # Counting the occurance of names using a for and a conditional loop
# counts = dict()
# names = ['nayeem','navid','tamzid','navid','tamzid','ashik','tamzid','ashik','tajwar','ashik','tajwar']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] += 1
# print(counts)

# #ALTERNATE
# counts = dict()
# names = ['nayeem','navid','tamzid','navid','tamzid','ashik','tamzid','ashik','tajwar','ashik','tajwar']
# for name in names:
#     counts[name] = counts.get(name,0) + 1 #A method to do the if and else
# print(counts)

# #COUNTING FROM INPUTS
# counts = dict()
# inp = input("Enter your text here: ")
# words = inp.split()
# print("The splitted words: ",words)

# for word in words:
#     counts[word] = counts.get(word,0) +1
# print(counts)

#Retrieving keys and values
duffle_bag = {'money': [26,35,33,55,66,66,65], 'gold': 25, 'gem': 55}
print(duffle_bag.keys())
print(list(duffle_bag)) #Creates a list() from dict()
print(duffle_bag.values())
print(duffle_bag.items()) #Double values as items

for key,value in duffle_bag.items(): #Items can be used for TWO simultaneous iteration variables
    print(key,value)
