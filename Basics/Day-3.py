# # Looping through a range of numbers
# for i in range(1, 10):
#     while i<6:
#         print(i)
#         i=i+1

# # Looping through a list
# for item in ['apple', 'orange', 'banana']:
#     print(item)

# #countdown timer using while loop
# import time
# countdown = 10 
# while countdown > 0:
#     print(countdown)
#     time.sleep(1)  # Wait for 1 second
#     countdown -= 1

# #simple way wothout using time module
# countdown = 10
# while countdown > 0:
#     print(countdown)
#     countdown -= 1  

#print multiplication table
for i in range(1, 3):
    print ("Multiplcatin table of ",i)
    while i<11:
        print (i,"*",i,"=",i*i)
        i=i+1

#better way to print multiplication table
for i in range(1, 3):
    print ("Multiplcatin table of ",i)
    for j in range(1, 11):
        print (i,"*",j,"=",i*j)
