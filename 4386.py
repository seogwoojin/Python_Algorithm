import sys
import math
import heapq
input=sys.stdin.readline

n=int(input())
star=[]
for i in range(n):
    star.append(list(map(float,input().split())))

dist=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        num=math.sqrt(abs(star[i][0]-star[j][0])**2+abs(star[i][1]-star[j][1])**2)
        num=round(num,3)
        dist[i][j]=num
        dist[j][i]=num

start=0
distance=[1000000]*n
distance[0]=0
check=0
already=[False]*n
answer=0
queue=[[0,0]]
while queue:
    check+=1
    small=heapq.heappop(queue)
    start=small[1]
    already[start]=True
    answer+=small[0]
    
    if check==n:
        break
    
    for num in range(n):
        if not already[num]:
            heapq.heappush(queue,[dist[start][num],num])
    
    while True:
        small=heapq.heappop(queue)
        if already[small[1]]==False:
            heapq.heappush(queue, small)
            break
    
print(round(answer,3))