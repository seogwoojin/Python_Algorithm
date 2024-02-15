import copy
from collections import deque
N,M,K=map(int,input().split())

land=[[5]*(N+1) for _ in range(N+1)]
s2d2=[[]]
for i in range(N):
    s2d2.append([0]+list(map(int,input().split())))

tree=[deque() for _ in range(N+1)]
trees=[]
for _ in range(N+1):
    trees.append(copy.deepcopy(tree))
    
for i in range(M):
    x,y,z=map(int,input().split())
    trees[x][y].append(z)
    if len(trees[x][y])>1:
        trees[x][y]=deque(sorted(trees[x][y]))
        
    
for _ in range(K):
    for i in range(1,N+1):
        for j in range(1,N+1):
            for num in range(len(trees[i][j])):
                if land[i][j]>=trees[i][j][num]:
                    land[i][j]-=trees[i][j][num]
                    trees[i][j][num]+=1
                else:
                    plus=0
                    for k in range(len(trees[i][j])-1,num-1,-1):
                        plus+=trees[i][j][k]//2
                        trees[i][j].pop()
                    land[i][j]+=plus
                    break
    for i in range(1,N+1):
        for j in range(1,N+1):
            can=0
            for tree in trees[i][j]:
                if tree%5==0:
                    can+=1
            
            if can!=0: 
                dx=[-1,-1,-1,1,1,1,0,0]
                dy=[-1,0,1,-1,0,1,-1,1]
                for k in range(8):
                    my=i+dy[k]
                    mx=j+dx[k]
                    if mx>0 and mx<=N and my>0 and my<=N:
                        for t in range(can):
                            trees[my][mx].appendleft(1)
            land[i][j]+=s2d2[i][j]

    
answer=0
for i in range(1,N+1):
    for j in range(1,N+1):
        answer+=len(trees[i][j])
print(answer)
                