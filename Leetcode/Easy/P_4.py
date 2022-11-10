"""Problem 4 -
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
strs = ["leetcode","leetcx","leetcsolve"]
result = ''

minlen = len(strs[0])
for i in range(1,len(strs)):                #calculating the minimum length of the list items
    minlen = min(minlen , len(strs[i]))

for i in range (minlen):                #iterating alphabates
    for s in strs:                  #iterating list items
        if i == len(s) or s[i] != strs[0][i]:
            break
    result += strs[0][i]
print(result)

# a = str(input())
# b = str(input())        #somry, this only accepts 2 input but in leetcode question we have to take a list
# length = 0
# if len(a)>len(b):
#     length = len(b)
# else:
#     length = len(a)

# same_pre = ''
# for i in range(length):
#     if a[i] == b[i]:
#         same_pre += a[i] 
#         print('.')
# if same_pre == '':
#     print('nothing same')
# else:
#     print('Longest common prefix is - ' + same_pre)