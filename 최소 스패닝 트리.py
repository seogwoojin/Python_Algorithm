import sys
input=sys.stdin.readline

V,E=map(int,input().split())

dist=[[False]*(V+1) for i in range(V+1)]
for _ in range(E):
    come=list(map(int,input().split()))
    dist[come[0]][come[1]]=come[2]
    dist[come[1]][come[0]]=come[2]

start=1
distance=[1000000]*(V+1)
distance[1]=0
already=[False]*(V+1)
answer=0

while True:
    
    already[start]=1
    answer+=distance[start]
    
    if False not in already[1:]:
        break
    
    for n in range(1,V+1):
        if not already[n] and dist[start][n]!=0:
            if distance[n]>dist[start][n]:
                distance[n]=dist[start][n]
    
    for n in range(1,V+1):
        if not already[n]:
            small=n
            temp=distance[n]
            break
    
    for num in range(small+1, V+1):
        if not already[num]:
            if temp>distance[num]:
                temp=distance[num]
                small=num
                
    start=small
    
    
print(answer)
    
            