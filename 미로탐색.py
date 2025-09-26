from collections import deque
N,M = map(int,input().split())

miro=[]
for i in range(N):
    miro.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
check=[[False]*M for _ in range(N)]
queue=deque()
queue.append([0,0,1])
check[0][0]=True

while queue:
    now = queue.popleft()
    x=now[1]
    y=now[0]
    layer=now[2]

    if x==M-1 and y==N-1:
        print(layer)
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<M and ny>=0 and ny<N and check[ny][nx]==False and miro[ny][nx]:
            queue.append([ny,nx, layer+1])
            check[ny][nx]=True

