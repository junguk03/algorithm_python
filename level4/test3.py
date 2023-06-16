def solution(scores):
    prizes = {1:"Notebook",2:"Cake",3:"Coffee"}
    answer = {}
    for name in scores:
        rank = 1
        for s in scores:
            if(scores[name]<scores[s]):
                rank += 1
        if(rank in prizes):
            answer[name] = prizes[rank]
        else:
            answer[name] = "None"

    return answer

scores = []
for i in range(4):
    scores.append(int(input()))
print(solution(scores))