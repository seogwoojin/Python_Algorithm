import sys
input=sys.stdin.readline

G=int(input())

P=int(input())

plain=[]
for i in range(P):
    plain.append(int(input()))

plain_set=[0]*(P+1)
plain_set[0]=-1
answer=0
for i in range(P):
    can_go=plain[i]
    while True:
        if plain_set[can_go]==0:
            plain_set[can_go]=-1
            answer+=1
        
        else:
            can_go-=1