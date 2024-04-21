num=10**7
N=int(input())
card=list(map(int,input().split()))

M=int(input())
much=list(map(int,input().split()))

dic={}

for i in card:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

for i in much:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")
    # start=-num
    # middle=0
    # end=num
    # while True:
    #     if i==middle:
    #         print(dic)
    #         break
    #     if i>middle:
    #         start=middle+1
    #         middle=(start+end)//2
    #     if i<middle:
    #         end=middle-1
    #         middle=(start+end)//2
        
            