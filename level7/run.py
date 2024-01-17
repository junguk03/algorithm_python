from collections import deque

def solution(players, callings):
    index = 0
    num = 1
    player_index = {player: idx for idx, player in enumerate(players)}
    players = deque(players)
    while(1):
        if(index + num < len(callings)):
            if(callings[index] == callings[index + num]):
                num += 1
            else:
                num1 = player_index[callings[index]]
                player_index[callings[index]] -= num
                print(callings[index])
                for name, player_idx in player_index.items():
                    if(player_idx >= player_index[callings[index]] and player_idx < num1):
                        player_index[name] += 1
                player_index[callings[index]] -= 1
                index += num
                num = 1
        elif(index + num == len(callings)):
            player_index[callings[index]] -= num
            print(callings[index])
            for name, player_idx in player_index.items():
                if(player_idx >= player_index[callings[index]] and player_idx < num1):
                    player_index[name] += 1
            player_index[callings[index]] -= 1
            break
    print(player_index)
    player_index1 = dict(sorted(zip(player_index.values(), player_index.keys())))
    return player_index1

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "kai", "mine"]))