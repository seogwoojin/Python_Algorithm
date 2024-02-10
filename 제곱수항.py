N=int(input())
import math
dp=[0]*(N+1)

for i in range(1,N+1):
    if math.sqrt(i).is_integer():
        dp[i]=1
    else:
        dp_list=[]
        for j in range(1,int(math.sqrt(i))+1):
            dp_list.append(dp[j*j]+dp[i-j*j])
        dp[i]=min(dp_list)
print(dp[N])

