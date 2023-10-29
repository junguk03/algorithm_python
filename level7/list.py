def solution(num_list):
    arr1 = list()
    arr2 = list()
    for i in range(len(num_list)):
        if(int(num_list(i))%2 == 1):
            arr1.append(num_list[i])
        else:
            arr2.append(num_list[i])
    sum1 = "".join(arr1)
    sum2 = "".join(arr2)
    answer = int(sum1) + int(sum2)
    return answer

print(solution([3, 4, 5, 2, 1]))