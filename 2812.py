import sys
sys.setrecursionlimit(10**6)
N,K=map(int,input().split())

number=input()

def substr(string, num, high):
    if len(string)==num:
        return ""
    if high==0:
        return "0"*(len(string)-num)
    for n in range(len(string)):
        if string[n]==str(high):
            if n==num:
                return string[n:]
            elif n>num:
                head_st=substr(string[:n], num, high-1)
                return head_st+string[n:]
            elif n<num:
                bot_st=substr(string[n+1:], num-n, high)
                return str(high)+bot_st
    
    return substr(string, num, high-1)




print(substr(number, K, 9))