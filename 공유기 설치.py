import sys
input= sys.stdin.readline
N,C= map(int,input().split())

house=[]

for _ in range(N):
    house.append(int(input()))

house.sort()

house_dist=[house[i+1]-house[i] for i in range(len(house)-1)]


while len(house)!=C:
    loc = house_dist.index(min(house_dist))
    
    if loc == 0:
        house.pop(1)
        next = house_dist.pop(1)
        house_dist[0]+=next
    elif loc == len(house_dist)-1:
        house.pop()
        house_dist.pop()
    else:
        left = house_dist[loc-1]
        right = house_dist[loc+1]
        
        if left >= right:
            house_dist[loc]+=right
            house_dist.pop(loc+1)
            house.pop(loc+1)
        else:
            house_dist[loc-1]+=house_dist[loc]
            house_dist.pop(loc)
            house.pop(loc)
    
print(min(house_dist))