def findLeastBig(target):
    start=0
    end=M-1
    while True:
        middle=(start+end)//2
        if start==end:
            return start
        elif M_list[middle]<=target:
            start=middle+1
        else:
            end=middle

def findUnionConnection(target):
    while True:
        if M_union[target]==-1:
            return target
        else:
            target=M_union[target]

N,M,K=map(int,input().split())

M_list=list(map(int,input().split()))
M_list.sort()
M_union=[-1]*M
K_list=list(map(int,input().split()))


for i in K_list:
    bigLocation=findLeastBig(i)
    if M_union[bigLocation]==-1:
        print(M_list[bigLocation])
        if bigLocation<M-1:
            notChecked=findUnionConnection(bigLocation+1)
            M_union[bigLocation]=notChecked

    else:    
        realBigLocation=bigLocation
        while True:
            if M_union[realBigLocation]==-1 or realBigLocation==M-1:
                break
            else:
                realBigLocation=M_union[realBigLocation]
        print(M_list[realBigLocation])
        if realBigLocation<M-1:
            notChecked=findUnionConnection(realBigLocation+1)
            M_union[realBigLocation]=notChecked
            M_union[bigLocation]=notChecked
    print(M_union)
