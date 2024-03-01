N=int(input())

clss=[[0]*N for _ in range(N)]
ans=0

next=[]
for n in range(N*N):
    lst=list(map(int,input().split()))
    next.append(lst)
    me=lst[0]
    lst2=lst[1:]

    hubo=[[[] for _ in range(5)] for _ in range(5)]
    for i in range(N):
        for j in range(N):
            if clss[i][j]!=0:
                continue
            adj=0
            blank=0
            if i>0:
                if clss[i-1][j] in lst2:    
                    adj+=1
                if clss[i-1][j]==0:
                    blank+=1
            if i<N-1:
                if clss[i+1][j] in lst2:
                    adj+=1
                if clss[i+1][j]==0:
                    blank+=1
            if j>0:
                if clss[i][j-1] in lst2:    
                    adj+=1
                if clss[i][j-1]==0:
                    blank+=1
            if j<N-1:
                if clss[i][j+1] in lst2:
                    adj+=1
                if clss[i][j+1]==0:
                    blank+=1
            
            hubo[adj][blank].append([i,j])
    
    alr=False
    for i in range(4,-1,-1):
        for j in range(4,-1,-1):
            if hubo[i][j]!=[]:
                y,x=hubo[i][j][0]
                clss[y][x]=me
                alr=True
                break
        if alr:
            break

for ne in next:
    lst2=ne[1:]
    alr=False
    for i in range(N):
        for j in range(N):
            if clss[i][j]==ne[0]:
                bef=0
                if i>0:
                    if clss[i-1][j] in lst2:    
                        bef+=1
                if i<N-1:
                    if clss[i+1][j] in lst2:
                        bef+=1
                if j>0:
                    if clss[i][j-1] in lst2:    
                        bef+=1
                if j<N-1:
                    if clss[i][j+1] in lst2:
                        bef+=1
                if bef==1:
                    ans+=1
                elif bef==2:
                    ans+=10
                elif bef==3:
                    ans+=100
                elif bef==4:
                    ans+=1000
                alr=True
                break
        if alr:
            break
print(ans)


        
            
            

