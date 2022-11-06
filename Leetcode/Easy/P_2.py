"""Problem 2
9. Palindrome Number - (ps: A number which is same when reversed like 121 -> 121)
Given an integer x, return true if x is a palindrome, and false otherwise.
"""
num = input()       #take input from user
str_num = str(num)      #make it to string
rev_num = "".join(reversed(str_num))        #reverse the string and assign it to rev_num
if(rev_num == str_num):     #if it is palindrome
    print("true")
else:       #if it is not palindrome
    print("false")