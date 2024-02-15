import sys
from itertools import combinations
input = sys.stdin.readline


N,M=map(int,input().split())

maps=[]
for i in range(N):
    maps.append(list(map(int,input().split())))
    
chick=[]
rooms=[]
for i in range(N):
    for j in range(N):
        if maps[i][j]==2:
            chick.append([i,j])
        elif maps[i][j]==1:
            rooms.append([i,j])

comb=[]

answer=10**6
for chi in combinations(chick, M):
    res=0
    for room in rooms:
        dist=[]
        for c in chi:
            dist.append(abs(room[0]-c[0])+abs(room[1]-c[1]))
        res+=min(dist)
    if answer>res:
        answer=res

print(answer)
    
       
    
    

    