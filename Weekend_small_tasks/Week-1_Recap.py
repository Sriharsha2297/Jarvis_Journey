# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

numbers = input("Enter numbers separated by commas: ")
result = numbers.split(",")
#
target = int(input("Enter the target number: "))
print ("Input list:", result)
print ("Target number:", target)
x = len(result)
print ("Length of the list:", x)

for i in range(x):
    for j in range(i+1, x):
        if int(result[i]) + int(result[j]) == target:
            print ("Indices of the two numbers that add up to the target:", [i, j]) 
            print ("The two numbers that add up to the target:", [result[i], result[j]])
