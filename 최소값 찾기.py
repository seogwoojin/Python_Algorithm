from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))

dq = deque()
for i in range(N):
    # 현재 창문을 벗어난 인덱스 제거
    while dq and dq[0] < i - L + 1:
        dq.popleft()
    # 현재 요소보다 큰 요소에 해당하는 인덱스 제거
    while dq and A[dq[-1]] > A[i]:
        dq.pop()
    dq.append(i)
    # 덱의 맨 앞은 현재 창문 내의 최솟값을 나타냅니다
    print(A[dq[0]], end=" ")
