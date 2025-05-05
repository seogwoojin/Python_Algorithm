n=int(input())

change=[]
for _ in range(n):
    change.append(list(map(int,input().split()))[1])

bef=change[0]
answer=1
stack=[bef]
if bef==0:
    answer=0
    stack=[]
for floor in change[1:]:
    if floor==0:
        stack=[]
    elif bef>floor:
        while True:
            if not(stack):
                stack.append(floor)
                answer+=1
                break
            elif stack[-1]>floor:
                stack.pop()
            elif stack[-1]<floor:
                stack.append(floor)
                answer+=1
                break
            elif stack[-1]==floor:
                break
    else:
        stack.append(floor)
        answer+=1
    bef=floor
print(answer)
    