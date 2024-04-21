import sys
sys.setrecursionlimit(10**6)
N,K=map(int,input().split())

A=list(map(int,input().split()))

num=0
def quick_sort(p,r):
    if p<r:
        q=partition(p,r)
        quick_sort(p,q-1)
        quick_sort(q+1,r)

def partition(p,r):
    global num
    global A
    global K
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            
            num+=1
            
            i+=1
            temp=A[j]
            A[j]=A[i]
            A[i]=temp
            if num==K:
                print(A[i],A[j])
                exit()
    if i+1!=r:
        num+=1
        temp=A[r]
        A[r]=A[i+1]
        A[i+1]=temp
        if num==K:
            print(A[i+1], A[r])
            exit()
    return i+1

quick_sort(0,N-1)
print(-1)