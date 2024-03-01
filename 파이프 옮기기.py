from collections import deque
import copy
N=int(input())
room=[]
for i in range(N):
    room.append(list(map(int,input().split())))
floor=[[0,0,0] for _ in range(N)]
dp_room=[]
for i in range(N):
    dp_room.append(copy.deepcopy(floor))

queue=deque()
dp_room[0][1][0]=1
dp_check=[[0]*N for i in range(N)]
dp_check[0][1]=1
dp_check[0][0]=1
def dp(y,x):
    dp_check[y][x]=1
    top=0
    mid=0
    left=0
    
    if y>=2 and room[y-1][x]==0:
        if dp_check[y-1][x]==0:
            dp(y-1,x)
        top=dp_room[y-1][x][1]+dp_room[y-1][x][2]
    
    if y>=1 and x>=1 and room[y-1][x-1]==0 and room[y-1][x]==0 and room[y][x-1]==0:
        if dp_check[y-1][x-1]==0:
            dp(y-1,x-1)
        mid=sum(dp_room[y-1][x-1])
    
    if x>=2 and room[y][x-1]==0:
        if dp_check[y][x-1]==0:
            dp(y,x-1)
        left=dp_room[y][x-1][0]+dp_room[y][x-1][1]
    dp_room[y][x][2]=top
    dp_room[y][x][1]=mid
    dp_room[y][x][0]=left     
    return top+mid+left
    
if room[N-1][N-1]==1:
    print(0)
else:
    print(dp(N-1,N-1))