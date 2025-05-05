import sys
sys.setrecursionlimit(10**6)

n=int(input())
in_order=list(map(int,input().split()))
post_order=list(map(int,input().split()))
num=n-1

dic={}
for i in range(len(in_order)):
    dic[in_order[i]]=i

def findtree(start, end):
    global num
    if start==end:
        print(post_order[num], end=" ")
        return
    middle=dic[post_order[num]]
    left_size=middle-start
    right_size=end-middle
    print(post_order[num], end=" ")
    num-=1
    if left_size>0:
        bfnum=num
        num-=right_size
        findtree(start, middle-1)
        num=bfnum
    
    if right_size>0:
        findtree(middle+1,end)
    return
findtree(0,n-1)