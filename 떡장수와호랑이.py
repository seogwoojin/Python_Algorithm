N=int(input())

sell_list = []
for i in range(N):
    sell_list.append(list(map(int,input().split()))[1:])

answer = -1
from_before = []

first = sell_list[0]
f_dict = {}
for rice in first:
    f_dict[rice] = 0
from_before.append(f_dict)

for i in range(1, len(sell_list)):
    sell = sell_list[i]
    before = from_before[i-1]
    f_dict = {}

    for rice in sell:
        for before_key in before:
            if before_key != rice:
                f_dict[rice] = before_key
                break
    
    if not(f_dict):
        print(-1)
        exit()
    
    from_before.append(f_dict)

answer_list = []
alive_list = from_before[-1]

before_number = 0
for key in alive_list:
    answer_list.append(str(key))
    before_number = alive_list[key]
    break
    
for i in range(len(from_before)-2, -1, -1):
    alive_list = from_before[i]
    answer_list.append(str(before_number))
    before_number = alive_list[before_number]
print("\n".join(reversed(answer_list)))

