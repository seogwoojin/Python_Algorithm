import sys
import heapq
input=sys.stdin.readline
N=int(input())

class_time=[]
room=[0]
for i in range(N):
    class_time.append(list(map(int,input().split())))
    
class_time.sort(key=lambda x:x[0])
for start,end in class_time:
    if room[0]>start:
        heapq.heappush(room, end)
        
    else:
        heapq.heappop(room)
        heapq.heappush(room,end)
    
    
print(len(room))

