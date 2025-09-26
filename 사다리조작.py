import sys
from copy import deepcopy


def i_is_i(ladder):
    for i in range(N):  # i가 i로 가는지 확인한다
        col = i
        for row in range(H):  # 마지막 가로줄(H) 가기 전까지 확인
            if ladder[row][col]:  # col번 세로선과 col+1번 세로선이 row번 가로선에 의해 연결되는가?
                col += 1  # 다음 세로줄로 이동
            elif 0 < col and ladder[row][col-1]:  # col-1 세로선과 col 세로선이 row 가로선에 의해 연결되는가?
                col -= 1
        if col != i:
            return False
    return True


def dfs(count, max_count, ladder, y, x):
    if count == max_count:
        if i_is_i(ladder):
            print(max_count)
            exit(0)
        return
    
    for i in range(x, N-1):
        if ladder[y][i] != 1:
            if 0 < i and ladder[y][i-1] == 1:
                continue
            if i < N-1 and ladder[y][i+1] == 1:
                continue

            ladder[y][i] = 1
            dfs(count+1, max_count, ladder, y, i)
            ladder[y][i] = 0


    for i in range(y+1, H):  # 가로
        for j in range(N-1):  # 세로
            if ladder[i][j] != 1:
                if 0 < j and ladder[i][j-1] == 1:
                    continue
                if j < N-1 and ladder[i][j+1] == 1:
                    continue

                ladder[i][j] = 1
                dfs(count+1, max_count, ladder, i, j)
                ladder[i][j] = 0


if __name__ == '__main__':
    input = sys.stdin.readline
    N, M, H = map(int, input().split())  # 세로선, 가로선, 가로선후보갯수
    ladder_origin = [[0] * N for _ in range(H)]

    for _ in range(M):
        i, j = map(int, input().split())  # j번 세로줄과 j+1번 세로선을 i번째 가로선이 연결하고 있음
        ladder_origin[i-1][j-1] = 1  #

    for h_num in range(4):  # 가로줄을 0~3개 놓아봄
        dfs(0, h_num, deepcopy(ladder_origin), 0, 0)

    print(-1)