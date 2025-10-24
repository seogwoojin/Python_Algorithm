import sys
import heapq
input = sys.stdin.readline

N,M = map(int,input().split())

roads = [[] for _ in range(N+1)]

for _ in range(M):
    u,v,w = map(int,input().split())
    roads[u].append((v,w))
    roads[v].append((u,w))

def dajikstra(start, roads):

    check = [False] * len(roads)
    minimum = [float('inf')] * len(roads)
    minimum[start] = 0

    next_queue = [(0, start)]
    while next_queue:
        dist, point = heapq.heappop(next_queue)
        if check[point] == True:
            continue

        check[point] = True
        next = roads[point]

        for next_info in next:
            new_road_dist = dist + next_info[1]

            if new_road_dist < minimum[next_info[0]]:
                minimum[next_info[0]] = new_road_dist
                heapq.heappush(next_queue, (new_road_dist, next_info[0]))
    return minimum

X, Z = map(int,input().split())
P = int(input())
p_list = list(map(int,input().split()))


print(dajikstra(X, roads))
middle_info = dajikstra(X, roads)
reverse_info = dajikstra(Z, roads)

answer = float('inf')

for p in p_list:
    to_p = middle_info[p]
    from_p = reverse_info[p]
    
    if to_p + from_p < answer:
        answer = to_p + from_p

if answer == float('inf'):
    print(-1)
else:
    print(answer)