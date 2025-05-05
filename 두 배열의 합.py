T=int(input())


n=int(input())
A_list=list(map(int,input().split()))
m=int(input())
B_list=list(map(int,input().split()))

A_hash={}
A_sum=[[0]*n for _ in range(n)]
for i in range(n):
    A_sum[i][i]=A_list[i]
    if A_list[i] in A_hash:
        A_hash[A_list[i]]+=1
    else:
        A_hash[A_list[i]]=1

for i in range(n-1):
    for j in range(i+1,n):
        if i==0:
            A_sum[i][j]=A_sum[i][j-1]+A_sum[j][j]
        else:
            A_sum[i][j]=A_sum[i-1][j]-A_sum[i-1][i-1]
        
        if A_sum[i][j] in A_hash:
            A_hash[A_sum[i][j]]+=1
        else:
            A_hash[A_sum[i][j]]=1
B_hash={}
B_sum=[[0]*m for _ in range(m)]
for i in range(m):
    B_sum[i][i]=B_list[i]
    if B_list[i] in B_hash:
        B_hash[B_list[i]]+=1
    else:
        B_hash[B_list[i]]=1

for i in range(m-1):
    for j in range(i+1,m):
        if i==0:
            B_sum[i][j]=B_sum[i][j-1]+B_sum[j][j]
        else:
            B_sum[i][j]=B_sum[i-1][j]-B_sum[i-1][i-1]
        
        if B_sum[i][j] in B_hash:
            B_hash[B_sum[i][j]]+=1
        else:
            B_hash[B_sum[i][j]]=1
                        
answer=0

for A_key in A_hash:
    num1=A_hash[A_key]
    if T-A_key in B_hash:
        answer+=num1*B_hash[T-A_key]
print(answer)
