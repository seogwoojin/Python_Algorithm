import sys
import heapq

input=sys.stdin.readline

n=int(input())
tasks=[]
for i in range(n):
    tasks.append(list(map(int,input().split())))

tasks.sort(key= lambda x:x[1])

lst=[]
for p,d in tasks:
    if len(lst)<d:
        heapq.heappush(lst, [p,d])
    
    elif len(lst)==d:
        if lst[0][0]<p:
            heapq.heappop(lst)
            heapq.heappush(lst, [p,d])

answer=0

for p,d in lst:
    answer+=p
print(answer)


