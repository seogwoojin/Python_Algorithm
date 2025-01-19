n=int(input())
lst = [0]*31

lst[2] = 3

if n % 2== 1:
    print(0)
else:
    for i in range(4,32,2):
        bef = lst[i-2]
        lst[i] = 3*bef + (bef-1)
    print(lst[n])
    