"""Problem 2 (from codechef)
Chef's son wants to go on a roller coaster ride. 
The height of Chef's son is XX inches while 
the minimum height required to go on the ride is HH inches. 
Determine whether he can go on the ride or not  ."""
t = int(input())
for i in range(t):
    x = int(input())
    h = int(input())
    if (x >= h):
        print("YES")
    else:
        print("NO")