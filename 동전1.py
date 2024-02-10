n,k=map(int,input().split())

money=[]
for i in range(n):
    money.append(int(input()))
    
money.sort()

lst=[0]*(k+1)
for m in money:
    if m>k:
        break
    lst2=[0]*(k+1)
    lst2[m]+=1
    for i in range(m+1,k+1):
        if i%m==0:
            lst2[i]+=1
        t=m
        tm=i-m
        lst2[i]+=(lst2[tm]*lst[t])
        
    for i in range(k+1):
        lst[i]+=lst2[i]
    print(lst)
print(lst[k])