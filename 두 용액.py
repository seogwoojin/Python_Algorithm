N=int(input())
bottle=list(map(int,input().split()))

bottle.sort(key=lambda x:abs(x))

ans=[]
for i in range(N):
    if bottle[i]>0:
        num1=bottle[i]
        for j in range(i+1,N):
            if bottle[j]>0:
                ans.append([num1+bottle[j], [num1, bottle[j]]])
                break
        break

for i in range(N):
    if bottle[i]<0:
        num1=bottle[i]
        for j in range(i+1,N):
            if bottle[j]<0:
                ans.append([abs(num1+bottle[j]), [bottle[j],num1]])
                break
        break

small=[float('inf'), [0,0]]

for i in range(N):
    if bottle[i]>0:
        right=[float('inf'), [0,0]]
        left=[float('inf'), [0,0]]
        if i!=N-1 and bottle[i+1]<0:
            right=[abs(bottle[i]+bottle[i+1]),[bottle[i+1],bottle[i]]]
        
        if i!=0 and bottle[i-1]<0:
            left=[abs(bottle[i]+bottle[i-1]),[bottle[i-1],bottle[i]]]
        
        small=min(right,left,small, key=lambda x:x[0])

ans.append(small)
answer=min(ans, key=lambda x:x[0])[1]
print(answer[0], answer[1])
