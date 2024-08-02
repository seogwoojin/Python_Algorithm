num=list(map(int,input().split()))
num.pop()

def getDistance(start, end):
    if start==0:
        return 2
    elif abs(start-end)==2:
        return 4
    elif start==end:
        return 1
    else:
        return 3

dp=[[[0]*5 for _ in range(5)] for _ in range(len(num))]

if not num:
    print(0)
    exit(0)
first=num[0]
dp[0][first][0]=2
dp[0][0][first]=2

for i in range(1, len(num)):
    next=num[i]
    for x in range(5):
        for y in range(5):
            if dp[i-1][x][y]!=0:
                print(i-1, x, y)
                if next!=y:
                    if dp[i][next][y]==0:
                        dp[i][next][y]=dp[i-1][x][y]+getDistance(x,next)
                    elif dp[i][next][y]>dp[i-1][x][y]+getDistance(x,next):
                        dp[i][next][y]=dp[i-1][x][y]+getDistance(x,next)
                if next!=x:
                    if dp[i][x][next]==0:
                        dp[i][x][next]=dp[i-1][x][y]+getDistance(y,next)
                    elif dp[i][x][next]>dp[i-1][x][y]+getDistance(y,next):
                        dp[i][x][next]=dp[i-1][x][y]+getDistance(y,next) 


answer=float('inf')
for i in range(5):
    for j in range(5): 
        if dp[len(num)-1][i][j]!=0 and dp[len(num)-1][i][j]<answer:
            answer=dp[len(num)-1][i][j]

print(answer)