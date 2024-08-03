import sys
from collections import deque
import heapq

input=sys.stdin.readline
N,M=map(int,input().split())

graph=[[]for _ in range(N+1)]
weight=[0]*(N+1)

for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    weight[b]+=1

queue=[]

for i in range(1,N+1):
    if weight[i]==0:
        queue.append(i)
heapq.heapify(queue)
answer=[]
while queue:
    now=heapq.heappop(queue)
    answer.append(now)
    for i in graph[now]:
        weight[i]-=1
        if weight[i]==0:
            heapq.heappush(queue,i)
    
for a in answer:
    print(a, end=' ')