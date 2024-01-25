from itertools import combinations

def solution(sequence, k):
    arr = list()
    sequence1 = {num1: num2 for num2, num1 in sequence}
    for i in range(len(sequence)):
        for num in combinations(sequence,i+1):
            sum1 = sum(num)
            if(sum1 == k):
                arr.append(sequence1[num[0]])
                arr.append(sequence1[num[-1]])
                break
        if(sum1 == k):
            break
    return 

print(solution([1, 2, 3, 4, 5],7))


