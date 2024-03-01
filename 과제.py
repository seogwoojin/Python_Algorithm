N=int(input())

stack=[]
for i in range(N):
    stack.append(list(map(int,input().split())))
    
stack.sort(key=lambda x:x[1])
lst=[0]*1001
while stack:
    task=stack.pop()
    day=task[0]
    score=task[1]
    
    while lst[day]!=0:
        day-=1
        if day==0:
            break
    if day!=0:
        lst[day]=score
    

print(sum(lst))
        
    
    