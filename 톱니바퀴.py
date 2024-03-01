lst=[0]
for i in range(4):
    lst.append(input())
K=int(input())
def turn(num, how,already):
    already.append(num)
    if how==1:
        bef=lst[num]
        now=bef[-1]+bef[:-1]
        lst[num]=now
        nr=bef[6]
        nl=bef[2]
    else:
        bef=lst[num]
        now=bef[1:]+bef[0]
        lst[num]=now
        nr=bef[6]
        nl=bef[2]
        
    if num>1:
        if nr==lst[num-1][2]:        
            pass
        else:
            if num-1 not in already:
                turn(num-1, -how,already)
    
    if num<4:
        if nl==lst[num+1][6]:
            pass
        else:
            if num+1 not in already:
                turn(num+1, -how, already)
            
for i in range(K):
    num,loc=map(int,input().split())
    already=[num]
    turn(num,loc,already)
answer=0
for i in range(4):
    hap=2**i
    if lst[i+1][0]=='1':
        answer+=hap
print(answer)


        