coordinate = [[0 for _ in range(101)] for _ in range(101)]

count = int(input())

for _ in range(count):
    x,y = list(map(int,input().split()))
    for i in range(x,x+10):
        for j in range(y,y+10):
            coordinate[i][j] = 1

result = 0
for i in coordinate:
    result += i.count(1)

print(result)