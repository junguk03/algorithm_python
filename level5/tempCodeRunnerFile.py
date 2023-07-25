width, height = map(int,input().split())

arr1 = [list(map(int,input().split())) for _ in range(height)]
arr2 = [list(map(int,input().split())) for _ in range(height)]


for i in range(height):
    for j in range(width):
        print(arr1[i][j] + arr2[i][j],end=" ")
    print()