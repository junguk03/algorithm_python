width, height = map(int,input().split())

arr1 = [list(map(int,input().split())) for _ in range(width)]
arr2 = [list(map(int,input().split())) for _ in range(width)]


for i in range(width):
    for j in range(height):
        print(arr1[i][j] + arr2[i][j],end=" ")
    print()