from collections import deque
N,M=map(int,input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    cheese[x][y]=3
    queue.append([x,y])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if mx>=0 and mx<N and my>=0 and my<M:
                if cheese[mx][my]==0:
                    cheese[mx][my]=3
                    queue.append([mx,my])
            
        

cheese=[]

for i in range(N):
    cheese.append(list(map(int,input().split())))

bfs(0,0)
answer=0
while True:
    stage=[]
    for i in range(N):
        for j in range(M):
            if cheese[i][j]==1:
                temp=0
                for t in range(4):
                    if cheese[i+dx[t]][j+dy[t]]==3:
                        temp+=1
                if temp>=2:
                    stage.append([i,j])
    if not(stage):
        print(answer)
        break
    
    answer+=1
    for x,y in stage:
        cheese[x][y]=3
        for i in range(4):
            if cheese[x+dx[i]][y+dy[i]]==0:
                bfs(x+dx[i],y+dy[i])
    
    noCheese=True
    for line in cheese:
        if 1 in line:
            noCheese=False
            break
        
    if noCheese:
        print(answer)
        break    