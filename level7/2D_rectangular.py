coordinate = [list(map(int,input().split())) for _ in range(3)]
x1 = int()
y1 = int()

if coordinate[0][0] == coordinate[1][0]:
    x1 = coordinate[2][0]
elif coordinate[0][0] == coordinate[2][0]:
    x1 = coordinate[1][0]
elif coordinate[1][0] == coordinate[2][0]:
    x1 = coordinate[0][0]

if coordinate[0][1] == coordinate[1][1]:
    y1 = coordinate[2][1]
elif coordinate[0][1] == coordinate[2][1]:
    y1 = coordinate[1][1]
elif coordinate[1][1] == coordinate[2][1]:
    y1 = coordinate[0][1]

print(x1,y1)