from collections import deque

sdoku=[]
for _ in range(9):
    sdoku.append(list(map(int,input().split())))
    
queue=deque()

for i in range(9):
    for j in range(9):
        if sdoku[i][j]==0:
            queue.append([i,j])
finish=False 
def dfs():
    lst=queue.popleft()
    i=lst[0]
    j=lst[1]
    
    search=[1,2,3,4,5,6,7,8,9]
    sec_i=i//3
    sec_j=j//3
    
    already=[]
    for k in range(9):
        if sdoku[i][k] not in already:
            already.append(sdoku[i][k])
    
    for k in range(9):
        if sdoku[k][j] not in already:
            already.append(sdoku[k][j])
            
    for a1 in range(3):
        for a2 in range(3):
            if sdoku[3*sec_i+a1][3*sec_j+a2] not in already:
                already.append(sdoku[3*sec_i+a1][3*sec_j+a2])
    sub=[x for x in search if x not in already]
    
    if not(queue):
        sdoku[i][j]=sub[0]
        for i in range(9):
            for j in range(9):
                print(sdoku[i][j],end=" ")
            print()
        exit()
    for s in sub:
        sdoku[i][j]=s
        dfs()
        sdoku[i][j]=0
    queue.appendleft(lst)
    return

dfs()
    