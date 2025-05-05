N,S=map(int,input().split())

number=list(map(int,input().split()))

sum_number=[]
answer=100000
small=0
big=0
sum_now=number[0]
while True:
    if sum_now>=S:
        while big>small:
            if sum_now-number[small]>=S:
                sum_now-=number[small]
                small+=1
            else:
                break
        if big-small+1<answer: answer=big-small+1
        if sum_now>=S and big<N-1:
            big+=1
            sum_now+=number[big]


    else:
        while big<N-1:
            big+=1
            sum_now+=number[big]
            if sum_now>=S:
                if big-small+1<answer: answer=big-small+1
                break
    
    if big==N-1:
        if sum_now>=S:
            while big>small:
                if sum_now-number[small]>=S:
                    sum_now-=number[small]
                    small+=1
                else:
                    break        
            if big-small+1<answer: answer=big-small+1
        break

if answer==100000:
    answer=0

print(answer)