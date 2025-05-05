import sys
input=sys.stdin.readline

def findNotChecked(target):
    while True:
        if target<1:
            return False
        if plain_set[target]==-1:
            return target
        else:
            target=plain_set[target]

G=int(input())

P=int(input())

plain=[]
for i in range(P):
    plain.append(int(input()))

plain_set=[-1]*(G+1)
answer=0
for i in range(P):
    can_go=plain[i]
    if plain_set[can_go]==-1:
        answer+=1
        notChecked=findNotChecked(can_go-1)
        if notChecked==False:
            plain_set[can_go]=0
        else:
            plain_set[can_go]=notChecked
    else:
        notChecked=findNotChecked(can_go)
        if notChecked==False:
            print(answer)
            exit(0)
        answer+=1
        nextChecked=findNotChecked(notChecked-1)
        if nextChecked==False:
            plain_set[can_go]=0
            plain_set[notChecked]=0
        else:
            plain_set[notChecked]=nextChecked
            plain_set[can_go]=nextChecked
print(answer)