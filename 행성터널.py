import sys
from collections import deque
import heapq
input=sys.stdin.readline
def get_line(planets,num):
    for n in range(N-1):
        planet=planets[n]
        next_planet=planets[n+1]
        
        dist=abs(next_planet[num]-planet[num])
        line[planet[0]].append([next_planet[0]]+[dist])
        line[next_planet[0]].append([planet[0]]+[dist])
def prim(start):
    checked=[-1]*N
    checked[start]=0
    answer=0
    hq=[]
    
    while True:
        for l in line[start]:
            if checked[l[0]]==-1:
                heapq.heappush(hq, [l[1],l[0]])
        start_change=False
        while hq:
            first=heapq.heappop(hq)
            if checked[first[1]]==-1:
                answer+=first[0]
                checked[first[1]]=0
                start=first[1]
                start_change=True
                break
        if start_change==False:
            break
    
    return answer

          
      

N=int(input())

planets=[]
for i in range(N):
    planets.append([i]+list(map(int,input().split())))

if N==1:
    print(0)
    exit(0)
line=[[] for _ in range(N)]


planets.sort(key=lambda x:x[1])
get_line(planets,1)

planets.sort(key=lambda x:x[2])
get_line(planets,2)

planets.sort(key=lambda x:x[3])
get_line(planets,3)      

print(prim(0))

