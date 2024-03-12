s=input()
t=input()

while True:
    if len(s)==len(t):
        if s==t:
            print(1)
        else:
            print(0)
        break
    
    if t[-1]=='A':
        t=t[:-1]
    else:
        t=''.join(reversed(t[:-1]))

