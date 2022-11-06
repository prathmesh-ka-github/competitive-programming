"""Problem 3 -
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example 1:

```Input: s = "III"
Output: 3
Explanation: III = 3.```

"""
roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
s = str(input())
i = 0
num = 0
while i < len(s):
    if i+1 < len(s) and s[i:i+2] in roman:      #I dont understand after this point :')
        num+=roman[s[i:i+2]]
        i+=2
    else:
        #print(i)
        num+=roman[s[i]]
        i+=1
print(num)