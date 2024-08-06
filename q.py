N,S=map(int,input().split())

ints=list(map(int,input().split()))

intsum=0
answer=0

def find_s(num):
    global intsum, answer

    if intsum==S:
        answer+=1
    
    if num<N-1:
        for i in range(num+1, N):
            intsum+=ints[i]
            find_s(i)
            intsum-=ints[i]
            
    
    
for i in range(N):
    intsum+=ints[i]
    find_s(i)
    intsum-=ints[i]
print(answer)