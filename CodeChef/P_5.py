loop = int(input())
for i in range(loop):
    X,Y = input().split()
    ans = 0
    if(int(X)>int(Y)):
        ans = int(X) - int(Y)
        print(ans)
    else:
        print('0')