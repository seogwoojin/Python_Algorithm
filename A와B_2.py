S=input()
T=input()
len_s = len(S)

from collections import deque
queue = deque()
queue.append(T)
answer = 0

while queue:
    string : str = queue.popleft()
    if len(string) < len_s:
        break
    if string == S:
        answer = 1
        break
    if string.startswith("B"):
        queue.append(''.join(reversed(string[1:])))
    if string.endswith("A"):
        queue.append(string[:-1])
    
print(answer)


