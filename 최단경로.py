import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
V,E=map(int,input().split())
K=int(input())

maps=[[] for _ in range(V+1)]

for i in range(E):
    u,v,w=map(int,input().split())
    c=True
    for i in maps[u]:
        if i[0]==v:
            if i[1]>w:
                i[1]=w
            else:
                c=False
    if c:
        maps[u].append([v,w])

ans=[-1]*(V+1)
lst=[]
ans[K]=0
def start(u, min):
    here=ans[u]
    check=maps[u]
    for k in range(len(check)):
        now=check[k]
        n=now[0]
        num=now[1]
        if ans[n]==-1:
            ans[n]=num+here
        elif ans[n]>num+here:
            ans[n]=num+here
    
    next=[-1,-1]
    for j in range(1,V+1):
        if ans[j]>min:
            next[1]=ans[j]
            next[0]=j
            break
    if next[0]==-1:
        return
    
    for t in range(j+1,V+1):
        if ans[t]>min and ans[t]<next[1]:
            next[0]=t
            next[1]=ans[t]
    start(next[0], next[1])
    
        
start(K,0)

for i in ans[1:]:
    if i==-1:
        print('INF')
    else:
        print(i)