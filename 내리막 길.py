import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
M,N=map(int,input().split())

maps=[]
check=[[-1]*N for i in range(M)]
check[0][0]=1
for _ in range(M):
    maps.append(list(map(int,input().split())))
    
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def find_route(x,y):
    ans=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if nx>=0 and nx<N and ny>=0 and ny<M and maps[ny][nx]>maps[y][x]:
            if check[ny][nx]==-1:
                find_route(nx,ny)
            ans+=check[ny][nx]
    
    check[y][x]=ans

if M==1 and N==1:
    print(1)
    exit(0)
find_route(N-1,M-1)
print(check[M-1][N-1])