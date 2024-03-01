from collections import deque
N,K=map(int,input().split())

lst=list(map(int,input().split()))
conven=[]
conven.append(lst[:N])
conven.append(lst[N:])
ans=1

start=0
end=N-1
queue=deque()
k_start=0
while True:
    if start==0:
        start=2*N-1
    else:
        start-=1
    
    if end==0:
        end=2*N-1
    else:
        end-=1
    
    if queue and queue[0]==end:
        queue.popleft()
    
    for num in range(len(queue)):
        if queue[num]+1==2*N:
            queue_next=0
        else:
            queue_next=queue[num]+1
        
        if num==0 and lst[queue_next]!=0:
            queue[num]=queue_next
        elif num>=1 and lst[queue_next]!=0 and queue[num-1]!=queue[num]+1:
            queue[num]=queue_next
        if queue[num]==queue_next:
            lst[queue[num]]-=1
            if lst[queue[num]]==0:
                k_start+=1
                    
        
    if queue and queue[0]==end:
        queue.popleft()
        
    if lst[start]!=0:
        queue.append(start)
        lst[start]-=1
        if lst[start]==0:
            k_start+=1
    
    if K<=k_start:
        break
    ans+=1
print(ans)
    
    
    
    