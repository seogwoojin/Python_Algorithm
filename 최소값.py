import sys
from collections import deque
input=sys.stdin.readline
MAX=1000000000
sys.setrecursionlimit(10**6)

N,M,K=map(int,input().split())

lst=[]

for i in range(N):
    lst.append(int(input()))
    
num=1
k=0
while True:
    k+=num
    if(N<=num): break
    num=num*2
    

seg_tree=[[] for i in range(k+1)]

def maketree(start, end, node):
    if start==end: 
        seg_tree[node]=lst[start]
        return
    
    mid=(start+end)//2
    
    maketree(start, mid, node*2)
    maketree(mid+1, end, node*2+1)
    
    seg_tree[node]=seg_tree[node*2]+seg_tree[node*2+1]
    return

    
def findSumTree(start, end, node):
    lazyCheck(start, end, node)
    
    if start>b or end<a:
        return 0
    
    mid=(start+end)//2
    
    if a<=start and end<=b:
        return seg_tree[node]
    
    else:
        l=findSumTree(start, mid, node*2)
        r=findSumTree(mid+1, end, node*2+1)
        return l+r

def lazyCheck(start, end ,node):
    if lazy[node]!=0:
        seg_tree[node]+=(end-start+1)*lazy[node]
        if start!=end:
            lazy[node*2]+=lazy[node]
            lazy[node*2+1]+=lazy[node]
        lazy[node]=0
        
def updateTree(start, end, node, num):
    lazyCheck(start, end, node)
    if start>b or end<a:
        return
    if a<=start and end<=b:
        seg_tree[node]+=(end-start+1)*num
        if start!=end:
            lazy[node*2]+=num
            lazy[node*2+1]+=num
        return
    else:
        mid=(start+end)//2
        updateTree(start, mid, node*2, num)
        updateTree(mid+1, end, node*2+1, num)
        seg_tree[node]=seg_tree[node*2]+seg_tree[node*2+1]
        return 
    
        
lazy=[0]*(k+1)
maketree(0,N-1,1)

for i in range(M+K):
    command=list(map(int,input().split()))
    if command[0]==1:
        a,b=command[1]-1,command[2]-1
        updateTree(0,N-1, 1, command[3])
    else:
        a,b=command[1]-1, command[2]-1
        print(findSumTree(0, N-1, 1))
    print(lazy)
    print(seg_tree)