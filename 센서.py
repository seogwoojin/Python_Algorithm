MAX_DIST = 1000000 
N=int(input())
K=int(input())
locations = list(set(map(int,input().split())))

locations.sort()

realN=len(locations)

distance = []
for i in range(realN-1):
    distance.append(locations[i+1]-locations[i])

ans = 0
while K<realN:
    # print(distance) 
    small_dist = MAX_DIST
    small_dist_loc = 0
    for i in range(len(distance)):
        if small_dist>distance[i]:
            small_dist = distance[i]
            small_dist_loc = i
    # print(small_dist, small_dist_loc)
    ans+=small_dist
    
    if small_dist_loc == len(distance)-1 :
        distance.pop(small_dist_loc)
    
    else:
        distance[small_dist_loc] = distance[small_dist_loc+1]
        distance.pop(small_dist_loc+1)
        
    realN-=1
print(ans)