import sys
import heapq
input=sys.stdin.readline

V,E=map(int,input().split())

dist=[[] for i in range(V+1)]
for _ in range(E):
    come=list(map(int,input().split()))
    dist[come[0]].append([come[1],come[2]])
    dist[come[1]].append([come[0],come[2]])

start=1
distance=[1000000]*(V+1)
distance[1]=0
check=0
already=[False]*(V+1)
answer=0
queue=[[0,1]]

while queue:
    check+=1
    small=heapq.heappop(queue)
    start=small[1]
    already[start]=True
    answer+=small[0]
    
    if check==V:
        break
    
    for n,ndist in dist[start]:
        if not already[n]:
            heapq.heappush(queue,[ndist,n])
    while True:
        small=heapq.heappop(queue)
        if already[small[1]]==False:
            heapq.heappush(queue, small)
            break
    
print(answer)