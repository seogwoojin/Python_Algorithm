MAX=10**6
N=int(input())
A=list(map(int,input().split()))

increase=[[] for _ in range(MAX+1)]
now_max=0
increase[0].append((-(10**9+1),0))
def find_small(start,end,insert):
    while True:
        if start>end:
            ans=end
            break
        mid=(start+end)//2
        if increase[mid][-1][0]>=insert:
            end=mid-1
        else:
            start=mid+1
    return ans

for i in range(N):
    Almost=find_small(0,now_max,A[i])
    if increase[Almost+1]==[]:
        now_max+=1
    increase[Almost+1].append((A[i],increase[Almost][-1][0]))

print(now_max)
ans=[]
ans.append(increase[now_max][0][0])
before=increase[now_max][0][1]

for n in range(now_max-1, 0,-1):
    ans.append(before)
    for i in increase[n]:
        if i[0]==before:
            before=i[1]
            break
print(' '.join(map(str,reversed(ans))))