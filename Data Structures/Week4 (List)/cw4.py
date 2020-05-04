# x = list()
# x = ["google","IBM","Azure",]
# x.append("AWS")
# print(x)

# #loop and print
# for i in x:
#     print("The cloud service platforms are: " , i )
# print("The length of the list is ",len(x))

# #Slicing
# print("The most popular one is ", x[3])

# x.sort()
# print("The sorted list",x)

#Finding the average from taking inputs using LISTS!!!
# num_list = list()
# while True:
#     inp = input("Enter the numbers  to add and avg: ")
#     if inp == "done": 
#         break
#     else:
#         values = float(inp)
#         num_list.append(values)
    
# tot=sum(num_list)
# count = len(num_list)
# avg = tot/count      
# print("The sum is ",tot," & the average is ",avg)

# #Spliting strings
# abc= "England,Bangladesh,Australia,China,Italy,Spain,Italy,Spain,Italy,Spain,Spain,Spain,Spain"
# cab = abc.split(",")
# print (cab)  

#Extractions of Weekdays
# inputfile = input("Enter file name: ")
# try:
#     file = open(inputfile + ".txt")
# except:
#     print("file not found!")
#     quit

# for line in file:
#     line = line.rstrip()
#     if not line.startswith("From "):
#         continue
#     words = line.split()  #Splitting the words in the line into a list
#     #print(words[2]) #printing the weekdays
#     email = words[1] #extracting the mail address 
#     pieces = email.split("@") #Splitting on the basis of @
#     print(pieces[1]) #Extracting the mail client
# print("That's all")        

# a = [1,2,3]
# b = [4,5,6]
# c= a+b #appends in order
# print(c)