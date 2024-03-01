from collections import deque
N,M=map(int,input().split())

land=[]
for i in range(N):
    land.append(list(map(int,input().split())))
    
def check_land(land):
    union=[[0]*M for _ in range(N)]
    queue=deque()
    for i in range(N):
        for j in range(M):
            if land[i][j]!=0:
                queue.append([i,j])
                union[i][j]=1
                break
        if queue:
            break
        
    if not(queue):
        return 0
    while queue:
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        y,x=queue.popleft()
        
        for n in range(4):
            mx=x+dx[n]
            my=y+dy[n]
            if mx>=0 and mx<M and my>=0 and my<N:
                if land[my][mx]!=0 and union[my][mx]==0:
                    queue.append([my,mx])
                    union[my][mx]=1
    
    find=False
    for i in range(N):
        for j in range(M):
            if land[i][j]!=0 and union[i][j]==0:
                find=True
                break
            
    
    if find==True:
        return 1
    else:
        return 2
    
def change_land():
    global land
    
    melt=[[0]*M for i in range(N)]
    for i in range(N):
        for j in range(M):
            if land[i][j]!=0:
                dx=[-1,1,0,0]
                dy=[0,0,-1,1]
                for num in range(4):
                    mx=dx[num]+j
                    my=dy[num]+i
                    if mx>=0 and mx<M and my>=0 and my<N and land[my][mx]==0:
                        melt[i][j]+=1
    
    for i in range(N):
        for j in range(M):
            if land[i][j]!=0:
                if land[i][j]-melt[i][j]>=0:
                    land[i][j]-=melt[i][j]
                else:
                    land[i][j]=0
    
    #change finish
K=0
answer=0
while True:
    K+=1
    change_land()
    num=check_land(land)
    if num==0:
        K=0
        break
    elif num==1:
        break
print(K)