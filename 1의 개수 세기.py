A,B=map(int,input().split())

def find_1(num):
    while num!=0:
        pass
    
    
lst_A=[]
lst_B=[]
while A!=0:
    lst_A.append(A%2)
    A=A//2
while B!=0:
    lst_B.append(B%2)
    B=B//2
dp=[-1]*len(lst_B)
dp[0]=0
def fill_dp(num):
    if dp[num]==-1:
        if dp[num-1]!=-1:
            pass
        else:
            fill_dp(num-1)
        dp[num]=2*dp[num-1]+2**(num-1)
        
fill_dp(len(lst_B)-1)
    
a1=0
start_a=0
for i in range(len(lst_A)-1, -1,-1):
    if lst_A[i]==1:
        a1+=dp[i]+2**i*start_a
        start_a+=1
b1=0
start_b=0
for i in range(len(lst_B)-1, -1,-1):
    if lst_B[i]==1:
        b1+=dp[i]+2**i*start_b
        start_b+=1
print(b1+start_b-a1)