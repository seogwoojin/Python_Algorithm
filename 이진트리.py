k=int(input())
weights=[0,0]+list(map(int,input().split()))
sum_weight=[0]*(2**(k+1))

def dp(parent):
    if parent*2>=2**(k+1):
        return weights[parent]
    
    left=dp(parent*2)
    right=dp(parent*2+1)
    
    if left>right:
        weights[parent*2+1]+=(left-right)
        sum_weight[parent]=left+weights[parent]
    
    else:
        weights[parent*2]+=(right-left)
        sum_weight[parent]=right+weights[parent]
    
    return sum_weight[parent]

dp(1)
print(sum(weights))

