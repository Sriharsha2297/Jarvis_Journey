# List Comprehensions & Lambdas
# n [x*2 for x in range(10)]
# n Filtered: [x for x in nums if x > 5]
# n Dict comprehension
# n lambda: sort_key = lambda x: x['speed']
# n sorted() with key function

# my_list = [x*2 for x in range(10)]
# print(my_list)  

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# # my_list = filter(lambda x: x > 5, nums)
# my_list = [x for x in nums if x > 5]
# print(list(my_list)) 

# my_dict = {x: x**2 for x in range(5)}
# print(my_dict)

my_list = sorted([{'name': 'Robot1', 'speed': 5}, {'name': 'Robot2', 'speed': 3}], key=lambda x: x['speed'])
print(my_list)