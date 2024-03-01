N,L=map(int,input().split())

dirt=[]
for i in range(N):
    dirt.append(list(map(int,input().split())))
    
dirt.sort(key=lambda x:x[0])

new_dirt=[]
stack=[]
left=-1
answer=0
for n in range(N):
    now=dirt[n]
    num=now[1]-now[0]
    need=L-num%L #2
    if need==L:
        need=0
    if need==0 and left<now[0]:
        answer+=num//L
        left=now[1]
        continue
    else:
        if left+1==now[0]:
            left=now[1]+need
            answer+=num//L+1
            
        elif left>=now[0]:
            num=now[1]-left
            need=L-num%L
            if need==L:
                need=0
            left=now[1]+need
            if num%L==0:
                answer+=num//L
            else:
                answer+=num//L+1
        
        else:
            can_use=now[0]-left
            if n!=N-1:
                if dirt[n+1][0]<=now[1]+need:
                    left=now[1]+need
                    answer+=num//L+1
                    continue
                
            if need<=can_use:
                left=now[1]
            else:
                need-=can_use
                left=now[1]+need
            
            
            answer+=num//L+1
            
        

print(answer)