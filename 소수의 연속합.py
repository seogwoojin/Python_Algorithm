MAX=4000000
prime=[True]*(MAX+1)
prime[0]=False
prime[1]=False
for i in range(2, int(MAX**(1/2))+1):
    if prime[i]==True:
        num=2
        while i*num<=MAX:
            if prime[i*num]==True:
                prime[i*num]=False
            num+=1

final=[]
for i in range(MAX+1):
    if prime[i]==True:
        final.append(i)
N=int(input())


small=0
big=0
now_sum=2
answer=0
while True:
    if now_sum==N:
        answer+=1
        if big==len(final)-1:
            break
        big+=1
        now_sum+=final[big]
    
    elif now_sum<N:
        if big==len(final)-1:
            break
        big+=1
        now_sum+=final[big]
    
    elif now_sum>N:
        if small==big:
            break
        now_sum-=final[small]
        small+=1
    
print(answer)
    
