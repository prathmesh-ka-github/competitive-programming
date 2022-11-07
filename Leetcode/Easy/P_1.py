"""Problem 1 - 
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
print('Problem 1 - Two sum')
class Solution:
    def twoSum(nums, target):
        for i in range(len(nums)):      #loop that iterates from i to length of the array
            for j in range(i + 1, len(nums)):       #loop that iterates j from i+1(i.e the next number) to length of the array
                if nums[j] == target - nums[i]:     #if statement for checking and prints the combo 
                    print([i,j])        #lmao use return if you pasting this to leetcode terminal
    twoSum([2,7,11,15], 9)