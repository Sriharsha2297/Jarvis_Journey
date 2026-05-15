#Lists, Tuples & Dictionaries

#list 

my_list = [8,7,1,2,3,4,5,6] 
# print (my_list)
# print (my_list[0])

#Append a value to the list
# append_value = 7
# my_list.append(append_value)
# print (my_list)

#Remove a value from the list
# ReMove_value = 3
# my_list.remove(ReMove_value)
# my_list.remove(4)
# print (my_list)

#Sort the list
# my_list.sort()
# print(my_list)

#pop a value from the list
#Removed_value = my_list.pop()
# my_list.pop()
# print (my_list)
#print (Removed_value)

#tuple 
# my_tuple = (1,2,3,4,5)
# print (my_tuple)  


#dictionary
my_dict = {"name": "Fanuc", "Size": "210", "Speed": "355M/min"}
print (my_dict)
#Accessing a value from the dictionary
print (my_dict["name"])
print (my_dict.get("Size"))
#Adding a new key-value pair to the dictionary
my_dict["Color"] = "Yellow"    
print (my_dict)
#Removing a key-value pair from the dictionary
my_dict.pop("Speed")
print (my_dict)
