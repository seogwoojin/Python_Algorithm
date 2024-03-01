T=int(input())
for _ in range(T):
    n=int(input())
    num=[]
    for i in range(2):
        num.append(list(map(int,input().split())))
        
    dp=[[0]*n for i in range(2)]
    dp[0][0]=num[0][0]
    dp[1][0]=num[1][0]
    for i in range(1,n):
        for k in range(2):
            if k==0:
                under=dp[1][i-1]
                top=dp[0][i-1]
                now=num[0][i]
                if top>=now+under:
                    dp[0][i]=top
                else:
                    dp[0][i]=now+under
            else:
                under=dp[1][i-1]
                top=dp[0][i-1]
                now=num[1][i]
                if under>=now+top:
                    dp[1][i]=under
                else:
                    dp[1][i]=now+top
    print(max(dp[0][n-1], dp[1][n-1]))                