n=int(input())

now = input()
want = input()

is_change = []

for i in range(n):
    if now[i] != want[i]:
        is_change.append(True)
    else:
        is_change.append(False)


will_change = [False]*n

answer1 = 0
for i in range(1,n):
    if i == n-1:
        if will_change[i-1] != is_change[i-1]:
            will_change[i] = not will_change[i]
            answer1+=1
        if will_change[i] != is_change[i]:
            answer1 = -1
        break
            

    if will_change[i-1] != is_change[i-1]:
        will_change[i] = not will_change[i]
        will_change[i+1] = not will_change[i+1]
        answer1 += 1


will_change = [False]*n

answer2 = 1
will_change[0] = True
will_change[1] = True
for i in range(1,n):
    if i == n-1:
        if will_change[i-1] != is_change[i-1]:
            will_change[i] = not will_change[i]
            answer2 += 1

        if will_change[i] != is_change[i]:
            answer2 = -1
        break
            

    if will_change[i-1] != is_change[i-1]:
        will_change[i] = not will_change[i]
        will_change[i+1] = not will_change[i+1]
        answer2 += 1
if answer1 == -1 and answer2 == -1:
    print(-1)
else:
    if answer1 >= 0 and answer2 >= 0:
        print(min(answer1, answer2))
    elif answer1>=0:
        print(answer1)
    else:
        print(answer2)