n=int(input())
not_sorted=list(map(int,input().split()))
yes_sorted=list(map(int,input().split()))

double=False

for i in range(n):
    if yes_sorted[i] in yes_sorted[i+1:]:
        double=True
        break

def check_notd(start, end):
    if start<end:
        mid=start+end//2
        check_notd(start, mid)
        check_notd(mid+1, end)
        sorting(start,end,mid)
        
def sorting(start,end,mid):
    

if double==False:
    q=n//2
    