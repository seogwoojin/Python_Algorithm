T=int(input())
from collections import deque
for i in range(T):
    n=int(input())
    start_x,start_y=map(int,input().split())
    store=[]
    for i in range(n):
        store.append(list(map(int,input().split()))+[0])

    end_x,end_y=map(int,input().split())
    
    queue=deque()
    queue.append([start_x, start_y,1])
    
    cango=False
    while queue:
        now=queue.popleft()
        now_x=now[0]
        now_y=now[1]
        if abs(end_x-now_x)+abs(end_y-now_y)<=1000:
            cango=True
            break
        for st in store:
            if st[2]==0:
                s_x=st[0]
                s_y=st[1]
                if abs(s_x-now_x)+abs(s_y-now_y)<=1000:
                    queue.append(st)
                    st[2]=1
    
    if cango:
        print("happy")
    else:
        print("sad")