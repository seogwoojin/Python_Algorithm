import sys
input=sys.stdin.readline
T=int(input())

for i in range(T):
    answer=0
    n=int(input())
    lst=[]
    for i in range(n):
        lst.append(list(map(int,input().split())))
        
    lst.sort(key=lambda x:x[0])
    smallest=n
    for i in range(n):
        if smallest<lst[i][1]:
            continue
        else:
            smallest=lst[i][1]
            answer+=1
    print(answer)
    