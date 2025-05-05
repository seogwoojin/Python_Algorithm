import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
N=int(input())
M=int(input())

dp=[[] for _ in range(N+1)]
beforeMax=[0]*(N+1)
graph=[[]for _ in range(N+1)]
weight=[0]*(N+1)
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    weight[b]+=1


start,end=map(int,input().split())
queue=deque()
queue.append(start)
dp[start].append([0,0])
while queue:
    now=queue.popleft()
    max_time=dp[now][0][0]
    for addr, spendTime in graph[now]:
        if not dp[addr]:
            dp[addr].append([max_time+spendTime,now])
        elif dp[addr][0][0]<max_time+spendTime:
            dp[addr]=[]
            dp[addr].append([max_time+spendTime,now])
        elif dp[addr][0][0]==max_time+spendTime:
            dp[addr].append([max_time+spendTime,now])
        weight[addr]-=1
        if weight[addr]==0:
            queue.append(addr)
checked=[False]*(N+1)
checked[start]=True
def get_route(num):
    if checked[num]==True:
        return 0
    elif len(dp[num])==1:
        checked[num]=True
        return 1+get_route(dp[num][0][1])
    else:
        checked[num]=True
        get_sum=0
        for a,b in dp[num]:
            get_sum=get_sum+get_route(b)
        return len(dp[num])+get_sum
answer=0
print(dp[end][0][0])
print(get_route(end))