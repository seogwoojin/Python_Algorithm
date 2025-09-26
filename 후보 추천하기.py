N = int(input())
M = int(input())

lst = list(map(int,input().split()))

student = dict()

for st in lst:
    print(st in student)
    if st in student:
        student[st]+=1
    
    else:
        if len(student) < N:
            student[st] = 1
        else:
            min_key = min(student, key=student.get)
            del student[min_key]
            student[st] = 1
            print(student)

print(student.keys())
ans = list(student.keys())
ans.sort()

for i in range(len(ans)):
    ans[i] = str(ans[i])

print(' '.join(ans))