N=int(input())

maps=[]
for i in range(N):
    maps.append(list(map(int,input().split())))
answer=0
def next_turn(state, direction, depth):
    global answer
    if direction==0: #up
        after_state=[[0]*N for _ in range(N)]
        for col in range(N):
            temp=[]
            for row in range(N):
                if state[row][col]!=0:
                    temp.append(state[row][col])
            temp_sum=[]
            start=0
            compare=1
            while compare<len(temp):
                if temp[start]==temp[compare]:
                    temp_sum.append(temp[start]*2)
                    start=compare+1
                    compare=start+1
                else:
                    temp_sum.append(temp[start])
                    start=compare
                    compare=start+1

            if start==len(temp)-1:
                temp_sum.append(temp[start])    
            
            
            for i in range(len(temp_sum)):
                after_state[i][col]=temp_sum[i]
            
    elif direction==1: #down
        after_state=[[0]*N for _ in range(N)]
        for col in range(N):
            temp=[]
            for row in range(N):
                if state[row][col]!=0:
                    temp.append(state[row][col])
            temp_sum=[]
            start=len(temp)-1
            compare=start-1
            while compare>-1:
                if temp[start]==temp[compare]:
                    temp_sum.append(temp[start]*2)
                    start=compare-1
                    compare=start-1
                else:
                    temp_sum.append(temp[start])
                    start=compare
                    compare=start-1

            if start==0:
                temp_sum.append(temp[start])    
            
            
            for i in range(len(temp_sum)):
                after_state[N-i-1][col]=temp_sum[i]
    elif direction==2: #right
        after_state=[[0]*N for _ in range(N)]
        for row in range(N):
            temp=[]
            for col in range(N):
                if state[row][col]!=0:
                    temp.append(state[row][col])
            temp_sum=[]
            start=0
            compare=1
            while compare<len(temp):
                if temp[start]==temp[compare]:
                    temp_sum.append(temp[start]*2)
                    start=compare+1
                    compare=start+1
                else:
                    temp_sum.append(temp[start])
                    start=compare
                    compare=start+1

            if start==len(temp)-1:
                temp_sum.append(temp[start])    
            
            
            for i in range(len(temp_sum)):
                after_state[row][i]=temp_sum[i]
    
    elif direction==3: #left
        after_state=[[0]*N for _ in range(N)]
        for row in range(N):
            temp=[]
            for col in range(N):
                if state[row][col]!=0:
                    temp.append(state[row][col])
            temp_sum=[]
            start=len(temp)-1
            compare=start-1
            while compare>-1:
                if temp[start]==temp[compare]:
                    temp_sum.append(temp[start]*2)
                    start=compare-1
                    compare=start-1
                else:
                    temp_sum.append(temp[start])
                    start=compare
                    compare=start-1

            if start==0:
                temp_sum.append(temp[start])    
            
            
            for i in range(len(temp_sum)):
                after_state[row][N-i-1]=temp_sum[i]
    
    if depth==5:
        value=max(map(max,after_state))
        if value>answer:
            answer=value
        return 
    
    else:
        for next in range(4):
            next_turn(after_state, next, depth+1)

for next in range(4):
    next_turn(maps, next, 1)

print(answer)