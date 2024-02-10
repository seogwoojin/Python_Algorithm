from collections import deque
F,S,G,U,D=map(int,input().split())

visit=[0]*(F+1)
queue=deque()
queue.append(S)
visit[S]=0
answer="use the stairs"
while queue:
    floor=queue.popleft()
    if floor==G:
        answer=visit[floor]
        break
    up=floor+U
    down=floor-D
    
    if up!=floor and up<=F and visit[up]==0:
        if up==G:
            answer=visit[floor]+1
            break 
        queue.append(up)
        visit[up]=visit[floor]+1
        
    if down!=floor and down>0 and visit[down]==0:
        if down==G:
            answer=visit[floor]+1        
        queue.append(down)
        visit[down]=visit[floor]+1
        
    
print(answer)
