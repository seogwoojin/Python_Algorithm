N=int(input())

player=[]
for i in range(N):
    player.append(list(map(int,input().split())))
all_player=[i for i in range(N)]
check=N//2
team_list=[]    
answer=10**6
def dfs(num):
    global answer
    team_list.append(num)
    if len(team_list)==check:
        team1=0
        for num in team_list:
            for path in team_list:
                team1+=player[num][path]
        
        team2_list=[]
        for i in range(N):
            if i not in team_list:
                team2_list.append(i)
        team2=0
        for num in team2_list:
            for path in team2_list:
                team2+=player[num][path] 
        
        minus=abs(team1-team2)
        if answer>minus:
            answer=minus
        return
    for k in range(num+1, N):
        dfs(k)
        team_list.pop()
            
    
dfs(0)
print(answer)
