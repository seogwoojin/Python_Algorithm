N=int(input())
answer=0
minus=[]
plus=[]
ones=[]
zeros=[]

for i in range(N):
    k=int(input())
    
    if k==0:
        zeros.append(0)
    elif k==1:
        answer+=1
    elif k>1:
        plus.append(k)
    else:
        minus.append(k)
        
plus.sort()
minus.sort(reverse=True)

while len(minus)>1:
    a=minus.pop()
    b=minus.pop()
    answer+=a*b

while len(plus)>1:
    a=plus.pop()
    b=plus.pop()
    answer+=a*b
    
if minus and zeros:
    minus.pop()

if minus:
    answer+=minus.pop()

if plus:
    answer+=plus.pop()

print(answer)



    
