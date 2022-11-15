"""Problem 6 - 
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

    Input: s = "()"
    Output: true

Example 2:

    Input: s = "()[]{}"
    Output: true

Example 3:

    Input: s = "(]"
    Output: false
"""
closing = ")}]"

# for i in s[::2]:
#     if i == i+1:
#         print("nailed it!!!")

# length = len(s)
# for letter in s[0:length:2]:
#     for nxtletter in s[1::2]:                                 Lots of failed attemps
#         print("letter " + letter)
#         print("next letter " + nxtletter)
#         print("  ")

# for i in range (0, len(s), 2):
#     for j in closing:
#         if s[i] == j:
#             print("Paranthesis valid")


#!now using a datastructure (stack FILO)
s = "{}(){[]}[]"
stack = []
lookup = {")":"(" , "}":"{" , "]":"["}

for bracket in s:
    if bracket in lookup.values():
        stack.append(bracket)
    elif stack and lookup[bracket] == stack[-1]:
        stack.pop()
    else:
        print("false")
if stack == []:
    print("true")
else:
    print("false")
print("\n" * 8)