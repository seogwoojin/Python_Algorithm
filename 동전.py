T=int(input())

for i in range(T):
    N=int(input())
    coins = list(map(int,input().split()))
    M=int(input())
    
    total = [0]*(M+1)
    for coin in coins:
        if coin > M:
            break
        total[coin] += 1
        for i in range(coin+1, M+1):
            bef = total[i-coin]
            total[i] += bef
    print(total[M])