# f = open ("file.txt","r")                 #Read
# data = f.read()
# print(data)
# f.close()


# f = open ("file.txt","r")              
# data = f.read(6)
# print(data)
# f.close()


# f = open ("file.txt","r")              
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# f.close()

# f = open ("demo.txt","w")                    #Write
# f.write("how are you")
# f.close()


# f = open ("file.txt","w") 
# f.write("Hello, how are you")
# f.close()


# f = open ("file.txt","a") 
# f.write("\n Hello, how are you")
# f.close()


# f = open ("file.txt","r+")              #overwrite
# f.write("you")
# f.close()


# f = open ("file.txt","w+")                 # truncated    (kuch bhi print nahi hoga)
# print(f.read())
# f.close()


# f = open ("demo.txt","a+")              # not overwrite
# f.write("\nyou")
# f.close()


# with open ("demo.txt", "r") as f:
#     data = f.read()
#     print(data)


# with open ("demo.txt", "w") as f:  
#      f.write("new data")


# import os                                 #remove the file
# os.remove("demo.txt")


# f = open ("newfile.txt","w")
# f.write("Deepak kumar \nAge=19 \nCourse=b.tech(CSE)")
# f.close()


# with open ("newfile.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("Deepak kumar", "Ram")
# print(new_data)


# with open ("newfile.txt", "r") as f:           # error
#     data = f.read()
# new_data = data.replace("Deepak kumar", "Ram")

# with open ("newfile.txt", "r") as f:
#     f.write(new_data)


# word = "Age" 
# with open ("newfile.txt", "r") as f:
#      data = f.read()
#      if(word in data):
#          print("Found")
#      else :
#          print("not found")
        
    
# def check_for_line():                                      #(Not Understand)
#     word = "Course"
#     line_no = 1   
#     with open("newfile.txt", "r") as f:
#         data = f.readline()        
#         while data:    
#             if word in data: 
#                 print(line_no)
#                 return line_no       
#             data = f.readline()  
#             line_no += 1      
#     return -1  
# result = check_for_line()
# if result == -1:
#     print("Word not found in file")


# f = open("demo.txt","r")
# data = f.read()
# print(data)0
# f.close()



with open("newfile.txt") as f:
    lines = f.readlines()
lineno = 1 
for line in lines:   
    if("python" in line):
        print(f"yes python is there. Line :{line}")
        break
    lineno +=1
else:
    print("python is not there")