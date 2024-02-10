N,L=map(int,input().split())

maps=[]
for i in range(N):
    maps.append(list(map(int,input().split())))
answer=0
for i in range(N):
    floors=maps[i]
    error=False
    before=floors[0]
    stack=[before]
    for n in range(1,N):
        floor=floors[n]
        if not(stack):
            stack.append(floor)
            continue
        before=stack[-1]
        if abs(before-floor)>=2:
            error=True
            break
        elif before==floor:
            stack.append(floor)
        else: #변화 발생
            if before>floor:
                j=0
                for j in range(1,L):
                    if n+j>=N:
                        error=True
                        break
                    elif floors[n+j]==before-1:
                        continue
                    else:
                        error=True
                        break
                if j!=L-1:
                    error=True
                    break
                else:
                    n=n+j+1
                    if n<N-1 and floors[n]<floors[n+1]:
                        error=True
                        break
                    elif n<N-1 and floors[n]>floors[n+1]:
                        stack=[floors[n]]
                    else:
                        stack=[]
            else:
                if len(stack)<L:
                    error=True
                    break
                else:
                    stack=[]
                    stack.append(floor)
        if error:
            break
        
    if not(error):
        answer+=1
            
for i in range(N):
    floors=[]
    for k in range(N):
        floors.append(maps[k][i])
    error=False
    before=floors[0]
    stack=[before]
    for n in range(1,N):
        floor=floors[n]
        if not(stack):
            stack.append(floor)
            continue
        before=stack[-1]
        if abs(before-floor)>=2:
            error=True
            break
        elif before==floor:
            stack.append(floor)
        else: #변화 발생
            if before>floor:
                j=0
                for j in range(1,L):
                    if n+j>=N:
                        error=True
                        break
                    elif floors[n+j]==before-1:
                        continue
                    else:
                        error=True
                        break
                if j!=L-1:
                    error=True
                    break
                else:
                    n=n+j+1
                    if n<N-1 and floors[n]<floors[n+1]:
                        error=True
                        break
                    elif n<N-1 and floors[n]>floors[n+1]:
                        stack=[floors[n]]
                    else:
                        stack=[]
            else:
                if len(stack)<L:
                    error=True
                    break
                else:
                    stack=[]
                    stack.append(floor)
        if error:
            break
        
    if not(error):
        answer+=1
            
print(answer)