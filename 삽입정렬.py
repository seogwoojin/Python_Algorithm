N=int(input())

listA=list(map(int,input().split()))
listB=list(map(int,input().split()))
answer=0
double=False
whatD=0
for i in range(N-1):
    if listB[i]==listB[i+1]:
        double=True
        whatD=listB[i]
        break

if double==False:
    start=listA[0]
    count=listB.index(start)
    small=0
    for j in range(1,N):
        if listA[j]<start:
            small+=1
            if small==count:
                break
    listFirst=listA[:j+1].copy()
    listFirst.sort()
    listA=listFirst+listA[j+1:]
    if listA==listB:
        answer=1
        
if double==True:
    small=0
    for j in range(N):
        if listA[j]<whatD:
            small+=1
            if small==i:
                break
    listFirst=listA[:j+1].copy()
    listFirst.sort()
    if j+2>N-1:
        notSort=[]
    else:
        notSort=listA[j+2:]
    listFirst.insert(i+1,whatD)
    listA=listFirst+notSort
    
    if listA==listB:
        answer=1
    

print(answer)
