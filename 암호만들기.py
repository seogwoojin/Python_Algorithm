L,C = map(int,input().split())
strings = list(map(str, input().split()))
strings.sort()

gathers = ['a','e','i','o','u']

def select(word_list, word_point):
    word_list.append(strings[word_point])
    if len(word_list) < L:
        for next_point in range(word_point+1, C):
            select(word_list, next_point)
        word_list.pop()
        return
    if len(word_list) == L:
        gathers_num = 0
        for char in gathers:
            if char in word_list:
                gathers_num+=1
        
        if gathers_num >=1 and L-gathers_num>=2:
            print(''.join(word_list))
            
        word_list.pop()
    
    
for start in range(0, C-L+1):
    select([], start)