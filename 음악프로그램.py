import sys
from collections import deque
input=sys.stdin.readline
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    buildTime=[0]+list(map(int,input().split()))
    beforeMax=[0]*(N+1)
    graph=[[]for _ in range(N+1)]
    weight=[0]*(N+1)
    for i in range(M):
        a,b=map(int,input().split())
        graph[a].append(b)
        weight[b]+=1

    W=int(input())
    queue=deque()

    for i in range(1,N+1):
        if weight[i]==0:
            queue.append(i)
    answer=[]
    while queue:
        now=queue.popleft()
        answer.append(now)
        buildSum=buildTime[now]
        for i in graph[now]:
            if beforeMax[i]<buildSum:
                beforeMax[i]=buildSum
            weight[i]-=1
            if weight[i]==0:
                queue.append(i)
                buildTime[i]=beforeMax[i]+buildTime[i]

    print(buildTime[W])