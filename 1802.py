T=int(input())

for _ in range(T):
    answer="YES"
    string=input()
    N=len(string)
    if N==1:
        print("YES")
        continue
    
    start=N//2
    s1=string[start]
    move=(start+1)//2
    
    check=[[[start-move],[start+move]]]
    chs=0
    while True:
        if move==1:
            break        
        move//=2
        lst=[[],[]]
        bef=check[chs]
        for be in bef:
            for k in be:
                lst[0].append(k-move)
                lst[1].append(k+move)
        chs+=1
        check.append(lst)
        
    
    for c in check:
        if string[c[0][0]]==string[c[1][0]]:
            answer="NO"
            break
        
        c0=string[c[0][0]]
        for n in range(1,len(c[0])):
            if c0!=string[c[0][n]]:
                answer="NO"
                break
        
        c1=string[c[1][0]]
        for n in range(1,len(c[1])):
            if c1!=string[c[1][n]]:
                answer="NO"
                break        
    
    print(answer)
    
    