K=int(input())

start=1
while K>start:
    start=start*2
start1=start
ans=0
choco=0
while True:
    if start==K:
        break
    now=start//2
    if now==0:
        break
    ans+=1
    if choco+now==K:
        break
    elif choco+now<K:
        choco+=now
    
    start=start//2
    
    
print(start1,ans)
    
        
    