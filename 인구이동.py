from collections import deque
N,L,R=map(int,input().split())
country=[]
for _ in range(N):
    country.append(list(map(int,input().split())))
country_visit=[[0]*N for _ in range(N)]

def make_union(y,x, num):
    people_sum=0
    union_sum=0
    dy=[-1,1,0,0]
    dx=[0,0,-1,1]
    bfs=deque()
    bfs.append([y,x])
    country_visit[y][x]=num
    while bfs:
        q=bfs.popleft()
        x=q[1]
        y=q[0]
        union_sum+=1
        people_sum+=country[y][x]
        people=country[y][x]
        for i in range(4):
            x_move=x+dx[i]
            y_move=y+dy[i]
            if x_move>=0 and x_move<N and y_move>=0 and y_move<N:
                if country_visit[y_move][x_move]==0:
                    if L<=abs(country[y_move][x_move]-people) and abs(country[y_move][x_move]-people)<=R:
                        
                        bfs.append([y_move,x_move])
                        country_visit[y_move][x_move]=num
    return people_sum//union_sum
    
def find_union(N):
    for i in range(N):
        for j in range(N):
            country_visit[i][j]=0
    start=0
    average=[0]
    for i in range(N):
        for j in range(N):
            if country_visit[i][j]==0:
                dy=[-1,1,0,0]
                dx=[0,0,-1,1]
                people=country[i][j]
                bfs=False
                for k in range(4):
                    x_move=j+dx[k]
                    y_move=i+dy[k]
                    if x_move>=0 and x_move<N and y_move>=0 and y_move<N:
                        if country_visit[y_move][x_move]==0:
                            if L<=abs(country[y_move][x_move]-people) and abs(country[y_move][x_move]-people)<=R:
                                
                                bfs=True
                                break
                if bfs:
                    start+=1
                    average.append(make_union(i,j,start))

    
    
    for i in range(N):
        for j in range(N):
            if country_visit[i][j]!=0:
                country[i][j]=average[country_visit[i][j]]
    
    return start

def turn():
    answer=0
    while find_union(N)!=0:
        answer+=1
    return answer

print(turn())