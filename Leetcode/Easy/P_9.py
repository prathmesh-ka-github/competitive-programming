"""Problem 9 -
217. Contains Duplicate
Given an integer array nums, 
return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
#!      using dont know tf is this

# nums = [1,2,3,4]
# ans = 0
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if (nums[i] == nums[j]):
#             ans = 1
#             break
#         else:
#             ans = 0
#     if(ans == 1):
#         break
# if (ans == 1):
#     print('True')
# else:
#     print('False')


#!      using loop iteration
# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if (nums[i] == nums[j]):
#                     ans = 1
#                     break
#                 elif(nums[i] != nums[j]):
#                     ans = 0
#             if(ans == 1):
#                 break
#         if (ans == 1):
#             print('true')
#         elif(ans == 0):
#             print('false')

#     containsDuplicate(0, [0,4,5,0,3,6])


#!      using count()

nums = [1,2,3,4,5,1]
ans = 0
for i in nums:
    ans = nums.count(i)
    if(ans > 1 ):
        break
if (ans > 1):
    print('true')
else:
    print('false')