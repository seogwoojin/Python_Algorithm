from collections import deque
N= int(input())
M = int(input())

graph_list = [[] for _ in range(N+1)]
for i in range(N):
    i_list = list(map(int,input().split()))
    for j in range(N):
        if i_list[j] == 1:
            graph_list[i+1].append(j+1)

plan = list(map(int,input().split()))
sub_graph = []

check = [False]*(N+1)
queue = deque()
queue.append(plan[0])
check[plan[0]] = True

while queue:
    q = queue.popleft()
    sub_graph.append(q)

    for num in graph_list[q]:
        if check[num]:
            continue
        queue.append(num)
        check[num] = True

answer = "YES"

for city in plan:
    if city not in sub_graph:
        answer = "NO"
        break

print(answer)