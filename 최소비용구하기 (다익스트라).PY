import heapq
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
distance=[[-1]*(n+1) for i in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    if distance[a][b]!=-1:
        if distance[a][b]>c:
            distance[a][b]=c
    else:
        distance[a][b]=c
    
start,end=map(int,input().split())

def dijkstra(num):
    global end,n
    mst=[10**9]*(n+1)
    mst[start]=0
    
    if num==end:
        return
    queue=[]
    heapq.heappush(queue, [mst[num], num])
    
    while queue:
        cur_cost, cur_loc=heapq.heappop(queue)
        
        if mst[cur_loc]<cur_cost:
            continue
        mst[cur_loc]=cur_cost
        for i in range(1,n+1):
            if distance[cur_loc][i]!=-1:
                endpoint=i
                cost=distance[cur_loc][i]
                if mst[endpoint]>cur_cost+cost:
                    mst[endpoint]=cur_cost+cost
                    heapq.heappush(queue, [cur_cost+cost,endpoint])
        
    return mst[end]
        
print(dijkstra(start))