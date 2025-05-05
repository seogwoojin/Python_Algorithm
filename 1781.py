import heapq

n=int(input())
work=[]
for _ in range(n):
    work.append(list(map(int,input().split())))
    
work.sort(key=lambda x: x[0])
hq = []
for w in work:
    day=w[0]
    reward=w[1]
    
    heapq.heappush(hq, w[1])
    
    if len(hq)>day:
        heapq.heappop(hq)
print(sum(hq))