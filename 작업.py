import sys
from collections import deque
import heapq

input=sys.stdin.readline
N=int(input())

graph=[[]for _ in range(N+1)]
weight=[0]*(N+1)
tasks=[0]*(N+1)
smallTime=[0]*(N+1)
for i in range(N):
    ints=list(map(int,input().split()))
    tasks[i+1]=ints[0]
    for j in range(ints[1]):
        graph[ints[j+2]].append(i+1)
        weight[i+1]+=1
queue=deque()

for i in range(1,N+1):
    if weight[i]==0:
        smallTime[i]=tasks[i]
        queue.append(i)
while queue:
    now=queue.popleft()
    for i in graph[now]:
        weight[i]-=1
        if smallTime[now]+tasks[i]>smallTime[i]:
            smallTime[i]=smallTime[now]+tasks[i]
        if weight[i]==0:
            queue.append(i)
    
print(max(smallTime))