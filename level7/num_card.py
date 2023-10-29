N = int(input())
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))
count = 0

arr3 = list(set(arr1) & set(arr2))
for i in arr2:
    if i in arr3:
        arr2[count] = "1"
    else:
        arr2[count] = "0"
    count += 1

for i in range(M):
    print(arr2[i],end = " ")