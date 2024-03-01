N,M,y,x,K=map(int,input().split())

maps=[]

for i in range(N):
    maps.append(list(map(int,input().split())))
    
todo=list(map(int,input().split()))

dice=dict()

for i in range(1,7):
    dice[i]=0

top_num=1
top_left=3
top_up=2

matching=[0,6,5,4,3,2,1]
for direction in todo:
    x_bef=x
    y_bef=y
    if direction==1:
        if x==M-1:
            continue
        x+=1
        temp=top_num
        top_num=matching[top_left]
        top_left=temp

    elif direction==2:
        if x==0:
            continue
        x-=1
        temp=top_num
        top_num=top_left
        top_left=matching[temp]
        
    elif direction==3:
        if y==0:
            continue
        y-=1
        
        temp=top_num
        top_num=matching[top_up]
        top_up=temp
        
    else:
        if y==N-1:
            continue
        y+=1
        temp=top_num
        top_num=top_up
        top_up=matching[temp]
    
    if x_bef==x and y_bef==y:
        continue
    else:
        bottom=matching[top_num]
        if maps[y][x]==0:
            maps[y][x]=dice[bottom]
        else:
            dice[bottom]=maps[y][x]
            maps[y][x]=0
            
        print(dice[top_num])