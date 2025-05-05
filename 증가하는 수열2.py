MAX=10**6
N=int(input())
A=list(map(int,input().split()))

increase=[False]*(MAX+1)
now_max=0
increase[0]=-(10**9+1)
def find_small(start,end,insert):
    while True:
        if start>end:
            ans=end
            break
        mid=(start+end)//2
        if increase[mid]>=insert:
            end=mid-1
        else:
            start=mid+1
    return ans

for i in range(N):
    Almost=find_small(0,now_max,A[i])
    if increase[Almost+1]==0:
        now_max+=1
    increase[Almost+1]=A[i]
print(now_max)
        