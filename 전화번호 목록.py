import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    n=int(input())
    num_hash={}
    breaked=False
    for i in range(n):

        number=input().strip()
        start=0
        in_hash=num_hash
        
        while True:
            num_char=number[start]

            if start==len(number)-1:
                if num_char in in_hash:
                    in_hash[num_char]=False
                    breaked=True
                    break

                else:
                    in_hash[num_char]=False
                    break
            

            if num_char in in_hash:
                if in_hash[num_char]==False:
                    breaked=True
                    break
            
            else:
                in_hash[num_char]={}
            
            in_hash=in_hash[num_char]
            start+=1
    if breaked==True:
        print("NO")
    else:
        print("YES")