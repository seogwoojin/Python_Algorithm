N,S=map(int,input().split())
lst=list(map(int,input().split()))

s_max=10**6

hap=[0]*(2*s_max+1)

hap[s_max]=1
hap[lst[0]+s_max]=1
for n in range(1,N):
    uplist=[]
    for i in range(2*s_max+1):
        if hap[i]!=0:
            uplist.append(i+lst[n])
    
    for u in uplist:
        hap[u]+=1

print(hap[S+s_max])