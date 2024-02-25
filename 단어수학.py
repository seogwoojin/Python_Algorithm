N=int(input())

words=[[] for _ in range(8)]
for _ in range(N):
    string=input()
    k=len(string)-1
    for n in range(len(string)):
        words[n].append(string[k])
        k-=1
    
word_order=[[0,i] for i in range(ord('Z')-ord('A')+1)]

order=[]
for i in range(7,-1,-1):
    if words[i]:
        for word in words[i]:
            word_order[ord(word)-ord('A')][0]+=10**i
            
mam=9
answer=0
word_order.sort(key=lambda x:x[0],reverse=True)


for wordk in word_order:
    if wordk[0]==0:
        break
    else:
        answer+=mam*wordk[0]
        mam-=1
print(answer)


