import sys
import heapq
input=sys.stdin.readline
N,K=map(int,input().split())

dia=[]
for i in range(N):
    dia.append(list(map(int,input().split())))

dia.sort(key=lambda x:x[1])

small_hq=[]
big_hq=[]

for i in range(K):
    c=int(input())
    heapq.heappush(small_hq, (-c,c))

max=0
for i in range(N):
    if dia[i][0]>small_hq[0][0]:
        continue
    while dia[i][0]<small_hq[0][0]:
        num=heapq.heappop(small_hq)
        heapq.heappush(big_hq, (num[1],num[1]))
    
    greedy=heapq.heappop(big_hq)
    max+=dia[i][1]
    
    #실패
    

