def solution(n,votes):
    arr = [0 for i in range(n+1)]
    for i in range(len(votes)):
        for j in range(i):
            arr[votes[i][j]] += 1
    return arr