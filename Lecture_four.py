# info = {                                                           # Dictionary
#     "name" : "Deepak",
#     "Roll" : 19636,
#     "cgpa" : 9.1
# }
# print(info)
# print(info["name"])
# print(info["Roll"])
# print(info["cgpa"])
# info["name"] = "Deepak Kumar"
# print(info)
# info["Class"] = "B.tech"
# print(info)


# student = {
#     "name" : "Deepak",
#     "subject" : {
#        "phy" : 98,
#        "chem" : 96,
#        "maths" : 99,
#     }
# }
# print(student)
# print(student["subject"])
# print(student["subject"] ["chem"])

                                             
student = {
    "name" : "Deepak",
    "subject" : {
       "phy" : 98,
       "chem" : 96,
       "maths" : 99,
    }
}
# print(student.keys())
# print(list(student.keys()))
# print(student.values())
# print(list(student.values()))
# print(student.items())
# print(list(student.items()))
# print(student.get("name2"))       # No error Return    (None)
# print(student["name2"])           # Error Return    (iss line ke baad kuch bhi print nahi hoga)
# student.update({"City : Bihar"})
# print(student)


# first = {}
# print(type(first))   # empty dictionary
#                ##                                      set

# collection = {1, 2, 2, "ram", "sita", "ram", 3}
# print(collection)
# print(type(collection))
# print(len(collection))


# second = set()      # empty set 
# print(type(second))

                              # Set Method 
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(4)
# collection.add(4)
# collection.add("Deepak")
# collection.add((1,4,6,7))
# print(collection)
# collection.remove(3)
# print(collection)
# collection.clear()
# print(collection)

# collection = {"ram", "shyam", "mohan",1,3,4}
# print(collection.pop())             # pop means- kuch bhi print ho shakta hai


# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2))



# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.intersection(set2))
# print(set1)
# print(set2)


